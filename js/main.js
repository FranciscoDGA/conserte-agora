(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.ConserteSearch = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  const STOPWORDS = new Set([
    'a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas',
    'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas',
    'por', 'para', 'com', 'sem', 'sob', 'sobre', 'entre',
    'e', 'ou', 'mas', 'que', 'se', 'como', 'qual', 'quais',
    'quando', 'onde', 'porque', 'porquê', 'fazer', 'meu', 'minha', 'sua', 'seu'
  ]);

  const ZERO_RESULTS_STORAGE_KEY = 'conserteAgora_zeroResultsAggregate_v1';
  const MAX_AGGREGATED_TERMS = 50;

  function normalizeText(str) {
    if (!str || typeof str !== 'string') return '';
    return str
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .toLowerCase()
      .replace(/[^a-z0-9\s]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function stemToken(token) {
    if (!token || token.length < 4) return token;
    let t = token;
    if (t.endsWith('oes') && t.length > 5) t = t.slice(0, -3) + 'ao';
    else if (t.endsWith('aes') && t.length > 5) t = t.slice(0, -3) + 'ao';
    else if (t.endsWith('ais') && t.length > 5) t = t.slice(0, -3) + 'al';
    else if (t.endsWith('res') && t.length > 5) t = t.slice(0, -2);
    else if (t.endsWith('s') && !t.endsWith('ss') && t.length > 4) t = t.slice(0, -1);

    if (t.length >= 7) {
      if (t.endsWith('ando') || t.endsWith('endo') || t.endsWith('indo')) {
        t = t.slice(0, -4);
      } else if (t.endsWith('amento') || t.endsWith('imento')) {
        t = t.slice(0, -6);
      } else if (t.endsWith('acao') || t.endsWith('icao')) {
        t = t.slice(0, -4);
      }
    } else if (t.length >= 6) {
      if (t.endsWith('ar') || t.endsWith('er') || t.endsWith('ir')) {
        t = t.slice(0, -2);
      }
    }
    return t;
  }

  function tokenize(str, keepStopwords) {
    const norm = normalizeText(str);
    if (!norm) return [];
    const rawTokens = norm.split(' ').filter(Boolean);
    const filtered = keepStopwords
      ? rawTokens
      : rawTokens.filter(t => t.length > 1 && !STOPWORDS.has(t));
    return filtered.length > 0 ? filtered : rawTokens.filter(t => t.length > 1);
  }

  // Damerau-Levenshtein distance (supports insertion, deletion, substitution, adjacent transposition)
  function editDistance(a, b) {
    if (a === b) return 0;
    const la = a.length;
    const lb = b.length;
    if (Math.abs(la - lb) > 2) return 99;
    const dp = Array.from({ length: la + 1 }, () => new Array(lb + 1).fill(0));
    for (let i = 0; i <= la; i++) dp[i][0] = i;
    for (let j = 0; j <= lb; j++) dp[0][j] = j;

    for (let i = 1; i <= la; i++) {
      for (let j = 1; j <= lb; j++) {
        const cost = a[i - 1] === b[j - 1] ? 0 : 1;
        dp[i][j] = Math.min(
          dp[i - 1][j] + 1,
          dp[i][j - 1] + 1,
          dp[i - 1][j - 1] + cost
        );
        if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) {
          dp[i][j] = Math.min(dp[i][j], dp[i - 2][j - 2] + 1);
        }
      }
    }
    return dp[la][lb];
  }

  function sameInitialGroup(c1, c2) {
    if (c1 === c2) return true;
    const sibilants = new Set(['s', 'c', 'z']);
    if (sibilants.has(c1) && sibilants.has(c2)) return true;
    const palatals = new Set(['g', 'j']);
    if (palatals.has(c1) && palatals.has(c2)) return true;
    return false;
  }

  function tokenMatchesFieldTokens(qToken, fieldTokens) {
    const qStem = stemToken(qToken);

    for (const fToken of fieldTokens) {
      if (fToken === qToken) return { matched: true, quality: 1.0 };
      const fStem = stemToken(fToken);
      if (fStem === qStem && qStem.length >= 4) return { matched: true, quality: 0.92 };

      // Prefix match on meaningful roots (>= 4 chars)
      if (qToken.length >= 4 && fToken.length >= 4) {
        if (fToken.startsWith(qToken) || qToken.startsWith(fToken)) {
          const minLen = Math.min(qToken.length, fToken.length);
          if (minLen >= 5 || Math.abs(qToken.length - fToken.length) <= 2) {
            return { matched: true, quality: 0.85 };
          }
        }
        if (qStem.length >= 5 && fStem.length >= 5 && (fStem.startsWith(qStem) || qStem.startsWith(fStem))) {
          return { matched: true, quality: 0.82 };
        }
      }

      // Controlled typo tolerance: max edit distance 1 for words >= 5 chars (or distance <= 2 for words >= 9 chars)
      if (qToken.length >= 5 && fToken.length >= 5 && sameInitialGroup(qToken[0], fToken[0])) {
        const dist = editDistance(qToken, fToken);
        if (dist === 1) return { matched: true, quality: 0.72 };
        if (dist === 2 && qToken.length >= 9 && fToken.length >= 8) {
          return { matched: true, quality: 0.65 };
        }
        const stemDist = editDistance(qStem, fStem);
        if (qStem.length >= 5 && fStem.length >= 5 && stemDist === 1) {
          return { matched: true, quality: 0.68 };
        }
      }
    }
    return { matched: false, quality: 0 };
  }

  function searchItems(items, rawQuery) {
    const normQuery = normalizeText(rawQuery);
    if (!normQuery || !Array.isArray(items)) return [];

    const queryTokens = tokenize(rawQuery, false);
    if (queryTokens.length === 0) return [];

    const scoredResults = [];

    for (const item of items) {
      const normTitle = normalizeText(item.title || '');
      const normDesc = normalizeText(item.desc || '');
      const normCat = normalizeText(item.category || '');
      const keywordsList = Array.isArray(item.keywords) ? item.keywords : [];
      const normKeywords = normalizeText(keywordsList.join(' '));

      const titleTokens = tokenize(normTitle, true);
      const kwTokens = tokenize(normKeywords, true);
      const catTokens = tokenize(normCat, true);
      const descTokens = tokenize(normDesc, true);

      let score = 0;
      let matchedTokensCount = 0;

      // Exact phrase bonus
      if (normTitle.includes(normQuery)) score += 45;
      if (normKeywords.includes(normQuery)) score += 35;
      if (normCat.includes(normQuery)) score += 20;
      if (normDesc.includes(normQuery)) score += 15;

      for (const qToken of queryTokens) {
        const mTitle = tokenMatchesFieldTokens(qToken, titleTokens);
        const mKw = tokenMatchesFieldTokens(qToken, kwTokens);
        const mCat = tokenMatchesFieldTokens(qToken, catTokens);
        const mDesc = tokenMatchesFieldTokens(qToken, descTokens);

        const bestQuality = Math.max(mTitle.quality, mKw.quality, mCat.quality, mDesc.quality);
        if (bestQuality > 0) {
          matchedTokensCount++;
          if (mTitle.matched) score += 24 * mTitle.quality;
          if (mKw.matched) score += 18 * mKw.quality;
          if (mCat.matched) score += 10 * mCat.quality;
          if (mDesc.matched) score += 8 * mDesc.quality;
        }
      }

      // Require all tokens to match for 1-2 word queries, or at least ceil(0.75 * N) tokens for longer queries
      const minRequiredTokens = queryTokens.length <= 2
        ? queryTokens.length
        : Math.ceil(queryTokens.length * 0.75);

      if (matchedTokensCount >= minRequiredTokens && score >= 10) {
        // Slight boost for complete guide articles over category overview pages
        if (item.type !== 'categoria') {
          score += 5;
        }
        scoredResults.push({ item, score });
      }
    }

    scoredResults.sort((a, b) => b.score - a.score);
    return scoredResults.map(r => r.item);
  }

  // Privacy-safe check: reject queries that resemble emails, phone numbers, CPFs, or URLs
  function looksLikePersonalData(rawQuery) {
    if (!rawQuery || typeof rawQuery !== 'string') return true;
    const trimmed = rawQuery.trim();
    if (trimmed.length < 2 || trimmed.length > 50) return true;
    if (/@/.test(trimmed)) return true;
    if (/https?:\/\/|www\./i.test(trimmed)) return true;
    // 4 or more digits in the query (phones, CPFs, CEPs, house numbers)
    const digitCount = (trimmed.match(/\d/g) || []).length;
    if (digitCount >= 4) return true;
    return false;
  }

  function recordZeroResult(rawQuery, storageOverride) {
    if (looksLikePersonalData(rawQuery)) return null;
    const normalizedTerm = normalizeText(rawQuery);
    if (!normalizedTerm || normalizedTerm.length < 2) return null;

    const storage = storageOverride || (typeof localStorage !== 'undefined' ? localStorage : null);
    if (!storage) return { term: normalizedTerm, count: 1 };

    try {
      const raw = storage.getItem(ZERO_RESULTS_STORAGE_KEY);
      const data = raw ? JSON.parse(raw) : {};
      const today = new Date().toISOString().slice(0, 10);

      if (!data[normalizedTerm]) {
        data[normalizedTerm] = { count: 0, lastDate: today };
      }
      data[normalizedTerm].count += 1;
      data[normalizedTerm].lastDate = today;

      // Keep bounded to top MAX_AGGREGATED_TERMS
      const entries = Object.entries(data)
        .sort((a, b) => b[1].count - a[1].count)
        .slice(0, MAX_AGGREGATED_TERMS);

      const bounded = Object.fromEntries(entries);
      storage.setItem(ZERO_RESULTS_STORAGE_KEY, JSON.stringify(bounded));
      return { term: normalizedTerm, count: bounded[normalizedTerm].count, lastDate: today };
    } catch (_) {
      return { term: normalizedTerm, count: 1 };
    }
  }

  function getZeroResultStats(storageOverride) {
    const storage = storageOverride || (typeof localStorage !== 'undefined' ? localStorage : null);
    if (!storage) return [];
    try {
      const raw = storage.getItem(ZERO_RESULTS_STORAGE_KEY);
      if (!raw) return [];
      const data = JSON.parse(raw);
      return Object.entries(data)
        .map(([term, info]) => ({ term, count: info.count, lastDate: info.lastDate }))
        .sort((a, b) => b.count - a.count);
    } catch (_) {
      return [];
    }
  }

  function resolveSearchPageUrl(query) {
    const path = (typeof window !== 'undefined' && window.location && window.location.pathname) || '';
    const isSubdir = /\/(artigos|categorias)\//i.test(path);
    const base = isSubdir ? '../busca.html' : 'busca.html';
    return `${base}?q=${encodeURIComponent(query)}`;
  }

  if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => {
      // Cookies Banner
      const cookieBanner = document.getElementById('cookieBanner');
      const acceptBtn = document.getElementById('acceptCookies');

      try {
        if (!localStorage.getItem('cookiesAccepted')) {
          if (cookieBanner) {
            cookieBanner.style.display = 'flex';
          }
        }
      } catch (_) {}

      if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
          try {
            localStorage.setItem('cookiesAccepted', 'true');
          } catch (_) {}
          if (cookieBanner) cookieBanner.style.display = 'none';
        });
      }

      // Header Search Bar Enhancement (supports Enter key, clickable button, explicit label, and empty-input error message)
      const searchBars = document.querySelectorAll('.search-bar');
      searchBars.forEach((bar, idx) => {
        const input = bar.querySelector('input');
        if (!input) return;

        if (!input.id) {
          input.id = `headerSearchInput_${idx}`;
        }

        if (!bar.querySelector('label')) {
          const label = document.createElement('label');
          label.className = 'sr-only';
          label.setAttribute('for', input.id);
          label.textContent = 'Buscar soluções no site';
          bar.insertBefore(label, input);
        }

        let errBox = bar.querySelector('.header-search-error');
        if (!errBox) {
          errBox = document.createElement('div');
          errBox.className = 'form-error-msg header-search-error';
          errBox.setAttribute('role', 'alert');
          errBox.hidden = true;
          errBox.textContent = 'Digite um termo (ex.: pia, fechadura ou mofo) para buscar.';
          bar.appendChild(errBox);
        }

        const triggerSearch = () => {
          const query = input.value.trim();
          if (query) {
            errBox.hidden = true;
            input.removeAttribute('aria-invalid');
            window.location.href = resolveSearchPageUrl(query);
          } else {
            errBox.hidden = false;
            input.setAttribute('aria-invalid', 'true');
            input.focus();
          }
        };

        input.addEventListener('input', () => {
          if (input.value.trim()) {
            errBox.hidden = true;
            input.removeAttribute('aria-invalid');
          }
        });

        input.addEventListener('keydown', (e) => {
          if (e.key === 'Enter') {
            e.preventDefault();
            triggerSearch();
          }
        });

        if (!bar.querySelector('.search-bar-btn')) {
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'search-bar-btn';
          btn.setAttribute('aria-label', 'Executar busca');
          btn.title = 'Buscar';
          btn.textContent = 'Buscar';
          btn.addEventListener('click', triggerSearch);
          bar.insertBefore(btn, errBox);
        }
      });

      // Home Hero Search Form Validation Feedback
      const heroForm = document.querySelector('.home-hero-search-form');
      if (heroForm) {
        const heroInput = heroForm.querySelector('input[name="q"]');
        heroForm.setAttribute('novalidate', 'novalidate');
        let heroErr = document.getElementById('homeHeroSearchError');
        if (!heroErr) {
          heroErr = document.createElement('p');
          heroErr.id = 'homeHeroSearchError';
          heroErr.className = 'form-error-msg';
          heroErr.setAttribute('role', 'alert');
          heroErr.hidden = true;
          heroErr.textContent = 'Por favor, digite o problema, ambiente ou objeto que você deseja procurar.';
          heroForm.insertAdjacentElement('afterend', heroErr);
        }
        if (heroInput) {
          heroInput.addEventListener('input', () => {
            if (heroInput.value.trim()) {
              heroErr.hidden = true;
              heroInput.removeAttribute('aria-invalid');
            }
          });
          heroForm.addEventListener('submit', (e) => {
            if (!heroInput.value.trim()) {
              e.preventDefault();
              heroErr.hidden = false;
              heroInput.setAttribute('aria-invalid', 'true');
              heroInput.focus();
            }
          });
        }
      }
    });
  }

  return {
    normalizeText,
    stemToken,
    tokenize,
    editDistance,
    searchItems,
    looksLikePersonalData,
    recordZeroResult,
    getZeroResultStats
  };
});
