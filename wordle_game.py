# Wordle-style guessing game
# The secret word is 'mormon'
# The player has 6 attempts to guess the word.
# I added a code to number the attempts the user is currently on.

secret_word = "mormon"
max_attempts = 6

print("Welcome to the Word Guessing Game!")
print(f"You have {max_attempts} attempts to guess the 6-letter secret word.")
print()
print("Your hint is: ______")
for attempt in range(1, max_attempts + 1):
    guess = input(f"Attempt {attempt}: Enter your guess word: ").lower()
    if len(guess) != len(secret_word):
        print(f"Your guess must be {len(secret_word)} letters.")
        continue
    
    # Build hint string
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()  # Correct letter and position
        elif guess[i] in secret_word:
            hint += guess[i]  # Correct letter, wrong position
        else:
            hint += "_"  # Incorrect letter
    print(f"Hint: {hint}")
    
    if guess == secret_word:
        print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
        if attempt == 1:
            print(f"It took you {attempt} guess.")
        else:
            print(f"It took you {attempt} guesses.")
        break
else:
    print(f"Sorry, you've used all attempts. The secret word was '{secret_word}'.")
