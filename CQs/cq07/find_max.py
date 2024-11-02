__author__: str = "730770696"


def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1

    maximum: int = max(a)

    while maximum in a:
        a.pop(a.index(maximum))

    return maximum


print(find_and_remove_max([10, 9, 8, 7, 10]))
