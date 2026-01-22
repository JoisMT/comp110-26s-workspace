"""Planning a tea party"""

__author__: str = "730802154"


def main_planner(guests: int) -> None:
    """Entrypoint of teaparty"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Number of guests attending"""
    return 2 * people


def treats(people: int) -> int:
    """Treats for my guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
