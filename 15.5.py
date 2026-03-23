# Refactoring training.
from random import choice

class RandomWalk():
    """Class for generating random walks"""

    def __init__(self, num_points=5000):
        """Initializes the wandering attributes"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Generate and return one step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Calculates all walking points"""

       # Steps are generated until the desired length is reached.
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # Zero displacement deviation.
            if x_step == 0 and y_step == 0:
                continue

            # Calculating the next values of x and y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)