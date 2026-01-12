"""My first exercise in COMP110!"""

__author__ = "730802154"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("what is your name?")))
