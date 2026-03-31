# Visualization of fire data provided by NASA.
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Studying data structure.
filename = 'data/fire_nrt_M-C61_727880.json'
# Added encoding for reading files.
with open (filename, encoding='utf-8') as f:
    all_fires_data = json.load(f)

# Count the number of fires from a file.
all_fires_dicts = all_fires_data
print(len(all_fires_dicts))
# Extracting the title for automatic display.
file_title = "Active fires MODIS"

def get_data(fire_dict):
    """Извлечение данных"""
    intensity = fire_dict.get('frp', 0)
    if intensity is None:
        intensity = 0
    lon = fire_dict.get('longitude', 0)
    lat = fire_dict.get('latitude', 0)
    title = (f"Date: {fire_dict.get('acq_date')}<br>"
             f"Time: {fire_dict.get('acq_time')}<br>")
    return intensity, lon, lat, title

# Adding data to the lists: fire intensity, location data, hints.
intensities, lons, lats, hover_texts = [], [], [], []
for fire_dict in all_fires_dicts:
    intensity, lon, lat, title = get_data(fire_dict)
    intensities.append(intensity)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Plotting data on a map.
data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [max(3, min(25, frp*0.5)) for frp in intensities],
        # Setting up a marker.
            'color': intensities,
            'colorscale': 'YlOrRd',
            'reversescale': False,
            'cmin': 0,
            'line': {'width': 1, 'color': 'grey'},
            'colorbar': {
                'title': 'Fire Radiative Power (MW)',    
                'thickness': 15,
                'len': 0.8,
                }
        }
}]
my_layout = Layout(
    title={
        'text': file_title,
        'x': 0.5,
        'font': {'size': 30, 'family': 'Arial'},
        },
    geo={
        'projection': {'type': 'natural earth'},
        'showland': True,
        'landcolor': 'rgb(230, 230, 230)',
        'countrycolor': 'rgb(180, 180, 180)',
        'showcountries': True,
        'showocean': True,
        'oceancolor': 'rgb(210, 230, 250)',
        'showlakes': True,
        'lakecolor': 'rgb(210, 230, 250)',
        #'projection_scale': 1.2,
        # Map background color.
        'bgcolor': 'rgb(240, 240, 240)'
        }
)        

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
