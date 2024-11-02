from find_max import find_and_remove_max


def test_find_and_remove_max_value() -> None:
    input_list = [5, 3, 5, 1, 5]
    expected_value = 5
    assert (
        find_and_remove_max(input_list) == expected_value
    ), "Expected to return the max value 5"


def test_find_and_remove_max_mutation() -> None:
    input_list = [6, 2, 6, 4, 6]
    find_and_remove_max(input_list)
    expected_list = [2, 4]
    assert (
        input_list == expected_list
    ), "Expected the input list to have all instances of 6 removed"


def test_find_and_remove_max_empty_list() -> None:
    input_list: list[int] = []
    assert find_and_remove_max(input_list) == -1, "Expected -1 for an empty list"
    assert input_list == [], "Expected the input list to remain unchanged"
