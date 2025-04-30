import random
word_list = ['python', 'jumps', 'liver', 'back', 'swift', 'courage', 'fox', 'mask', 'dry']
word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6
print("Welcome to Hangman!")
while incorrect_guesses < max_incorrect_guesses:
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {displayed_word}")
    print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print(f"Good guess! '{guess}' is in the word!")
    else:
        incorrect_guesses += 1
        print(f"Oops! '{guess}' is not in the word.")
    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You've guessed the word: {word}")
        break
else:
    print(f"Game Over! The word was: {word}")
