import random

# 1. Print a welcome message
print("Welcome to Hangman")

# 2. Store a list of words and choose one randomly
word_list = ['python', 'java', 'swift', 'kotlin', 'hangman', 'apple', 'banana']
word_to_guess = random.choice(word_list)

# Create a display of underscores for the word
guessed_word = ['_' for _ in word_to_guess]

# Initialize variables for the game
attempts_left = 10
guessed_letters = set()

# 3. Keep asking the user to guess the word
while attempts_left > 0:
    print(f"\nAttempts left: {attempts_left}")
    print("Current word: " + ' '.join(guessed_word))

    # 3.3 Ask the user to enter a single letter
    guess = input("Guess a letter: ").lower()

    # 3.4 Check for valid input (only alphabets)
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid Character. Please enter a single alphabet.")
        continue

    # 3.6 Check if the letter was already guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue
        # Add guess to the set of guessed letters
        guessed_letters.add(guess)

        # 3.8 Check if the guess is correct
        if guess in word_to_guess:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempts_left -= 1

        # Check if the entire word has been guessed
        if '_' not in guessed_word:
            print("\nAwesome! You guessed the word correctly.")
            print(f"The word was: {''.join(guessed_word)}")
            break

    # Game over: either win or lose
    if attempts_left == 0:
        print("\nYou've run out of attempts.")
        print(f"The word was: {word_to_guess}")
        print("Thank you for playing. Better luck next time.")
    else:
        print("Thank you for playing. See you next time!")
