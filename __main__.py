import folium
import geopandas as gpd
import branca.colormap as cm
import pandas as pd

# url = (
#     "https://docs.google.com/spreadsheets/d/1tttGLST1VR5duGWbvcQ2EyrllpAINXGe5W3fYEaZj0E/gviz/tq?tqx=out:csv&sheet=tratamento_dados"
# )
# malha = open('malha-dos-municipios-pi.json', 'r')
# geo_data = json.loads(malha.read())
#state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
# csv_municipios = open('vacinados.csv', 'r')
# dtypes = {'municipio': 'str', 'porcentagem': 'float'}
# data = pd.read_csv(csv_municipios, dtype=dtypes)

# m = folium.Map(location=[-6.8125424, -45.4353583], zoom_start=6.75)
#colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 50e3)

dtypes = {'codarea': 'str'}
municipios = pd.read_csv('p_vacinados.csv', dtype=dtypes)
population = pd.read_csv('vacinados.csv', dtype=dtypes)

data = pd.merge(municipios, population)
nil = gpd.read_file('malha-dos-municipios-pi.json')
print(nil.head())

#population = pd.read_csv('vacinados.csv', dtype=dtypes)

nilpop = nil.merge(data, on='codarea')
# print(nilpop.head())


x_map = nil.centroid.x.mean()
y_map = nil.centroid.y.mean()

m = folium.Map(
    location=[y_map, x_map],
    zoom_start=6.80, tiles=None
)
folium.TileLayer('CartoDB positron', name="Light Map", control=False).add_to(m)


def style_function(x): return {
    'fillColor': '#ffffff', 'color': '#000000', 'fillOpacity': 0.1, 'weight': 0.1}


def highlight_function(x): return {
    'fillColor': '#000000', 'color': '#000000', 'fillOpacity': 0.50, 'weight': 0.1}


folium.Choropleth(
    geo_data=nilpop,
    name="choropleth",
    data=nilpop,
    columns=['codarea', 'porcentagem'],
    key_on="feature.properties.codarea",
    fill_color="GnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Taxa de Vacinação (%)",
).add_to(m)

NIL = folium.features.GeoJson(
    nilpop,
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['municipio', 'total_doses', 'porcentagem'],
        aliases=['Município: ', 'Total de Doses', 'Vacinados em %: '],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
    )
)

m.add_child(NIL)
m.keep_in_front(NIL)
folium.LayerControl().add_to(m)

m.save('index.html')
