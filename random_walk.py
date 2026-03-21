from random import choice

class RandomWalk():
    """Random Walk Generation Class"""

    def __init__(self, num_points=5000):
        """Initializes the wandering attributes"""
        self.num_points = num_points

        self.x_values = [0]  # All walks start from the point (0, 0).
        self.y_values = [0]  # Two lists for storing data.

    def fill_walk(self):
        """Calculates all wandering points"""

       # Steps are generated until the desired length is reached.
        while len(self.x_values) < self.num_points:

            # Determining the direction and length of movement.
            x_direction = choice([1, -1])
            x_distance =  choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Zero displacement deviation.
            if x_step == 0 and y_step == 0:
                continue

            # Calculating the next X and Y values.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)