"""File to run river simulation."""

from exercises.ex07.river import River

my_river: River = River(10, 2)
my_river.one_river_week()


print(my_river)
