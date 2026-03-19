import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap='plasma', s=10)

# Assigning a chart title and axes.
ax.set_title("Cubes Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True, alpha=0.3)

plt.show()