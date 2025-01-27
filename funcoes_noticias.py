from requests import get
from bs4 import BeautifulSoup

def ultima_noticias():
    url = 'https://news.google.com/rss?gl=BR&hl=pt-BR&ceid=BR:pt-419'
    try:
        site = get(url)
        noticias = BeautifulSoup(site.text, 'lxml')
        return [item.title.text for item in noticias.findAll('item')[:3]]
    except Exception:
        return ['Erro ao acessar as notícias. Verifique sua conexão.']