import random

def hangman_game():
    words = ["python", "hangman", "programming", "eternal", "concrete"]
    word = random.choice(words)
    guessed = set()
    attempts = 7
    display_word = ["_" for _ in word]

    