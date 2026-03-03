"Utility functions for lists"

__author__ = "730802154"


def all(values: list[int], number: int) -> bool:
    """Retrun True if all elements in values are equal to number, False if diff"""

    if len(values) == 0:
        return False

    for value in values:
        if value != number:
            return False

    return True


def max(input: list[int]) -> int:
    """Return the largest int in input. Raises ValueErros if input is empty"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")

    largest = input[0]

    for value in input:
        if value > largest:
            largest = value

    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if list1 and list2 are equal if not Return False"""

    if len(list1) != len(list2):
        return False

    copy_list2 = []
    for item in list2:
        copy_list2.append(item)

    for item in list1:
        if item != copy_list2.pop(0):
            return False

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate list1 by appending all elements of list2 to it"""

    for item in list2:
        list1.append(item)
