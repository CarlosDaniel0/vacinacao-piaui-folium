import csv
import json
import pandas as pd

cod_municipios = open('id-municipios-pi.json')
cod_municipios = json.loads(cod_municipios.read())
dados_municipios = pd.read_csv('vacinacao_rnds.csv', delimiter=';')
#dados_municipios = pd.read_excel('vacinacao_rnds.xlsx', dtype='str')


def get_nome_por_cod(cod, df):
    return df[df['codarea'].isin([cod])]


def get_dados_por_nome(nome, df):
    return df[df['Município'].isin([nome])]


file = open('vacinacao_pi_map.csv', 'w', newline='', encoding='utf-8')
csv_file = csv.writer(file)
csv_file.writerow(['codarea', 'municipio', 'total_doses', 'doses_aplicadas', 'porcentagem'])

for i in range(len(cod_municipios)):
    print(cod_municipios[i]['municipio']['id'])
    print(cod_municipios[i]['municipio']['nome'])
    municipio = get_dados_por_nome(cod_municipios[i]['municipio']['nome'].title(), dados_municipios)
    print(municipio['Município'])

    total_doses = municipio['Doses Distribuídas às Secretarias Municipais de Saúde'].values[0]
    doses_aplicadas = municipio['Doses Aplicadas'].values[0]
    percentual = municipio['Relação entre doses distribuídas e doses aplicadas*'].values[0]

    # CSV
    try:
        percentual = percentual.replace(",", ".").replace("%", "")
        if float(percentual) > 100:
            percentual = 100
    except ValueError as e:
        percentual = 0

    # Excel
    """
    try:
        percentual = round(float(percentual) * 100, 1)
        if percentual > 100:
                percentual = 100
        #total_doses = format(float(total_doses)/1000, ".3f")
        #doses_aplicadas = format(float(doses_aplicadas)/1000, ".3f")
    except ValueError as e:
        percentual = 0
    """

    csv_file.writerow([
        cod_municipios[i]['municipio']['id'],
        cod_municipios[i]['municipio']['nome'],
        total_doses,
        doses_aplicadas,
        percentual
    ])

file.close()
