"""File to define Bear class."""


class Bear:
    """Changes in age and hunger"""

    age: int
    hunger_score: int

    def __init__(self):

        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase age and decrease hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase hunger score by number of fish eaten"""
        self.hunger_score += num_fish
        return None
