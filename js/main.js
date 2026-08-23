document.addEventListener('DOMContentLoaded', () => {
  // Cookies Banner
  const cookieBanner = document.getElementById('cookieBanner');
  const acceptBtn = document.getElementById('acceptCookies');
  
  if (!localStorage.getItem('cookiesAccepted')) {
    if (cookieBanner) {
      cookieBanner.style.display = 'flex';
    }
  }
  
  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      localStorage.setItem('cookiesAccepted', 'true');
      cookieBanner.style.display = 'none';
    });
  }

  // Search Functionality Mockup
  const searchInput = document.querySelector('.search-bar input');
  if (searchInput) {
    searchInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        const query = searchInput.value.trim();
        if (query) {
          window.location.href = `/busca.html?q=${encodeURIComponent(query)}`;
        }
      }
    });
  }
});
