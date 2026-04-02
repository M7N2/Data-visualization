# The most active topics on Hacker News.
from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Making an API call and saving the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Processing information about each article.
submission_ids = r.json()
submission_dicts, comments, titles, labels, links = [], [], [], [], []

for submission_id in submission_ids[:30]:
	# Creating a separate API call for each article.
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	#print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()
	submission_dicts.append(response_dict)

# Sorted by number of comments. Protection against missing keys.
submission_dicts.sort(key=lambda x: x.get('descendants', 0), reverse=True)

for submission_dict in submission_dicts:
    title = submission_dict['title']
    comment_count = submission_dict.get('descendants', 0)
    # Уshorten names on x-axis.
    if len(title) > 35:
    	short_title = title[:35] + "..."
    else:
    	short_title = title

    # Link to the page.
    article_id = submission_dict['id']
    article_link = f"https://news.ycombinator.com/item?id={article_id}"
    clickable_title = f"<a href='{article_link}'>{short_title}</a>"
 
    # Hint: Author and number of points.
    author = submission_dict['by']
    score = submission_dict['score']
    label = f"Author: {author}<br />Score: {score}<br />Comments: {comment_count}"

    titles.append(clickable_title)
    comments.append(comment_count)
    labels.append(label)

# Visualization.
data = [{
    'type': 'bar',
    'x': titles,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': comments,
        'colorscale': 'Cividis',
        'reversescale': True,
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
	'title': {
	    'text': "Top Hacker News Stories by Comments",
	    'x': 0.5,
	    'font': {'size': 27},
	},
	'xaxis': {
	    'title': {
	        'text': "Story Title",
	        'font': {'size': 24},
	    },
	    'tickfont': {'size': 14},
	},
	'yaxis': {
	    'title': {
	        'text': "Number of Comments",
	        'font': {'size': 24},
	    },
	    'tickfont': {'size': 14},
	},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news.html')
