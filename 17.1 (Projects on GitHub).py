# Most-Starred Java Projects on GitHub.
# Visualization using API, Bar chart.
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Making an API call and saving the response.
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Saving an API response to a variable.
response_dict = r.json()
repo_dicts = response_dict['items']

# Adding lists of names, ratings, hints.
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    # Adding active links to a diagram.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    # Adding advanced hints.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Building a visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,  # Hints.
    # Column color, line, transparency.
    'marker': {
        #'color': 'rgb(60, 100, 150)',
        'color': stars,
        'colorscale': 'Bluered',
        'reversescale': True,
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': {
        'text': "Most-Starred Java Projects on GitHub",
        'x': 0.5,  # Centered title.
        'font': {'size': 28},
    },
    'xaxis': {
        'title': {
            'text': 'Repository',
            'font': {'size': 24},
        },    
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': {
            'text': 'Stars',
            'font': {'size': 24},
        },    
        'tickfont': {'size': 14},  # Font on the coordinate axis.
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='java_repos.html')
