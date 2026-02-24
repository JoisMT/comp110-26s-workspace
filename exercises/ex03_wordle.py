"Wordle Exercise"

__author__ = "730802154"


def input_guess(secret_word_len: int) -> str:
    """Prompts user until they guess the correct length."""
    # prompt them to guess a word
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    # if the length is incorrect this prompt asks them to try again
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the character guess is in the secret word."""
    #
    assert len(char_guess) == 1
    idx: int = 0
    # loop for each character
    while idx < len(secret_word):
        # if theres a match return True
        if secret_word[idx] == char_guess:
            return True
        # move to next index
        idx += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Emoji boxes based off the user guess and the secret word."""
    # this makes sure that the guess and secret word are the same length first
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"

    result: str = ""
    idx: int = 0

    # loop for each character
    while idx < len(secret):
        # case 1 correct letter and position
        if guess[idx] == secret[idx]:
            result += GREEN_BOX

        # case 2 letter is right but wrong position
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX

        # case 3 no right letters
        else:
            result += WHITE_BOX

        idx += 1

    return result


def main(secret: str) -> None:
    """Entry of the program and main game loop."""

    max_turns: int = 6
    turn: int = 1
    won: bool = False

    # Game keeps going until they finish their turn and
    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/{max_turns} ===")
        # valid guess of correct length
        guess: str = input_guess(len(secret))
        # print emojis
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turn += 1
    # after loop ends move on to print final results
    if won:
        print(f"You won in {turn}/{max_turns}) turns!")
    else:
        print("x/6 - Sorry, try again tomorrow!")

    if __name__ == "__main__":
        main(secret="codes")
