"""
CodeAlpha Internship - Python Programming
TASK 1: Hangman Game

"""

import random


# ============================================================
# PREDEFINED WORDS COLLECTION  
# ============================================================

WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "software"
]

MAX_INCORRECT_GUESSES = 6


# ============================================================
# DISPLAY THE CURRENT WORD
# ============================================================

def display_word(word, guessed_letters):
    """
    Show guessed letters and underscores for hidden letters.
    """

    result = []

    for letter in word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")

    return " ".join(result)


# ============================================================
# DISPLAY HANGMAN
# ============================================================

def display_hangman(incorrect_guesses):
    """
    Display the Hangman drawing according to the number
    of incorrect guesses.
    """

    stages = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]

    print(stages[incorrect_guesses])


# ============================================================
# MAIN HANGMAN GAME
# ============================================================

def play_hangman():

    # Randomly select one of the 5 hard-coded words.
    word = random.choice(WORDS)

    # Store letters guessed by the player.
    guessed_letters = set()

    # Count incorrect guesses.
    incorrect_guesses = 0

    print("=" * 50)
    print("CODEALPHA - HANGMAN GAME")
    print("=" * 50)

    print("\nGuess the hidden word one letter at a time.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses.")

    # Continue while the player has guesses remaining.
    while incorrect_guesses < MAX_INCORRECT_GUESSES:

        display_hangman(incorrect_guesses)

        print("Word:", display_word(word, guessed_letters))

        if guessed_letters:
            print(
                "Guessed letters:",
                ", ".join(sorted(guessed_letters))
            )

        # Check whether every letter has been guessed.
        if all(
            letter in guessed_letters
            for letter in word
        ):
            print("\nCongratulations!")
            print(f"You guessed the word: {word}")
            return

        # Ask the player for a letter.
        guess = input("\nEnter one letter: ").strip().lower()

        # Validate the input.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        # Prevent the same letter being guessed twice.
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        # Determine whether the guess is correct.
        if guess in word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")

    # Six incorrect guesses have been used.
    display_hangman(incorrect_guesses)

    print("\nGAME OVER!")
    print(f"The correct word was: {word}")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    play_hangman()