import matplotlib.pyplot as plt
from die import Die

# Creating Dice.
die_1 = Die()
die_2 = Die()

# Simulating a series of throws with saving the results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analysis of resultss.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of results.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)

x_values = list(range(2, max_result + 1))

# Creating a diagram.
ax.bar(x_values, frequencies,
       color='skyblue',
       edgecolor='darkblue',
       linewidth=1.5,
       alpha=0.8)

# Write above each column the number of times the combination has appeared..
for i, v in enumerate(frequencies):
    ax.text(x_values[i], v + 2, str(v), ha='center', fontsize=8)

# Settings.
ax.set_title(f"Results of rolling two D{die_1.num_sides} and"
             f" D{die_2.num_sides} 1000 times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

# Setting axis labels.
ax.set_xticks(x_values)
ax.tick_params(axis='both', labelsize=10)

plt.show()
