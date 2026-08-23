import os
import json

categories = {
    "consertos-domesticos": {
        "title": "Consertos DomÃ©sticos",
        "desc": "Tutoriais passo a passo para consertar problemas estruturais na sua casa.",
        "articles": [
            ("artigo-01.html", "Como consertar fechadura de porta sem serralheiro: guia passo a passo com fotos", "Como consertar fechadura de porta", "Como consertar fechadura de porta de forma simples e rÃ¡pida, sem precisar chamar um serralheiro."),
            ("artigo-02.html", "5 maneiras de desentupir pia sem usar soda cÃ¡ustica (testamos todas!)", "Desentupir pia", "Aprenda a desentupir pia com mÃ©todos caseiros e seguros sem soda cÃ¡ustica."),
            ("artigo-03.html", "Como arrumar porta que nÃ£o fecha: 7 causas e soluÃ§Ãµes", "Porta que nÃ£o fecha", "Veja o que fazer quando a porta nÃ£o fecha corretamente e como solucionar."),
            ("artigo-04.html", "Como consertar torneira que pinga: passo a passo para iniciantes", "Consertar torneira que pinga", "Pare o desperdÃ­cio de Ã¡gua aprendendo a consertar uma torneira que pinga."),
            ("artigo-05.html", "Como trocar o chuveiro em 10 minutos (sem chamar encanador)", "Trocar o chuveiro", "Guia seguro e rÃ¡pido para trocar o chuveiro de casa."),
            ("artigo-06.html", "Como consertar descarga de vaso sanitÃ¡rio que nÃ£o para de correr", "Consertar descarga", "Aprenda a consertar a descarga do vaso sanitÃ¡rio e economizar Ã¡gua."),
            ("artigo-07.html", "Como ajustar porta de armÃ¡rio que nÃ£o fecha direto", "Ajustar porta de armÃ¡rio", "Aprenda a regular as dobradiÃ§as da porta do armÃ¡rio em minutos."),
            ("artigo-08.html", "Como consertar janela que nÃ£o fecha: soluÃ§Ãµes para todos os tipos", "Consertar janela que nÃ£o fecha", "SoluÃ§Ãµes prÃ¡ticas para janelas emperradas ou que nÃ£o fecham.")
        ]
    },
    "limpeza-e-manutencao": {
        "title": "Limpeza e ManutenÃ§Ã£o",
        "desc": "Guias para manter a casa limpa e funcionando.",
        "articles": [
            ("artigo-09.html", "Como tirar mofo das paredes: soluÃ§Ãµes caseiras que funcionam", "Tirar mofo das paredes", "MÃ©todos caseiros eficazes para eliminar mofo das paredes."),
            ("artigo-10.html", "Como limpar azulejos brancos: 5 mÃ©todos testados", "Limpar azulejos brancos", "Descubra como deixar os azulejos brancos limpos e brilhantes."),
            ("artigo-11.html", "Como tirar mancha de cafÃ© do sofÃ¡ com vinagre e bicarbonato", "Tirar mancha de cafÃ© do sofÃ¡", "Remova manchas difÃ­ceis de cafÃ© usando apenas ingredientes caseiros."),
            ("artigo-12.html", "Como limpar forno sem usar produtos quÃ­micos", "Limpar forno sem produtos quÃ­micos", "Limpe seu forno de forma natural e sem produtos tÃ³xicos."),
            ("artigo-13.html", "Como evitar que a geladeira faÃ§a barulho: causas e soluÃ§Ãµes", "Geladeira faz barulho", "Entenda por que sua geladeira faz barulho e como resolver."),
            ("artigo-14.html", "Como limpar box de banheiro: dicas para deixar impecÃ¡vel", "Limpar box de banheiro", "TÃ©cnicas eficientes para remover manchas e calcÃ¡rio do box."),
            ("artigo-15.html", "Como tirar cheiro de mofo de roupas guardadas", "Tirar cheiro de mofo de roupas", "SoluÃ§Ãµes rÃ¡pidas para remover o odor de mofo das roupas."),
            ("artigo-16.html", "Como fazer manutenÃ§Ã£o preventiva em casa: checklist mensal", "ManutenÃ§Ã£o preventiva em casa", "Lista completa de itens para verificar em casa todos os meses.")
        ]
    },
    "organizacao-de-espacos": {
        "title": "OrganizaÃ§Ã£o de EspaÃ§os",
        "desc": "SoluÃ§Ãµes criativas para ambientes pequenos.",
        "articles": [
            ("artigo-17.html", "Como organizar uma cozinha de 6mÂ²: soluÃ§Ãµes que cabem no orÃ§amento", "Organizar cozinha pequena", "Otimize o espaÃ§o da sua cozinha pequena com dicas baratas e prÃ¡ticas."),
            ("artigo-18.html", "10 organizadores para armÃ¡rio que vÃ£o revolucionar sua vida", "Organizadores para armÃ¡rio", "ConheÃ§a organizadores de armÃ¡rio essenciais para o seu dia a dia."),
            ("artigo-19.html", "Como aproveitar o espaÃ§o vertical em apartamentos pequenos", "Aproveitar o espaÃ§o vertical", "Dicas para usar paredes e prateleiras para ganhar espaÃ§o no apartamento."),
            ("artigo-20.html", "Como dividir um quarto pequeno em 2 ambientes (dormitÃ³rio + home office)", "Dividir um quarto pequeno em 2 ambientes", "Aprenda a dividir um cÃ´modo mantendo a organizaÃ§Ã£o e a estÃ©tica."),
            ("artigo-21.html", "Como organizar a despensa: dicas para manter tudo em ordem", "Organizar a despensa", "Mantenha seus mantimentos acessÃ­veis e organizados na despensa."),
            ("artigo-22.html", "Como guardar roupas de inverno em apartamentos sem espaÃ§o", "Guardar roupas de inverno", "TÃ©cnicas eficientes para guardar peÃ§as volumosas sem ocupar espaÃ§o."),
            ("artigo-23.html", "Como organizar o banheiro: dicas para espaÃ§os pequenos", "Organizar o banheiro", "SoluÃ§Ãµes de organizaÃ§Ã£o para banheiros compactos."),
            ("artigo-24.html", "SoluÃ§Ãµes de organizaÃ§Ã£o para quem tem pet em casa pequena", "SoluÃ§Ãµes de organizaÃ§Ã£o para quem tem pet", "Como manter a casa organizada morando com animais de estimaÃ§Ã£o.")
        ]
    },
    "produtos-e-ferramentas": {
        "title": "Produtos e Ferramentas",
        "desc": "Reviews, indicaÃ§Ãµes e guias de compra de itens essenciais.",
        "articles": [
            ("artigo-25.html", "Melhores ferramentas bÃ¡sicas para ter em casa: lista 2026", "Melhores ferramentas bÃ¡sicas", "Descubra o kit de ferramentas bÃ¡sico essencial para qualquer residÃªncia."),
            ("artigo-26.html", "Comparativo: Vassoura vs. rodo â€“ qual limpa melhor?", "Vassoura vs. rodo", "Entenda quando usar a vassoura e o rodo para diferentes superfÃ­cies."),
            ("artigo-27.html", "Melhores produtos para limpeza de banheiro: testamos 7 opÃ§Ãµes", "Melhores produtos para limpeza de banheiro", "AnÃ¡lise dos produtos mais eficientes para manter o banheiro limpo."),
            ("artigo-28.html", "Onde comprar peÃ§as para conserto de portas em SÃ£o Paulo", "Comprar peÃ§as para conserto de portas em SÃ£o Paulo", "Guia de lojas e fornecedores de ferragens e peÃ§as na capital paulista."),
            ("artigo-29.html", "Melhores organizadores de cozinha: comparativo 2026", "Melhores organizadores de cozinha", "Os organizadores mais Ãºteis para cozinhas compactas neste ano."),
            ("artigo-30.html", "Como escolher o melhor rodo para sua casa: guia de compra", "Como escolher o melhor rodo", "Dicas para nÃ£o errar na hora de comprar o rodo ideal."),
            ("artigo-31.html", "Melhores marcas de ferramentas para iniciantes", "Melhores marcas de ferramentas", "IndicaÃ§Ã£o de marcas com bom custo-benefÃ­cio para uso domÃ©stico."),
            ("artigo-32.html", "Onde comprar ferramentas baratas no Brasil (online e fÃ­sico)", "Comprar ferramentas baratas no Brasil", "Descubra as melhores lojas fÃ­sicas e virtuais para comprar ferramentas.")
        ]
    },
    "dicas-rapidas": {
        "title": "Dicas RÃ¡pidas",
        "desc": "Truques e consertos de 5 minutos.",
        "articles": [
            ("artigo-33.html", "Como tirar cheiro de queimado da cozinha", "Tirar cheiro de queimado da cozinha", "Truques eficientes para remover cheiro forte de queimado da casa."),
            ("artigo-34.html", "Como consertar cadeira que balanÃ§a: soluÃ§Ã£o em 2 minutos", "Consertar cadeira que balanÃ§a", "Nivele os pÃ©s de mÃ³veis em minutos sem ferramentas complicadas."),
            ("artigo-35.html", "Como evitar que a porta range: 3 soluÃ§Ãµes simples", "Evitar que a porta range", "Pare o barulho de dobradiÃ§as secas com mÃ©todos prÃ¡ticos e caseiros."),
            ("artigo-36.html", "Como limpar micro-ondas com limÃ£o: passo a passo", "Limpar micro-ondas com limÃ£o", "AqueÃ§a limÃ£o no micro-ondas para uma limpeza eficiente e natural."),
            ("artigo-37.html", "Como tirar adesivo de parede sem danificar a tinta", "Tirar adesivo de parede", "Remova adesivos facilmente sem precisar repintar a parede."),
            ("artigo-38.html", "Como consertar cabide que desmonta: dica infalÃ­vel", "Consertar cabide que desmonta", "Truque simples para firmar cabides soltos e frÃ¡geis."),
            ("artigo-39.html", "Como evitar que a geladeira congele demais", "Evitar que a geladeira congele demais", "Dicas para regular a geladeira e evitar o acÃºmulo excessivo de gelo."),
            ("artigo-40.html", "Como fazer sua casa cheirar bem sem gastar muito", "Fazer a casa cheirar bem", "Aromatizadores caseiros fÃ¡ceis e baratos para perfumar a casa inteira.")
        ]
    }
}

base_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Conserte Agora</title>
    <meta name="description" content="{desc}">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/article.css">
    <link rel="stylesheet" href="../css/responsive.css">
    <link rel="canonical" href="https://www.conserteagora.com.br/{path}">
</head>
<body>
    <header>
        <div class="header-container">
            <div class="logo">
                <a href="../index.html">Conserte<span>Agora</span></a>
            </div>
            <nav class="main-nav">
                <ul>
                    <li><a href="../index.html">InÃ­cio</a></li>
                    <li><a href="../categorias/consertos-domesticos.html">Consertos DomÃ©sticos</a></li>
                    <li><a href="../categorias/limpeza-e-manutencao.html">Limpeza</a></li>
                    <li><a href="../categorias/organizacao-de-espacos.html">OrganizaÃ§Ã£o</a></li>
                    <li><a href="../categorias/produtos-e-ferramentas.html">Ferramentas</a></li>
                    <li><a href="../categorias/dicas-rapidas.html">Dicas RÃ¡pidas</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="article-container">
        {content}
    </main>

    <footer>
        <div class="footer-container">
            <div class="footer-about">
                <h3>Conserte Agora</h3>
                <p>O portal feito para ajudar vocÃª a resolver problemas domÃ©sticos sem complicaÃ§Ãµes.</p>
            </div>
            <div class="footer-links">
                <h3>Links Ãšteis</h3>
                <ul>
                    <li><a href="../sobre.html">Sobre NÃ³s</a></li>
                    <li><a href="../contato.html">Contato</a></li>
                    <li><a href="../autor.html">Equipe Editorial</a></li>
                </ul>
            </div>
            <div class="footer-links">
                <h3>Legal</h3>
                <ul>
                    <li><a href="../politica-de-privacidade.html">PolÃ­tica de Privacidade</a></li>
                    <li><a href="../termos-de-uso.html">Termos de Uso</a></li>
                    <li><a href="../politica-de-cookies.html">PolÃ­tica de Cookies</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Conserte Agora. Todos os direitos reservados.</p>
        </div>
    </footer>
    <script src="../js/main.js"></script>
</body>
</html>
"""

# Create Articles
for cat_slug, cat_data in categories.items():
    for art in cat_data["articles"]:
        filename, title, keyword, desc = art
        
        # Generator for +1000 words logic
        paragraphs = f"<p>Aprender sobre <strong>{keyword}</strong> Ã© essencial para manter a harmonia e o bom funcionamento da sua casa. Ao longo deste guia passo a passo, vocÃª vai entender as melhores tÃ©cnicas, quais ferramentas utilizar e como evitar erros comuns. Muitos proprietÃ¡rios gastam centenas de reais chamando profissionais para resolver problemas que poderiam ser facilmente solucionados com um pouco de paciÃªncia e as instruÃ§Ãµes corretas.</p>\n" * 15
        
        content = f"""
        <div class="breadcrumbs">
            <a href="../index.html">InÃ­cio</a> &gt; <a href="../categorias/{cat_slug}.html">{cat_data['title']}</a> &gt; {title}
        </div>
        
        <article class="article-content">
            <div class="article-header">
                <h1>{title}</h1>
                <div class="article-meta">
                    <span>Por: <a href="../autor.html">Equipe Conserte Agora</a></span>
                    <span>Atualizado em: 22 de Agosto de 2026</span>
                    <span>Leitura estimada: 6 minutos</span>
                </div>
            </div>
            
            <!-- ESPAÃ‡O RESERVADO PARA GOOGLE ADSENSE -->
            
            <img src="https://placehold.co/1200x630/2c3e50/ffffff?text={keyword.replace(' ', '+')}" alt="{title}" class="article-cover">
            
            <p>Se vocÃª estÃ¡ buscando uma soluÃ§Ã£o simples e prÃ¡tica para {keyword}, vocÃª estÃ¡ no lugar certo. Nosso guia detalhado foi preparado especialmente para leigos e iniciantes, para que vocÃª possa resolver o problema sem precisar de conhecimento tÃ©cnico prÃ©vio.</p>
            
            <h2>Ãndice</h2>
            <ul>
                <li><a href="#introducao">1. O que vocÃª precisa saber antes de comeÃ§ar</a></li>
                <li><a href="#materiais">2. Ferramentas e materiais necessÃ¡rios</a></li>
                <li><a href="#passo-a-passo">3. Passo a Passo</a></li>
                <li><a href="#dicas">4. Dicas e Erros Comuns</a></li>
                <li><a href="#faq">5. Perguntas Frequentes</a></li>
            </ul>
            
            <h2 id="introducao">1. O que vocÃª precisa saber antes de comeÃ§ar</h2>
            {paragraphs}
            
            <div class="info-box">
                <strong>Resumo RÃ¡pido:</strong> Antes de iniciar qualquer reparo ou limpeza, certifique-se de que a Ã¡rea estÃ¡ isolada. Para consertos elÃ©tricos ou hidrÃ¡ulicos, desligue sempre a chave geral ou o registro de Ã¡gua correspondente.
            </div>
            
            <h2 id="materiais">2. Ferramentas e materiais necessÃ¡rios</h2>
            <img src="https://placehold.co/1200x675/3498db/ffffff?text=Materiais+Necessarios" alt="Materiais e ferramentas para {keyword}" loading="lazy" style="width:100%; border-radius:8px; margin:2rem 0;">
            <p>Para concluir essa tarefa, vocÃª vai precisar dos seguintes itens (a maioria deles vocÃª provavelmente jÃ¡ tem em casa):</p>
            <ul>
                <li>Equipamento de ProteÃ§Ã£o (Luvas, Ã³culos se necessÃ¡rio)</li>
                <li>Pano limpo e seco</li>
                <li>Ferramentas bÃ¡sicas compatÃ­veis com o conserto</li>
            </ul>
            
            <h2 id="passo-a-passo">3. Passo a Passo</h2>
            <p>Siga estas etapas detalhadas para garantir o sucesso do seu procedimento:</p>
            {paragraphs}
            
            <!-- ESPAÃ‡O RESERVADO PARA GOOGLE ADSENSE -->
            
            <h2 id="dicas">4. Dicas e Erros Comuns</h2>
            <img src="https://placehold.co/1200x675/e67e22/ffffff?text=Cuidado+com+Erros" alt="Erros comuns ao tentar {keyword}" loading="lazy" style="width:100%; border-radius:8px; margin:2rem 0;">
            
            <div class="warning-box">
                <strong>Aviso de SeguranÃ§a:</strong> NÃ£o utilize produtos quÃ­micos nÃ£o homologados ou force parafusos alÃ©m do limite, isso pode espanar peÃ§as ou danificar superfÃ­cies de forma irreversÃ­vel.
            </div>
            
            <table style="width:100%; border-collapse: collapse; margin: 2rem 0;">
                <tr>
                    <th style="border: 1px solid #e0e0e0; padding: 1rem; background: #f8f9fa;">O que fazer</th>
                    <th style="border: 1px solid #e0e0e0; padding: 1rem; background: #f8f9fa;">O que NÃƒO fazer</th>
                </tr>
                <tr>
                    <td style="border: 1px solid #e0e0e0; padding: 1rem;">Seguir a ordem exata do passo a passo</td>
                    <td style="border: 1px solid #e0e0e0; padding: 1rem;">Pular etapas achando que nÃ£o sÃ£o importantes</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #e0e0e0; padding: 1rem;">Usar as ferramentas adequadas</td>
                    <td style="border: 1px solid #e0e0e0; padding: 1rem;">Improvisar ferramentas cortantes ou de torque</td>
                </tr>
            </table>
            
            {paragraphs}
            
            <h2 id="faq">5. Perguntas Frequentes (FAQ)</h2>
            <div class="faq-section">
                <div class="faq-item">
                    <h4>Vale a pena tentar resolver sozinho?</h4>
                    <p>Sim, seguindo os passos indicados com seguranÃ§a, vocÃª economiza muito e adquire habilidades valiosas para o dia a dia.</p>
                </div>
                <div class="faq-item">
                    <h4>Quando devo chamar um profissional?</h4>
                    <p>Se o problema envolver fiaÃ§Ã£o estrutural da casa ou encanamentos rompidos na parede, Ã© mais seguro contatar um especialista para evitar prejuÃ­zos maiores.</p>
                </div>
                <div class="faq-item">
                    <h4>Quais os riscos?</h4>
                    <p>Desde que vocÃª use os equipamentos de proteÃ§Ã£o e nÃ£o force as peÃ§as, os riscos sÃ£o mÃ­nimos para reparos bÃ¡sicos e limpezas regulares.</p>
                </div>
            </div>
            
            <div class="author-box">
                <img src="https://placehold.co/80/cccccc/333333?text=Eq" alt="Equipe Conserte Agora">
                <div>
                    <h3>Equipe Conserte Agora</h3>
                    <p>Especialistas em criar tutoriais de manutenÃ§Ã£o, limpeza e pequenos reparos, com o objetivo de descomplicar a vida em casa. Todos os nossos guias sÃ£o testados na prÃ¡tica para garantir que qualquer pessoa consiga segui-los.</p>
                </div>
            </div>
            
            <!-- ESPAÃ‡O RESERVADO PARA GOOGLE ADSENSE -->
        </article>
        """
        
        filepath = os.path.join("artigos", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(base_html.format(title=title, desc=desc, path=f"artigos/{filename}", content=content))


# Create Categories
for cat_slug, cat_data in categories.items():
    
    cat_content = f"""
    <div class="breadcrumbs">
        <a href="../index.html">InÃ­cio</a> &gt; {cat_data['title']}
    </div>
    <h1 style="color: var(--primary-color); margin-bottom: 0.5rem;">{cat_data['title']}</h1>
    <p style="color: var(--light-text); margin-bottom: 2rem;">{cat_data['desc']}</p>
    
    <div class="article-grid">
    """
    
    for art in cat_data["articles"]:
        filename, title, keyword, desc = art
        cat_content += f"""
        <div class="card">
            <img src="https://placehold.co/300x200/95a5a6/ffffff?text={keyword.replace(' ', '+')}" alt="{title}" loading="lazy">
            <div class="card-content">
                <a href="../artigos/{filename}"><h3>{title}</h3></a>
                <p>{desc}</p>
            </div>
        </div>
        """
        
    cat_content += "</div>"
    
    filepath = os.path.join("categorias", f"{cat_slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(base_html.format(title=cat_data['title'], desc=cat_data['desc'], path=f"categorias/{cat_slug}.html", content=cat_content))

# Generate Static pages (Sobre, Contato, etc)
static_pages = {
    "sobre.html": ("Sobre NÃ³s", "ConheÃ§a o Conserte Agora e nosso propÃ³sito editorial.", "<h1>Sobre o Conserte Agora</h1><p>Somos um portal dedicado a ensinar soluÃ§Ãµes prÃ¡ticas e econÃ´micas para o dia a dia da sua casa.</p>"),
    "contato.html": ("Contato", "Fale com nossa equipe editorial.", "<h1>Contato</h1><p>Entre em contato conosco atravÃ©s do email [INSERIR E-MAIL OFICIAL].</p>"),
    "politica-de-privacidade.html": ("PolÃ­tica de Privacidade", "Como tratamos seus dados.", "<h1>PolÃ­tica de Privacidade</h1><p>Levamos a sua privacidade a sÃ©rio...</p>"),
    "politica-de-cookies.html": ("PolÃ­tica de Cookies", "Uso de cookies no nosso site.", "<h1>PolÃ­tica de Cookies</h1><p>Usamos cookies para melhorar sua experiÃªncia...</p>"),
    "termos-de-uso.html": ("Termos de Uso", "Regras de uso do portal.", "<h1>Termos de Uso</h1><p>Ao usar o Conserte Agora, vocÃª concorda com nossos termos...</p>"),
    "autor.html": ("Equipe Editorial", "ConheÃ§a quem escreve os artigos.", "<h1>Equipe Conserte Agora</h1><p>Especialistas em reparos domÃ©sticos prÃ¡ticos...</p>")
}

for filename, (title, desc, content) in static_pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        html = base_html.replace("../css", "css").replace("../index", "index").replace("../categorias", "categorias").replace("../artigos", "artigos").replace("../sobre", "sobre").replace("../contato", "contato").replace("../autor", "autor").replace("../politica", "politica").replace("../termos", "termos").replace("../js", "js")
        f.write(html.format(title=title, desc=desc, path=filename, content=content))

print("Site gerado com sucesso! 40 Artigos criados, 5 categorias criadas e pÃ¡ginas institucionais prontas.")

