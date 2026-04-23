from __future__ import annotations

"""Linked list functioms"""

__author__ = "730802154"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize the Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce string representation of life."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)


def value_at(head: Node | None, index: int) -> int:
    """Find the value at a specific index in a linked list using recursion."""
    # Base case 1: list is empty or index is out of bounds
    if head is None:
        raise IndexError("Index is out of bonds on the list.")

    # Base case 2: Found the target index
    if index == 0:
        return head.value

    # Recursive case: Move to the next node and decrement index
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Find the maximum value in a linked list recursively."""

    # Base case 1: intial list is empty
    if head is None:
        raise ValueError("Cannot call max with None.")

    # Base case 2: only one node left in list
    if head.next is None:
        return head.value

    # recursive step: find max of rest of the list
    sub_max: int = max(head.next)

    # Return the larger of the current value and sublist max
    if head.value > sub_max:
        return head.value

    return sub_max


def linkify(items: list[int]) -> Node | None:
    """Turn a Python list into a linked list of Nodes recursively."""
    # Base case: list is empty
    if len(items) == 0:
        return None

    # Recursive step:
    # 1 - take the first item
    # 2 - link it to the result of linking the rest
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Create a new linked list where every value is multiplied by factor."""
    # Base case: end of original list
    if head is None:
        return None
    # Recursive step:
    # 1- create a new Node with scaled value
    # 2- link it to the result of scaling the rest of the list
    return Node(head.value * factor, scale(head.next, factor))
