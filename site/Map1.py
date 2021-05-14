import folium
import pandas

data=pandas.read_csv("Pop Table.csv")
lat=list(data["lat"])
lng=list(data["lng"])
pop=list(data["pop"])

def color_producer(population):
    if population<100000:
        return 'green'
    elif 100000<= population < 1000000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[24.10, 88.26], zoom_start=10, tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Population")

for lt, ln, pop in zip(lat,lng,pop):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(pop)+" people", icon=folium.Icon(color=color_producer(pop))))
fgp=folium.FeatureGroup(name="Covid")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'orange' if 500000 <= x['properties']['POP2005'] < 1500000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
