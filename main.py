import pandas as pd
from datetime import datetime
import gspread

def compara_dia(tabela, indice):
    coluna_dia = tabela['Dia']
    dia_hoje = datetime.now().day
    for i in range(len(coluna_dia)):
        dia = coluna_dia.iloc[i]
        if dia == dia_hoje:
            indice.append(i)

def compara_mes(tabela, indice):
    coluna_mes = tabela['Mes']
    mes_hoje = datetime.now().month
    for i in range(len(df)):
        mes = coluna_mes.iloc[i]
        if mes == mes_hoje:
            indice.append(i)

NOME_PLANILHA = 'Birthday'

try:
    print("Conectando com a API do Google Sheets...")

    #Carrega as credenciais a partir do arquivo JSON
    gc = gspread.service_account(filename='birthday-templete.json')

    planilha = gc.open(NOME_PLANILHA)

    #Le todoa os dados da planilha
    primeira_aba = planilha.worksheet('Aniversarios')
    registros = primeira_aba.get_all_records()

    df = pd.DataFrame(registros)

    indice_dia = []
    indice_mes = []
    aniverssariante = []

    compara_dia(df, indice_dia)
    compara_mes(df, indice_mes)

    for item1 in indice_dia:
        for item2 in indice_mes:
            if item1 == item2:
                aniverssariante.append(item1)

    nomes_aniversariantes = df.iloc[aniverssariante]['Nome']
    for nome in nomes_aniversariantes:
        print("Feliz aniversário", nome, "!")

except FileNotFoundError:
    print("Erro: O arquivo 'teste.xlsx' não foi encontrado.")
except gspread.exceptions.SpreadsheetNotFound:
    print(f"ERRO: Planilha '{NOME_PLANILHA}' não encontrada. Verifique o nome e o compartilhamento.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")