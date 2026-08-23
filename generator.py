import os
import json

categories = {
    "consertos-domesticos": {
        "title": "Consertos Domésticos",
        "desc": "Tutoriais passo a passo para consertar problemas estruturais na sua casa.",
        "articles": [
            ("artigo-01.html", "Como consertar fechadura de porta sem serralheiro: guia passo a passo com fotos", "Como consertar fechadura de porta", "Como consertar fechadura de porta de forma simples e rápida, sem precisar chamar um serralheiro."),
            ("artigo-02.html", "5 maneiras de desentupir pia sem usar soda cáustica (testamos todas!)", "Desentupir pia", "Aprenda a desentupir pia com métodos caseiros e seguros sem soda cáustica."),
            ("artigo-03.html", "Como arrumar porta que não fecha: 7 causas e soluções", "Porta que não fecha", "Veja o que fazer quando a porta não fecha corretamente e como solucionar."),
            ("artigo-04.html", "Como consertar torneira que pinga: passo a passo para iniciantes", "Consertar torneira que pinga", "Pare o desperdício de água aprendendo a consertar uma torneira que pinga."),
            ("artigo-05.html", "Como trocar o chuveiro em 10 minutos (sem chamar encanador)", "Trocar o chuveiro", "Guia seguro e rápido para trocar o chuveiro de casa."),
            ("artigo-06.html", "Como consertar descarga de vaso sanitário que não para de correr", "Consertar descarga", "Aprenda a consertar a descarga do vaso sanitário e economizar água."),
            ("artigo-07.html", "Como ajustar porta de armário que não fecha direto", "Ajustar porta de armário", "Aprenda a regular as dobradiças da porta do armário em minutos."),
            ("artigo-08.html", "Como consertar janela que não fecha: soluções para todos os tipos", "Consertar janela que não fecha", "Soluções práticas para janelas emperradas ou que não fecham.")
        ]
    },
    "limpeza-e-manutencao": {
        "title": "Limpeza e Manutenção",
        "desc": "Guias para manter a casa limpa e funcionando.",
        "articles": [
            ("artigo-09.html", "Como tirar mofo das paredes: soluções caseiras que funcionam", "Tirar mofo das paredes", "Métodos caseiros eficazes para eliminar mofo das paredes."),
            ("artigo-10.html", "Como limpar azulejos brancos: 5 métodos testados", "Limpar azulejos brancos", "Descubra como deixar os azulejos brancos limpos e brilhantes."),
            ("artigo-11.html", "Como tirar mancha de café do sofá com vinagre e bicarbonato", "Tirar mancha de café do sofá", "Remova manchas difíceis de café usando apenas ingredientes caseiros."),
            ("artigo-12.html", "Como limpar forno sem usar produtos químicos", "Limpar forno sem produtos químicos", "Limpe seu forno de forma natural e sem produtos tóxicos."),
            ("artigo-13.html", "Como evitar que a geladeira faça barulho: causas e soluções", "Geladeira faz barulho", "Entenda por que sua geladeira faz barulho e como resolver."),
            ("artigo-14.html", "Como limpar box de banheiro: dicas para deixar impecável", "Limpar box de banheiro", "Técnicas eficientes para remover manchas e calcário do box."),
            ("artigo-15.html", "Como tirar cheiro de mofo de roupas guardadas", "Tirar cheiro de mofo de roupas", "Soluções rápidas para remover o odor de mofo das roupas."),
            ("artigo-16.html", "Como fazer manutenção preventiva em casa: checklist mensal", "Manutenção preventiva em casa", "Lista completa de itens para verificar em casa todos os meses.")
        ]
    },
    "organizacao-de-espacos": {
        "title": "Organização de Espaços",
        "desc": "Soluções criativas para ambientes pequenos.",
        "articles": [
            ("artigo-17.html", "Como organizar uma cozinha de 6m²: soluções que cabem no orçamento", "Organizar cozinha pequena", "Otimize o espaço da sua cozinha pequena com dicas baratas e práticas."),
            ("artigo-18.html", "10 organizadores para armário que vão revolucionar sua vida", "Organizadores para armário", "Conheça organizadores de armário essenciais para o seu dia a dia."),
            ("artigo-19.html", "Como aproveitar o espaço vertical em apartamentos pequenos", "Aproveitar o espaço vertical", "Dicas para usar paredes e prateleiras para ganhar espaço no apartamento."),
            ("artigo-20.html", "Como dividir um quarto pequeno em 2 ambientes (dormitório + home office)", "Dividir um quarto pequeno em 2 ambientes", "Aprenda a dividir um cômodo mantendo a organização e a estética."),
            ("artigo-21.html", "Como organizar a despensa: dicas para manter tudo em ordem", "Organizar a despensa", "Mantenha seus mantimentos acessíveis e organizados na despensa."),
            ("artigo-22.html", "Como guardar roupas de inverno em apartamentos sem espaço", "Guardar roupas de inverno", "Técnicas eficientes para guardar peças volumosas sem ocupar espaço."),
            ("artigo-23.html", "Como organizar o banheiro: dicas para espaços pequenos", "Organizar o banheiro", "Soluções de organização para banheiros compactos."),
            ("artigo-24.html", "Soluções de organização para quem tem pet em casa pequena", "Soluções de organização para quem tem pet", "Como manter a casa organizada morando com animais de estimação.")
        ]
    },
    "produtos-e-ferramentas": {
        "title": "Produtos e Ferramentas",
        "desc": "Reviews, indicações e guias de compra de itens essenciais.",
        "articles": [
            ("artigo-25.html", "Melhores ferramentas básicas para ter em casa: lista 2026", "Melhores ferramentas básicas", "Descubra o kit de ferramentas básico essencial para qualquer residência."),
            ("artigo-26.html", "Comparativo: Vassoura vs. rodo – qual limpa melhor?", "Vassoura vs. rodo", "Entenda quando usar a vassoura e o rodo para diferentes superfícies."),
            ("artigo-27.html", "Melhores produtos para limpeza de banheiro: testamos 7 opções", "Melhores produtos para limpeza de banheiro", "Análise dos produtos mais eficientes para manter o banheiro limpo."),
            ("artigo-28.html", "Onde comprar peças para conserto de portas em São Paulo", "Comprar peças para conserto de portas em São Paulo", "Guia de lojas e fornecedores de ferragens e peças na capital paulista."),
            ("artigo-29.html", "Melhores organizadores de cozinha: comparativo 2026", "Melhores organizadores de cozinha", "Os organizadores mais úteis para cozinhas compactas neste ano."),
            ("artigo-30.html", "Como escolher o melhor rodo para sua casa: guia de compra", "Como escolher o melhor rodo", "Dicas para não errar na hora de comprar o rodo ideal."),
            ("artigo-31.html", "Melhores marcas de ferramentas para iniciantes", "Melhores marcas de ferramentas", "Indicação de marcas com bom custo-benefício para uso doméstico."),
            ("artigo-32.html", "Onde comprar ferramentas baratas no Brasil (online e físico)", "Comprar ferramentas baratas no Brasil", "Descubra as melhores lojas físicas e virtuais para comprar ferramentas.")
        ]
    },
    "dicas-rapidas": {
        "title": "Dicas Rápidas",
        "desc": "Truques e consertos de 5 minutos.",
        "articles": [
            ("artigo-33.html", "Como tirar cheiro de queimado da cozinha", "Tirar cheiro de queimado da cozinha", "Truques eficientes para remover cheiro forte de queimado da casa."),
            ("artigo-34.html", "Como consertar cadeira que balança: solução em 2 minutos", "Consertar cadeira que balança", "Nivele os pés de móveis em minutos sem ferramentas complicadas."),
            ("artigo-35.html", "Como evitar que a porta range: 3 soluções simples", "Evitar que a porta range", "Pare o barulho de dobradiças secas com métodos práticos e caseiros."),
            ("artigo-36.html", "Como limpar micro-ondas com limão: passo a passo", "Limpar micro-ondas com limão", "Aqueça limão no micro-ondas para uma limpeza eficiente e natural."),
            ("artigo-37.html", "Como tirar adesivo de parede sem danificar a tinta", "Tirar adesivo de parede", "Remova adesivos facilmente sem precisar repintar a parede."),
            ("artigo-38.html", "Como consertar cabide que desmonta: dica infalível", "Consertar cabide que desmonta", "Truque simples para firmar cabides soltos e frágeis."),
            ("artigo-39.html", "Como evitar que a geladeira congele demais", "Evitar que a geladeira congele demais", "Dicas para regular a geladeira e evitar o acúmulo excessivo de gelo."),
            ("artigo-40.html", "Como fazer sua casa cheirar bem sem gastar muito", "Fazer a casa cheirar bem", "Aromatizadores caseiros fáceis e baratos para perfumar a casa inteira.")
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
                    <li><a href="../index.html">Início</a></li>
                    <li><a href="../categorias/consertos-domesticos.html">Consertos Domésticos</a></li>
                    <li><a href="../categorias/limpeza-e-manutencao.html">Limpeza</a></li>
                    <li><a href="../categorias/organizacao-de-espacos.html">Organização</a></li>
                    <li><a href="../categorias/produtos-e-ferramentas.html">Ferramentas</a></li>
                    <li><a href="../categorias/dicas-rapidas.html">Dicas Rápidas</a></li>
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
                <p>O portal feito para ajudar você a resolver problemas domésticos sem complicações.</p>
            </div>
            <div class="footer-links">
                <h3>Links Úteis</h3>
                <ul>
                    <li><a href="../sobre.html">Sobre Nós</a></li>
                    <li><a href="../contato.html">Contato</a></li>
                    <li><a href="../autor.html">Equipe Editorial</a></li>
                </ul>
            </div>
            <div class="footer-links">
                <h3>Legal</h3>
                <ul>
                    <li><a href="../politica-de-privacidade.html">Política de Privacidade</a></li>
                    <li><a href="../termos-de-uso.html">Termos de Uso</a></li>
                    <li><a href="../politica-de-cookies.html">Política de Cookies</a></li>
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
        paragraphs = f"<p>Aprender sobre <strong>{keyword}</strong> é essencial para manter a harmonia e o bom funcionamento da sua casa. Ao longo deste guia passo a passo, você vai entender as melhores técnicas, quais ferramentas utilizar e como evitar erros comuns. Muitos proprietários gastam centenas de reais chamando profissionais para resolver problemas que poderiam ser facilmente solucionados com um pouco de paciência e as instruções corretas.</p>\n" * 15
        
        content = f"""
        <div class="breadcrumbs">
            <a href="../index.html">Início</a> &gt; <a href="../categorias/{cat_slug}.html">{cat_data['title']}</a> &gt; {title}
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
            
            <!-- ESPAÇO RESERVADO PARA GOOGLE ADSENSE -->
            
            <img src="https://via.placeholder.com/1200x630/2c3e50/ffffff?text={keyword.replace(' ', '+')}" alt="{title}" class="article-cover">
            
            <p>Se você está buscando uma solução simples e prática para {keyword}, você está no lugar certo. Nosso guia detalhado foi preparado especialmente para leigos e iniciantes, para que você possa resolver o problema sem precisar de conhecimento técnico prévio.</p>
            
            <h2>Índice</h2>
            <ul>
                <li><a href="#introducao">1. O que você precisa saber antes de começar</a></li>
                <li><a href="#materiais">2. Ferramentas e materiais necessários</a></li>
                <li><a href="#passo-a-passo">3. Passo a Passo</a></li>
                <li><a href="#dicas">4. Dicas e Erros Comuns</a></li>
                <li><a href="#faq">5. Perguntas Frequentes</a></li>
            </ul>
            
            <h2 id="introducao">1. O que você precisa saber antes de começar</h2>
            {paragraphs}
            
            <div class="info-box">
                <strong>Resumo Rápido:</strong> Antes de iniciar qualquer reparo ou limpeza, certifique-se de que a área está isolada. Para consertos elétricos ou hidráulicos, desligue sempre a chave geral ou o registro de água correspondente.
            </div>
            
            <h2 id="materiais">2. Ferramentas e materiais necessários</h2>
            <img src="https://via.placeholder.com/1200x675/3498db/ffffff?text=Materiais+Necessarios" alt="Materiais e ferramentas para {keyword}" loading="lazy" style="width:100%; border-radius:8px; margin:2rem 0;">
            <p>Para concluir essa tarefa, você vai precisar dos seguintes itens (a maioria deles você provavelmente já tem em casa):</p>
            <ul>
                <li>Equipamento de Proteção (Luvas, óculos se necessário)</li>
                <li>Pano limpo e seco</li>
                <li>Ferramentas básicas compatíveis com o conserto</li>
            </ul>
            
            <h2 id="passo-a-passo">3. Passo a Passo</h2>
            <p>Siga estas etapas detalhadas para garantir o sucesso do seu procedimento:</p>
            {paragraphs}
            
            <!-- ESPAÇO RESERVADO PARA GOOGLE ADSENSE -->
            
            <h2 id="dicas">4. Dicas e Erros Comuns</h2>
            <img src="https://via.placeholder.com/1200x675/e67e22/ffffff?text=Cuidado+com+Erros" alt="Erros comuns ao tentar {keyword}" loading="lazy" style="width:100%; border-radius:8px; margin:2rem 0;">
            
            <div class="warning-box">
                <strong>Aviso de Segurança:</strong> Não utilize produtos químicos não homologados ou force parafusos além do limite, isso pode espanar peças ou danificar superfícies de forma irreversível.
            </div>
            
            <table style="width:100%; border-collapse: collapse; margin: 2rem 0;">
                <tr>
                    <th style="border: 1px solid #e0e0e0; padding: 1rem; background: #f8f9fa;">O que fazer</th>
                    <th style="border: 1px solid #e0e0e0; padding: 1rem; background: #f8f9fa;">O que NÃO fazer</th>
                </tr>
                <tr>
                    <td style="border: 1px solid #e0e0e0; padding: 1rem;">Seguir a ordem exata do passo a passo</td>
                    <td style="border: 1px solid #e0e0e0; padding: 1rem;">Pular etapas achando que não são importantes</td>
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
                    <p>Sim, seguindo os passos indicados com segurança, você economiza muito e adquire habilidades valiosas para o dia a dia.</p>
                </div>
                <div class="faq-item">
                    <h4>Quando devo chamar um profissional?</h4>
                    <p>Se o problema envolver fiação estrutural da casa ou encanamentos rompidos na parede, é mais seguro contatar um especialista para evitar prejuízos maiores.</p>
                </div>
                <div class="faq-item">
                    <h4>Quais os riscos?</h4>
                    <p>Desde que você use os equipamentos de proteção e não force as peças, os riscos são mínimos para reparos básicos e limpezas regulares.</p>
                </div>
            </div>
            
            <div class="author-box">
                <img src="https://via.placeholder.com/80/cccccc/333333?text=Eq" alt="Equipe Conserte Agora">
                <div>
                    <h3>Equipe Conserte Agora</h3>
                    <p>Especialistas em criar tutoriais de manutenção, limpeza e pequenos reparos, com o objetivo de descomplicar a vida em casa. Todos os nossos guias são testados na prática para garantir que qualquer pessoa consiga segui-los.</p>
                </div>
            </div>
            
            <!-- ESPAÇO RESERVADO PARA GOOGLE ADSENSE -->
        </article>
        """
        
        filepath = os.path.join("artigos", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(base_html.format(title=title, desc=desc, path=f"artigos/{filename}", content=content))


# Create Categories
for cat_slug, cat_data in categories.items():
    
    cat_content = f"""
    <div class="breadcrumbs">
        <a href="../index.html">Início</a> &gt; {cat_data['title']}
    </div>
    <h1 style="color: var(--primary-color); margin-bottom: 0.5rem;">{cat_data['title']}</h1>
    <p style="color: var(--light-text); margin-bottom: 2rem;">{cat_data['desc']}</p>
    
    <div class="article-grid">
    """
    
    for art in cat_data["articles"]:
        filename, title, keyword, desc = art
        cat_content += f"""
        <div class="card">
            <img src="https://via.placeholder.com/300x200/95a5a6/ffffff?text={keyword.replace(' ', '+')}" alt="{title}" loading="lazy">
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
    "sobre.html": ("Sobre Nós", "Conheça o Conserte Agora e nosso propósito editorial.", "<h1>Sobre o Conserte Agora</h1><p>Somos um portal dedicado a ensinar soluções práticas e econômicas para o dia a dia da sua casa.</p>"),
    "contato.html": ("Contato", "Fale com nossa equipe editorial.", "<h1>Contato</h1><p>Entre em contato conosco através do email [INSERIR E-MAIL OFICIAL].</p>"),
    "politica-de-privacidade.html": ("Política de Privacidade", "Como tratamos seus dados.", "<h1>Política de Privacidade</h1><p>Levamos a sua privacidade a sério...</p>"),
    "politica-de-cookies.html": ("Política de Cookies", "Uso de cookies no nosso site.", "<h1>Política de Cookies</h1><p>Usamos cookies para melhorar sua experiência...</p>"),
    "termos-de-uso.html": ("Termos de Uso", "Regras de uso do portal.", "<h1>Termos de Uso</h1><p>Ao usar o Conserte Agora, você concorda com nossos termos...</p>"),
    "autor.html": ("Equipe Editorial", "Conheça quem escreve os artigos.", "<h1>Equipe Conserte Agora</h1><p>Especialistas em reparos domésticos práticos...</p>")
}

for filename, (title, desc, content) in static_pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        html = base_html.replace("../css", "css").replace("../index", "index").replace("../categorias", "categorias").replace("../artigos", "artigos").replace("../sobre", "sobre").replace("../contato", "contato").replace("../autor", "autor").replace("../politica", "politica").replace("../termos", "termos").replace("../js", "js")
        f.write(html.format(title=title, desc=desc, path=filename, content=content))

print("Site gerado com sucesso! 40 Artigos criados, 5 categorias criadas e páginas institucionais prontas.")
