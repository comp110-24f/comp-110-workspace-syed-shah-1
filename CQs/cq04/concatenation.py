"""Contains function for concatenating two strings."""

__author__: str = "730770696"


def concat(string1: str, string2: str) -> str:
    return string1 + string2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
