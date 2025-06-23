import requests
import pandas as pd
import os

url = "https://apisidra.ibge.gov.br/values/t/9542/n2/all/n3/all/n24/all/v/allxp/p/all/c59/allxt/c2/allxt/c86/allxt/c287/2999,3000,9482,9483,9484,93086,93087"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data[1:], columns=data[0])

novos_nomes = {
    "NC": "Nivel_Territorial_Codigo",
    "NN":"Nivel_Territorial",
    "D1C": "Nivel_Geografico_Codigo",
    "D1N":"Nivel_Geografico",
    "D2C": "Faixa_Etaria_Codigo",
    "D2N":"Faixa_Etaria",
    "D3C": "Ano_Codigo",
    "D3N":"Ano",
    "D4C": "Alfabetizacao_Codigo",
    "D4N":"Alfabetizacao",
    "D5C":"Sexo_Codigo",
    "D5N":"Sexo",
    "D6C":"Cor/Raca_Codigo",
    "D6N":"Cor/Raca",
    "D7C":"Idade_Codigo",
    "D7N":"Idade",
    "V": "Valor"
}

df = df.rename(columns=novos_nomes)

colunas_filtradas = ["Nivel_Territorial_Codigo", "Nivel_Territorial", "Nivel_Geografico_Codigo", "Nivel_Geografico",
         "Faixa_Etaria_Codigo", "Faixa_Etaria", "Ano_Codigo", "Ano", "Alfabetizacao_Codigo", "Alfabetizacao",
         "Sexo_Codigo", "Sexo", "Cor/Raca_Codigo", "Cor/Raca", "Idade_Codigo", "Idade", "Valor"]

df_filtrado = df[colunas_filtradas]

caminho_arquivo = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                               'dados', 'dados_alfabetizacao.csv')

df.to_csv(caminho_arquivo, index=False, encoding='utf-8-sig')

print(f"Dados salvos com sucesso em: {caminho_arquivo}")