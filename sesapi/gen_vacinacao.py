import pandas as pd
import geopandas as gpd
import json
#import branca.colormap as cm

nil = gpd.read_file('malha-dos-municipios-pi.json')
print(nil.head())

dtypes = {'codarea': 'str', 'porcentagem': 'float'}
population = pd.read_csv('vacinados.csv', dtype=dtypes)
print(population.head(5))

municipios = open('id-municipios-pi.json', 'r')

#print(map(lambda x: print(x.nome), municipios))
nilpop = nil.merge(population, on='codarea')
print(nilpop.head())
