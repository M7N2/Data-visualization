# Visualization of volcanic activity in the United States. Data is loaded via API.
import requests
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

url = 'https://volcanoes.usgs.gov/vsc/api/volcanoApi/vhpstatus'
r = requests.get(url)
print(f"Status code: {r.status_code}")

data = r.json()

# Loading data from a saved file for debugging.
#with open('data/readable_volcano_data.json', 'r', encoding='utf-8') as f:
#    data = json.load(f)

# Data storage lists.
names, lats, lons, alert_level, hover_texts = [], [], [], [], []

# Colors by danger level.
color_map = {
    'UNASSIGNED': 'gray',
    'NORMAL': 'green',
    'ADVISORY': 'yellow',
    'WATCH': 'orange',
    'WARNING': 'red',
}
# Hazard marker sizes.
size_map = {
    'UNASSIGNED': 5,
    'NORMAL': 8,
    'ADVISORY': 12,
    'WATCH': 16,
    'WARNING': 20,
}

for volcano in data:
    # Checking for coordinate data availability.
    if volcano.get('lat') and volcano.get('long'):
        names.append(volcano['vName'])
        lats.append(volcano['lat'])
        lons.append(volcano['long'])
        alert_level.append(volcano['alertLevel'])
    
        # Creating a hint.
        name = volcano.get('vName')
        color_code = volcano.get('colorCode')
        region = volcano.get('region')
        threat = volcano.get('nvewsThreat')
        alert_date = volcano.get('alertDate')
        level = volcano.get('alertLevel')

        hover_text = (f"<b>{name}</b><br />"
                      f"Alert level: {level}<br />"
                      f"Color code: {color_code}<br />"
                      f"Region: {region}<br />"
                      f"Threat: {threat}")
        hover_texts.append(hover_text)

# Colors for markers.
colors = [color_map.get(level, 'gray') for level in alert_level]
# Sizes for markers.
sizes = [size_map.get(level, 5) for level in alert_level]

# Data visualization.
data_geo = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': names,
        'hovertext': hover_texts,
        'marker': {
            'size': sizes,
            'color': colors,
            'line': {'width': 1, 'color': 'grey'},
            }
}]
my_layout = Layout(
    title={
        'text': "US Volcanoes Activity Status",
        'x': 0.5,
        'font': {'size': 30, 'family': 'Arial'},
        },
    geo={
        'scope': 'usa', 
        'projection': {'type': 'albers usa'},
        'showland': True,
        'landcolor': 'rgb(230, 230, 230)',
        'countrycolor': 'rgb(180, 180, 180)',
        'showlakes': True,
        'lakecolor': 'rgb(210, 230, 250)',
        'showocean': True,
        'oceancolor': 'rgb(31, 97, 141)',
        'showrivers': True,
        'rivercolor': 'rgb(133, 193, 233)',
        'showcountries': True,
        'countrycolor': 'rgb(127, 140, 141)',
        'showsubunits': True,
        'subunitcolor': 'rgb(189, 195, 199)',
        'bgcolor': 'rgb(240, 240, 240)',
        }
)        

fig = {'data': data_geo, 'layout': my_layout}
offline.plot(fig, filename='active_volcanoes_map.html')
