from etl import pipeline_consolidado_vendas

pasta: str = 'data'
formato_saida: list = ["csv", "parquet"]

pipeline_consolidado_vendas(pasta, formato_saida)