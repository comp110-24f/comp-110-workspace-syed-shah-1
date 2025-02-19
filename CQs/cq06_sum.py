"""Summing the elements of a list using different loops"""

__author__: str = "730770696"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0

    while idx < len(vals):
        sum += vals[idx]
        idx += 1

    return sum


def f_sum(vals: list[float]) -> float:

    sum: float = 0

    for val in vals:
        sum += val

    return sum


def f_range_sum(vals: list[float]) -> float:

    sum: float = 0
    idx: int

    for idx in range(len(vals)):
        sum += vals[idx]

    return sum
