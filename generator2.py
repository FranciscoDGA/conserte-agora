import os
import json

base_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Conserte Agora</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>
    <header>
        <div class="header-container">
            <div class="logo">
                <a href="index.html">Conserte<span>Agora</span></a>
            </div>
            <nav class="main-nav">
                <ul>
                    <li><a href="index.html">Início</a></li>
                    <li><a href="categorias/consertos-domesticos.html">Consertos Domésticos</a></li>
                    <li><a href="categorias/limpeza-e-manutencao.html">Limpeza</a></li>
                    <li><a href="categorias/organizacao-de-espacos.html">Organização</a></li>
                    <li><a href="categorias/produtos-e-ferramentas.html">Ferramentas</a></li>
                    <li><a href="categorias/dicas-rapidas.html">Dicas Rápidas</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main class="article-container" style="text-align: center; padding: 5rem 2rem;">
        {content}
    </main>
    <script src="js/main.js"></script>
</body>
</html>"""

# 404 page
content_404 = """
<h1 style="font-size: 4rem; color: var(--primary-color);">404</h1>
<h2>Página não encontrada</h2>
<p>Desculpe, a página que você está procurando não existe ou foi movida.</p>
<a href="index.html" class="btn btn-primary" style="display: inline-block; margin-top: 2rem;">Voltar para o Início</a>
"""
with open("404.html", "w", encoding="utf-8") as f:
    f.write(base_html.format(title="Página não encontrada", content=content_404))

# Busca page
content_busca = """
<h1>Resultados da Busca</h1>
<div id="search-results" style="text-align: left; margin-top: 2rem;">
    <p>Buscando...</p>
</div>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const query = urlParams.get('q');
        const resultsDiv = document.getElementById('search-results');
        
        if (!query) {
            resultsDiv.innerHTML = '<p>Digite algo para buscar.</p>';
            return;
        }
        
        fetch('search.json')
            .then(res => res.json())
            .then(data => {
                const results = data.filter(item => 
                    item.title.toLowerCase().includes(query.toLowerCase()) || 
                    item.desc.toLowerCase().includes(query.toLowerCase())
                );
                
                if (results.length === 0) {
                    resultsDiv.innerHTML = '<p>Nenhum resultado encontrado para "'+query+'".</p>';
                    return;
                }
                
                let html = '<ul style="list-style: none; padding: 0;">';
                results.forEach(item => {
                    html += `<li style="margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid #eee;">
                        <a href="${item.url}" style="font-size: 1.2rem; font-weight: bold; color: var(--primary-color);">${item.title}</a>
                        <p style="color: var(--light-text); margin-top: 0.5rem;">${item.desc}</p>
                    </li>`;
                });
                html += '</ul>';
                resultsDiv.innerHTML = html;
            });
    });
</script>
"""
with open("busca.html", "w", encoding="utf-8") as f:
    f.write(base_html.format(title="Busca", content=content_busca))

# search.json
# We'll just generate a basic one based on the articles in the directories
import glob


search_data = []
articles = glob.glob("artigos/*.html")
for article in articles:
    with open(article, "r", encoding="utf-8") as f:
        html = f.read()
        title_start = html.find("<h1>") + 4
        title_end = html.find("</h1>")
        title = html[title_start:title_end] if title_start != 3 else os.path.basename(article)
        search_data.append({
            "title": title,
            "url": article.replace("\\", "/"),
            "desc": "Aprenda sobre " + title
        })

with open("search.json", "w", encoding="utf-8") as f:
    json.dump(search_data, f, ensure_ascii=False)

# robots.txt
robots_content = """User-agent: *
Allow: /
Sitemap: https://www.conserteagora.com.br/sitemap.xml
"""
with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

# sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
pages = glob.glob("*.html") + glob.glob("categorias/*.html") + glob.glob("artigos/*.html")
for page in pages:
    page = page.replace("\\", "/")
    sitemap_content += f"  <url>\n    <loc>https://www.conserteagora.com.br/{page}</loc>\n  </url>\n"
sitemap_content += "</urlset>"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)
    
print("Complementary files generated")
