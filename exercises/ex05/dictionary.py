"""Dictionary Utility Functions"""

__author__ = "730802154"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    """Inverting letters"""
    for key in input_dict:
        value: str = input_dict[key]

        if value in result:
            raise KeyError("Duplicate key when inverting")

        result[value] = key

    return result


def favorite_color(colors: dict[str, str]) -> str:
    count: dict[str, int] = {}
    """Matching name with color"""
    for name in colors:
        color: str = colors[name]

        if color in count:
            count[color] = count[color] + 1
        else:
            count[color] = 1

    most_color: str = ""
    most_count: int = 0

    for name in colors:
        color: str = colors[name]

        if count[color] > most_count:
            most_count = count[color]
            most_color = color

    return most_color


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    """Count number of times value appear"""
    for item in values:
        if item in result:
            result[item] = result[item] + 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    """Match word with letter"""
    for word in words:
        first_letter: str = word[0].lower()

        if first_letter.isalpha():
            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
