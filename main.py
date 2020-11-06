import folium
import pandas

data = pandas.read_csv('Volcanoes.csv')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def colors(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="VMap")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(
        folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m", parse_html=True, fill_color=colors(el),
                            color='grey', fill_opacity=0.7))

fg = folium.FeatureGroup(name="Population")
fg.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map1.html")
