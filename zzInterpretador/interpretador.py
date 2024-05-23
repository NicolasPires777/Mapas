import json
import matplotlib.pyplot as plt #cria a visualizaçõa
from shapely.geometry import shape, Polygon, MultiPolygon #manipular formas geometricas
from matplotlib.patches import Polygon as MplPolygon #desenhar forma geometrica

#carrega esse demonio desse mapa pqp vou surtar
def load_geojson(filepath):
    with open(filepath, 'r') as mapadesgraçado:
        data = json.load(mapadesgraçado)
    return data

# Função para desenhar o mapa
def draw_map(data):
    fig, ax = plt.subplots(figsize=(15, 15)) #quadrados e figuras e janelas e alegria

    minx, miny, maxx, maxy = float('inf'), float('inf'), float('-inf'), float('-inf') #tamanho do quadrado que fica o mapa, depois de 3 horas descobri que com inf ajusta automatico

    for feature in data['features']:
        geom = shape(feature['geometry'])
        if geom.geom_type == 'Polygon':
            patch = MplPolygon(list(geom.exterior.coords), closed=True, edgecolor='black', facecolor='none') #essa função desenha e list interpreta 
            ax.add_patch(patch)
            bounds = geom.bounds 
        elif geom.geom_type == 'MultiPolygon': #acho que não tem nenhum multi poligono mas deixa ai fé
            for poly in geom:
                patch = MplPolygon(list(poly.exterior.coords), closed=True, edgecolor='black', facecolor='none')
                ax.add_patch(patch)
                bounds = poly.bounds
        minx, miny = min(minx, bounds[0]), min(miny, bounds[1])
        maxx, maxy = max(maxx, bounds[2]), max(maxy, bounds[3])

    ax.set_aspect('equal')
    ax.set_title('Cidades do Paraná')
    
    plt.xlim(minx - 0.5, maxx + 0.5)
    plt.ylim(miny - 0.5, maxy + 0.5)
    
    plt.show()

# Caminho do arquivo GeoJSON
filename = '/home/nicolas/Documents/Mapa/Parana.geojson'

# Carregar e desenhar o mapa
data = load_geojson(filename)
draw_map(data)
