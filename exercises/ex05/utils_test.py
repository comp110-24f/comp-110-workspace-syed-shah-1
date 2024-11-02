"""unit tests for list utility functions."""

__author__ = "730770696"

import pytest
from utils import only_evens, sub, add_at_index


# tests for only_evens
def test_only_evens_edge_case_empty_list() -> None:
    """tests only_evens with an empty list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_only_evens_use_case_all_odds() -> None:
    """tests only_evens when input contains all odd numbers."""
    a: list[int] = [1, 3, 5]
    assert only_evens(a) == []


def test_only_evens_use_case_mixed_numbers() -> None:
    """tests only_evens with a list containing both even and odd numbers."""
    a: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(a) == [2, 4]


# tests for sub
def test_sub_edge_case_empty_list() -> None:
    """tests sub with an empty list."""
    a: list[int] = []
    assert sub(a, 0, 3) == []


def test_sub_use_case_valid_range() -> None:
    """tests sub with a valid range."""
    a: list[int] = [10, 20, 30, 40, 50]
    assert sub(a, 1, 3) == [20, 30]


def test_sub_use_case_negative_start() -> None:
    """tests sub with a negative start index."""
    a: list[int] = [10, 20, 30, 40, 50]
    assert sub(a, -2, 3) == [10, 20, 30]


# tests for add_at_index
def test_add_at_index_raises_indexerror() -> None:
    """test that add_at_index raises an IndexError for an invalid index."""
    a: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(a, 4, 5)


def test_add_at_index_use_case_mutation() -> None:
    """tests add_at_index by checking if the list is mutated correctly."""
    a: list[int] = [1, 2, 3]
    add_at_index(a, 4, 1)
    assert a == [1, 4, 2, 3]


def test_add_at_index_use_case_append() -> None:
    """tests add_at_index by adding an element at the end of the list."""
    a: list[int] = [10, 20, 30]
    add_at_index(a, 40, 3)
    assert a == [10, 20, 30, 40]
