
# Task 2: Hangman Game (with hints)

import random

# List of words and hints
words = {
    "tiger": "A big wild cat",
    "laptop": "Portable computer",
    "rain": "Falling water from the sky",
    "apple": "Red or green fruit",
    "india": "A country in Asia"
}

# Pick a random word
word, hint = random.choice(list(words.items()))
guessed_letters = []
chances = 6

print("Welcome to Hangman!")
print("Hint:", hint)

# Game loop
while chances > 0:
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word:", ' '.join(display))

    if "_" not in display:
        print("You won! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        chances -= 1
        print("Wrong guess. Chances left:", chances)

if chances == 0:
    print("Game over! The word was:", word)