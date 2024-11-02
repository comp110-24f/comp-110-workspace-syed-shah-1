"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730770696"


def input_word() -> str:
    # prompt user for a 5-character word
    word: str = input("Enter a 5-character word: ")
    # check if the entered word has exactly 5 characters
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exit the program if the condition is not met
    return word  # return the valid word


def input_letter() -> str:
    # prompt user for a single character
    letter: str = input("Enter a single character: ")
    # check if the entered character is a single character
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # exit the program if the condition is not met
    return letter  # return the valid letter


def contains_char(word: str, letter: str) -> None:
    # announce that we are searching for the letter in the word
    print("Searching for " + letter + " in " + word)
    count: int = 0  # initialize count of occurrences to zero
    # check each character in the word for a match with the letter
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1  # increment count if found
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1  # increment count if found
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1  # increment count if found
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1  # increment count if found
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1  # increment count if found

    # print the total number of occurrences found
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    # run the main program flow
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()  # execute the main function if this script is run directly
