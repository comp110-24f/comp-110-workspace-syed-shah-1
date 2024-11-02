"""using a while loop to iterate over a string"""

__author__: str = "730770696"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    index = 0
    while index < len(phrase) - 1:
        if search_char == phrase[index]:
            count += 1
        index += 1
    return count
