# Ability to work with data for 1 day, week, month. Refactoring, automatic header.
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Studying data structure.
filename = 'data/eq_1_day_m1.json'
# Added encoding for reading files.
with open (filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

# Calculate the number of earthquakes from a file.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
# Extracting the title for automatic display.
file_title = all_eq_data['metadata']['title']

def get_data(eq_dict):
    """Extracting magnitude, location data, hints"""
    mag = eq_dict['properties']['mag']
    if mag is None:
        mag = 0
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    # Returning a tuple.
    return mag, lon, lat, title

# Adding data to the lists: magnitude, location data, hints.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag, lon, lat, title = get_data(eq_dict)
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Plotting data on a map.
#data = [Scattergeo(lon=lons, lat=lats)]
data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            # max(1, -) to remove the negative magnitude error.
            # Adjusting the marker size.
            'size': [max(1, 3*mag) for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitide'}
        }
}]
my_layout = Layout(title=file_title, title_x=0.5)  # Align the title to the middle.

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
