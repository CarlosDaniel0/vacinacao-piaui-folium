import csv
import json
import pandas as pd
# conteudo[i].municipio.id
# features.properties.codearea
malha = open('malha-dos-municipios-pi.json')
municipios = open('id-municipios-pi.json')
vacinados = open('vacinados.csv', 'rb')

# 1 - Cria o arquivo
f = open('p_vacinados.csv', 'w', newline='', encoding='utf-8')

# 2. cria o objeto de gravação
w = csv.writer(f)

data_municipios = json.loads(municipios.read())
data_vacinados = pd.read_csv('vacinados.csv', delim_whitespace=True)
w.writerow(['codarea', 'municipio'])
# 3. grava as linhas
for i in range(len(data_municipios)-1):
    w.writerow([data_municipios[i]['municipio']['id'],
                data_municipios[i]['municipio']['nome']])

malha.close()
municipios.close()
f.close()
