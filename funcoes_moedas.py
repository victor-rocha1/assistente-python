from requests import get

def cotacao_moeda(moeda):
    try:
        if moeda == "Dólar":
            url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
        elif moeda == "Euro":
            url = 'https://economia.awesomeapi.com.br/json/last/EUR-BRL'
        elif moeda == "Bitcoin":
            url = 'https://economia.awesomeapi.com.br/json/last/BTC-BRL'
        else:
            return 'Moeda não suportada.'

        requisicao = get(url)
        cotacao = requisicao.json()
        nome = cotacao[list(cotacao.keys())[0]]['name']
        data = cotacao[list(cotacao.keys())[0]]['create_date']
        valor = cotacao[list(cotacao.keys())[0]]['bid']
        return f'Cotacão do {nome} em {data} é {valor} reais.'
    except Exception:
        return 'Erro ao obter a cotação. Verifique sua conexão.'