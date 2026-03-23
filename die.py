from random import randint

class Die():
    """One Die."""

    def __init__(self, num_sides=6):
        """The default is a 6-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Returns a random number between 1 and the number of sides."""
        return randint(1, self.num_sides)
