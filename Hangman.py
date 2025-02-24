import random

def hangman_game():
    words = ["python", "hangman", "programming", "eternal", "concrete"]
    word = random.choice(words)
    guessed = set()
    attempts = 7
    display_word = ["_" for _ in word]

    while attempts > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter")
    elif guess in word:
        print("Correct guess!")