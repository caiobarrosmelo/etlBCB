import pandas as pd
import sqlite3
from sqlalchemy import create_engine


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


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    conn = sqlite3.connect(nome_banco)
    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)
    conn.close()
    return


def salvarMySQL(
    df: pd.DataFrame,
    usuario: str,
    senha: str,
    host: str,
    nome_banco: str,
    nome_tabela: str,
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{nome_banco}")
    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
    return
