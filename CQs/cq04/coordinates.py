"""Defines function to print all possible character pairings from two strings."""

__author__: str = "730770696"


def get_coords(xs: str, ys: str) -> None:
    """Prints all possible pairs of characters from two input strings."""
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            print(f"({xs[i]},{ys[j]})")
            j += 1
        i += 1
