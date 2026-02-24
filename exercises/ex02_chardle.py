"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730802154"


# Getting an error for the first str


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")

    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    # put exit if its gonns return something wrong
    # remember return must be same place as the if
    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()

    return letter


# keep up with last lesson on "f"
def contains_char(word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")
    # INDENTATIONS MATTER SO MUCH

    count: int = 0
    # basically saying letter input has to equal letter of the word
    # if its true it then executes whats under
    if word[0] == letter:
        print(f"{letter} found at index 0")
        count = count + 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count = count + 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count = count + 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count = count + 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count = count + 1
    # this happens if none of the above is true
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
