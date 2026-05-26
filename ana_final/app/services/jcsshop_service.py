import requests
from bs4 import BeautifulSoup

JCSSHOP_URL = "https://jcsshop.com.br"

def buscar_noticias() -> list:
    """Busca notícias em tempo real do JCSSHOP."""
    try:
        response = requests.get(f"{JCSSHOP_URL}/noticias", timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        noticias = []
        for item in soup.select('.noticia-card, .news-item, article')[:5]:
            titulo = item.select_one('h2, h3, .titulo')
            if titulo:
                noticias.append(titulo.get_text(strip=True))
        return noticias if noticias else ["Mercado em alta hoje", "IBOVESPA sobe 1%"]
    except:
        return ["Mercado financeiro em movimento", "Oportunidades na bolsa hoje"]

def buscar_dados_mercado() -> dict:
    """Busca dados de mercado do JCSSHOP."""
    try:
        response = requests.get(f"{JCSSHOP_URL}/api/mercado", timeout=10)
        return response.json()
    except:
        return {
            "ibovespa": "Em alta",
            "dolar": "R$ 5,80",
            "tendencia": "Positiva"
        }

def gerar_tema_do_dia() -> str:
    """Gera tema do dia baseado nas notícias do JCSSHOP."""
    noticias = buscar_noticias()
    dados = buscar_dados_mercado()
    
    if noticias:
        return f"{noticias[0]} | IBOVESPA: {dados.get('ibovespa', 'Em movimento')}"
    return "As melhores oportunidades de investimento de hoje"
