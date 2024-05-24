import random
import requests

website = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(website)

words = list(response.content.splitlines())

guessing_word = str(random.choice(words)).replace("b", "").replace('\'', "")
# print(guessing_word)

guessed_letters = []

hangman_ui = ["_ "]*len(guessing_word)

count = 0
lives = 5

while True:

    if lives == 0:
        print(f"You are out of lives, the word was: {guessing_word}")
        break

    if "_ " not in hangman_ui:
        if lives == 1:
            print(f"You win! The word was {guessing_word}, you had {lives} life remaining")
            break
        else:
            print(f"You win! The word was {guessing_word}, you had {lives} lives remaining")
            break
    user_guess = input("Enter a letter: ").lower()

    if user_guess == "quit":
        break

    if len(user_guess) > 1 or len(user_guess) == 0:
        print("Please enter 1 letter")
        continue

    elif user_guess in guessed_letters:
        print("You already guessed that letter!")

    elif user_guess in guessing_word:
        guessed_letters.append(user_guess)
        for index, x in enumerate(guessing_word):
            if x == user_guess:
                hangman_ui[index] = x

    elif user_guess not in guessing_word:
        guessed_letters.append(user_guess)
        lives -= 1
        print(f'You have {lives} lives remaining')

    print(f'Letters you have guessed: {guessed_letters}')
    print(" ".join(hangman_ui))
    print('\n')
