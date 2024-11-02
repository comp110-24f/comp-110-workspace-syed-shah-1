"""A Wordle game where the player guesses a secret word and receives feedback through emoji codification."""

__author__: str = "730770696"


def input_guess(secret_word_len: int) -> str:
    # Prompt the player to input a guess and enforce that it matches the secret word's length.
    guess: str = input(f"Enter a {secret_word_len} character word: ")

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Returns True if the character is found in the word, otherwise False."""
    # Assert that only a single character is checked at a time.
    assert len(char_guess) == 1

    i: int = 0
    # Loop through each character of the secret word to check for a match.
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emoji feedback for a guess compared to the secret word."""
    # Ensure both guess and secret are the same length.
    assert len(guess) == len(secret)

    output = ""

    # Set up emoji representations:
    WHITE_BOX: str = "\U00002B1C"  # Incorrect letter.
    GREEN_BOX: str = "\U0001F7E9"  # Correct letter in the correct position.
    YELLOW_BOX: str = "\U0001F7E8"  # Correct letter but in the wrong position.

    idx: int = 0
    # Loop through each character in the guess and compare it to the secret word.
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            output += GREEN_BOX  # Right letter in the right position.
        elif contains_char(secret, guess[idx]):
            output += YELLOW_BOX  # Right letter in the wrong position.
        else:
            output += WHITE_BOX  # Wrong letter.
        idx += 1

    return output


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    # Allow the player to take up to 6 turns to guess the secret word.
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        print(emojified(guess=guess, secret=secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1

    # If the player didn't guess correctly after 6 turns, end the game.
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    # Run the game with the secret word "codes".
    main(secret="codes")
