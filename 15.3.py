import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Molecular motion in the form of lines rather than dots.
while True:
    # Construction of a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plotting points on a diagram.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    # Генерация чисел равных количеству точек.
    ax.plot(rw.x_values, rw.y_values, linewidth=5)

    # Selecting the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    	       s=100)

    # Removing axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break