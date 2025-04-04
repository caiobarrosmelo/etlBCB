import pandas as pd

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Salva um DataFrame em um arquivo CSV.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados a serem salvos.
    nome_arquivo (str): Nome do arquivo CSV onde os dados serão armazenados.
    separador (str, opcional): Caractere usado como delimitador de colunas no CSV. Padrão é ",".
    decimal (str, opcional): Caractere usado para representar casas decimais. Padrão é ".".
    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return
