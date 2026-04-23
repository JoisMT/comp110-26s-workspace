"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730802154"


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove old animals from river"""

        surviving_fish: list[Fish] = []
        for f in self.fish:
            if f.age <= 3:
                surviving_fish.append(f)
        self.fish = surviving_fish

        surviving_bears: list[Bear] = []
        for b in self.bears:
            if b.age <= 5:
                surviving_bears.append(b)
        self.bears = surviving_bears

        return None

    def bears_eating(self):
        """Each bear eats 3 fish if there are at least 5 available."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Remove bears that have a hunger score below 0."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Each pair of fish produces 4 offspring"""
        new_fish: int = (len(self.fish) // 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Each pair of bears produces 1 offspring"""
        num_new_bears: int = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())
        return None

    def __str__(self) -> str:
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, other_riv: River) -> River:
        """Combine two rivers into a new one"""
        total_fish: int = len(self.fish) + len(other_riv.fish)
        total_bears: int = len(self.bears) + len(other_riv.bears)

        return River(total_fish, total_bears)

        return self

    def __mul__(self, factor: int) -> River:
        """Scale a river by a factor to create a new one"""
        new_fish_count: int = len(self.fish) * factor
        new_bear_count: int = len(self.bears) * factor

        return River(new_fish_count, new_bear_count)

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """Simulate a week in the river"""
        for _ in range(7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Remove fish from front of list"""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        return None
