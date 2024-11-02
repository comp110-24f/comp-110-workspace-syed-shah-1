"""a program to help you plan a cozy tea party. The program will ultimately ask the user for the number of guests and it will calculate the quantity of tea bags needed, the number of treats to accompany the tea, and the expected cost of the party.

"""

__author__: str = "730770696"


def main_planner(guests: int) -> None:
    """function that calls every other function and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")

    # Calculate and display the number of tea bags required
    print("Tea Bags: " + str(tea_bags(people=guests)))

    # Calculate and display the number of treats required
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """A function to compute the number of tea bags needed based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """A function to calculate number of treats based on number of teas guests drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """A function to compute the cost of the tea bags and the treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    """Prompt the user for the number of guests and start the main planner"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
