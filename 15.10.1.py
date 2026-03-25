from plotly.graph_objs import Scatter, Layout
from plotly import offline
from random_walk import RandomWalk


# Creating a random walk.
rw = RandomWalk()
rw.fill_walk()

# Visualization.
# Setting up points.
trace = Scatter(x=rw.x_values, y=rw.y_values, mode='markers',
                marker=dict(size=3, color='blue', symbol='circle',
                opacity=0.6))
# Design settings.
my_layout = Layout(title=f"Random walk {rw.num_points} steps",
                   xaxis=dict(title="x-coordinate"),
                   yaxis=dict(title="y-coordinate",
                   scaleanchor='x', scaleratio=1))
# Creating a graph.
data = [trace]

offline.plot({'data': data, 'layout': my_layout},
             filename='random_walk_plotly.html')
