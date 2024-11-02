"""Creating dictionary utility functions"""

__author__: str = "730770696"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    # creates a new dictionary with keys and values swapped
    inverted_dict: dict[str, str] = {}
    for key, value in input_dict.items():
        # checks if the value already exists as a key to avoid duplicates
        if value in inverted_dict:
            raise KeyError("duplicate key after inversion.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    # returns an empty string if the input dictionary is empty
    if not color_dict:
        return ""

    # counts the occurrences of each color in the dictionary
    color_count: dict[str, int] = {}
    for color in color_dict.values():
        color_count[color] = color_count.get(color, 0) + 1
    # finds the most frequent color, resolving ties by first appearance
    max_color = max(
        color_count, key=lambda k: (color_count[k], -list(color_dict.values()).index(k))
    )
    return max_color


def count(items: list[str]) -> dict[str, int]:
    # counts occurrences of each item in the list
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    # organizes words into lists by their starting letter
    alpha_dict: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        # adds the word under its starting letter if not already there
        if first_letter not in alpha_dict:
            alpha_dict[first_letter] = []
        alpha_dict[first_letter].append(word)
    return alpha_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    # adds the student to the attendance list for the specified day
    if day not in attendance:
        attendance[day] = []
    if student not in attendance[day]:
        attendance[day].append(student)
