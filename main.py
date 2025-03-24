import requests
import pandas as pd


def requestsApiBcb(data):
    """Funcao para extrair os dados dos meios de pagamentos trimestrais do Banco Central
    Parametros:
    Data - string - aaaat (Ex:20191)"""
    
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    req = requests.get(url)
    dados = req.json()
    df = pd.json_normalize(dados['value'])
    return print(df)

requestsApiBcb(20241)