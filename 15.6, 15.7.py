from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Creating dice
die_1 = Die() # You can change the number of sides in the argument.
die_2 = Die()
die_3 = Die()

# Simulating a series of throws with saving the results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analysis of results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)  # Method for counting elements.
    frequencies.append(frequency)

# Visualization of results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': "Frequency of Result"}
my_layout = Layout(title=f"Results of rolling three D{die_1.num_sides}, "
                   f"D{die_2.num_sides} and D{die_3.num_sides} 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
