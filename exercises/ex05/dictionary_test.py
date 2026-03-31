"""Unit tests for dictionary utility functions"""

__author__ = "730802154"

from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


import pytest

""" Invert"""


def test_invert_single_pair() -> None:
    """Use case: dictionary with one key-value pair."""
    assert invert({"a": "b"}) == {"b": "a"}


def test_invert_multiple_pairs() -> None:
    """Use case: dictionary with multiple pairs."""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_empty_dict() -> None:
    """Edge case: empty dictionary."""
    assert invert({}) == {}


def test_invert_raises_keyerror() -> None:
    """Edge case: duplicate values should raise KeyError."""
    with pytest.raises(KeyError):
        invert({"a": "b", "c": "b"})


def test_favorite_color_normal() -> None:
    """Use case: most common color appears multiple times."""
    assert favorite_color({"Alice": "blue", "Bob": "red", "Charlie": "blue"}) == "blue"


def test_favorite_color_single_entry() -> None:
    """Use case: only one person."""
    assert favorite_color({"Alice": "green"}) == "green"


def test_favorite_color_tie() -> None:
    """Edge case: tie returns first color."""
    assert favorite_color({"Alice": "blue", "Bob": "red"}) == "blue"


def test_count_multiple_items() -> None:
    """Use case: list with repeated items."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_all_same() -> None:
    """Use case: all elements are the same."""
    assert count(["x", "x", "x"]) == {"x": 3}


def test_count_empty_list() -> None:
    """Edge case: empty list."""
    assert count([]) == {}


""" alphabetizer"""


def test_alphabetizer_basic() -> None:
    """Use case: normal list of lwoercase words."""
    assert alphabetizer(["apple", "banana", "apricot"]) == {
        "a": ["apple", "apricot"],
        "b": ["banana"],
    }


def test_alphabetizer_mixed_case() -> None:
    """Use case: words with uppercase letters."""
    assert alphabetizer(["apple", "banana"]) == {
        "a": ["apple"],
        "b": ["banana"],
    }


def test_alphabetizer_non_alpha() -> None:
    """Edge case: words starting with non-letters are ignored."""
    assert alphabetizer(["123", "!test", "apple"]) == {"a": ["apple"]}


def test_update_attendance_existing_day() -> None:
    """Use case: add student to existing day."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Bob")
    assert attendance == {"Monday": ["Alice", "Bob"]}


def test_update_attendance_new_day() -> None:
    """Use case: add student to new day."""
    attendance = {}
    update_attendance(attendance, "Tuesday", "Alice")
    assert attendance == {"Tuesday": ["Alice"]}


def test_update_attendance_multiple_updates() -> None:
    """Edge case: multiple updates to same day."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Bob")
    update_attendance(attendance, "Monday", "Charlie")
    assert attendance == {"Monday": ["Alice", "Bob", "Charlie"]}
