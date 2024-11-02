"""Mutating functions"""

__author__: str = "730770696"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a: list[int], num: int) -> None:
    a.append(num)
    return None


def double(a: list[int]) -> None:
    idx: int = 0
    while idx < len(a):
        a[idx] = 2 * a[idx]
        idx += 1


double(list_2)
print(list_1)
print(list_2)
