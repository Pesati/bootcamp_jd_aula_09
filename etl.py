import pandas as pd
import os
import glob
from utils_log import log_decorator

# função para extrair e ler os dados json

@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_concat = pd.concat(df, ignore_index=True)
    return df_concat

# função para transformar os dados
@log_decorator
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# função para realizar o load e salvar em csv e/ou parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, formato_saida: list):
    
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        elif formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)
        else:
            df.to_excel("dados.xlsx", index=False)

@log_decorator
def pipeline_consolidado_vendas(pasta: str, formato_saida: list):
    dados_extraido = extrair_dados(pasta)
    total_vendas = calcular_kpi_total_vendas(dados_extraido)
    carregar_dados(total_vendas, formato_saida)

    
