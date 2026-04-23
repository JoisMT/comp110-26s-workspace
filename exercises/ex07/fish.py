"""File to define Fish class."""


class Fish:
    """Changes in age."""

    age: int

    def __init__(self):

        self.age = 0
        return None

    def one_day(self):
        """Increase age"""
        self.age += 1
        return None
