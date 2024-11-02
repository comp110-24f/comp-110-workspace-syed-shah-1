"""Recreating utility functions in Python."""

__author__ = "730770696"


def all(integers: list[int], integer: int) -> bool:

    if len(integers) == 0:
        return False

    idx: int = 0
    # iterate through the list and compare each element with the target integer
    while idx < len(integers):
        # if one element is not equal to the target, return False
        if integers[idx] != integer:
            return False
        idx += 1
    # if the loop completes, all elements are equal to the target
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    idx = 0
    max_val = input[0]  # store the first element as the initial maximum

    # iterate through the list to find the maximum value
    while idx < len(input):
        # update max_val if a larger element is found
        if input[idx] > max_val:
            max_val = input[idx]
        idx += 1

    return max_val


def is_equal(list1: list[int], list2: list[int]) -> bool:

    # check if the lengths of the lists are the same
    if len(list1) != len(list2):
        return False

    # compare elements at each index
    for idx in range(len(list1)):
        # return False if any element doesn't match
        if list1[idx] != list2[idx]:
            return False

    # if all elements are equal, return True
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    # iterate through each element in list2 and append it to list1
    for element in list2:
        list1.append(element)
