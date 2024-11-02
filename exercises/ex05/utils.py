"""building list utility functions in Python."""

__author__ = "730770696"


def only_evens(a: list[int]) -> list[int]:
    b: list[int] = []

    # iterate over the list and add only even numbers
    for i in a:
        if i % 2 == 0:
            b.append(i)

    return b


def sub(a: list[int], start: int, end: int) -> list[int]:
    # handle the empty list case and invalid start/end values
    if len(a) == 0 or start >= len(a) or end <= 0:
        return []

    # if start is negative begin from index 0
    if start < 0:
        start = 0

    # if end is greater than the length of the list set it to the length of the list
    if end > len(a):
        end = len(a)

    # create the sublist
    b: list[int] = []
    for i in range(start, end):
        b.append(a[i])

    return b


def add_at_index(a: list[int], element: int, index: int) -> None:
    # check if index is out of range
    if index < 0 or index > len(a):
        raise IndexError("Index is out of bounds for the input list")

    # append a element to extend the list
    a.append(0)

    # shift elements to the right
    for i in range(len(a) - 1, index, -1):
        a[i] = a[i - 1]

    # insert the new element
    a[index] = element
