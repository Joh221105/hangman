import random
import requests
from tkinter import *

website = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(website)

words = list(response.content.splitlines())

guessing_word = None

lives = 6

length_of_word_chosen = False
temp_guess_word = None
word_chosen = False

# while not length_of_word_chosen:
#     length_choice = input('Would you like a short(s), medium(m), or long(l) word: ').lower()
#     if length_choice == 's' or length_choice == 'short':
#         while not word_chosen:
#             temp_guess_word = str(random.choice(words)).replace("b", "").replace('\'', "")
#             if len(temp_guess_word) <=4:
#                 word_chosen = True
#         length_of_word_chosen = True

#     elif length_choice == 'm' or length_choice == 'medium':
#         while not word_chosen:
#             temp_guess_word = str(random.choice(words)).replace("b", "").replace('\'', "")
#             if len(temp_guess_word) > 4 and len(temp_guess_word) <= 7:
#                 word_chosen = True
#         length_of_word_chosen = True

#     elif length_choice == 'l' or length_choice == 'long':
#         while not word_chosen:
#             temp_guess_word = str(random.choice(words)).replace("b", "").replace('\'', "")
#             if len(temp_guess_word) > 7 and len(temp_guess_word) <= 15:
#                 word_chosen = True
#         length_of_word_chosen = True
#     else:
#         print('Sorry, please choose s for a short word, m for a medium word, l for a long word')

guessing_word = temp_guess_word.lower()

# guessed_letters = []

# hangman_ui = ["_ "]*len(guessing_word)
# print(" ".join(hangman_ui))

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

    user_guess = input("Enter a letter or guess the word: ").lower()

    if user_guess == guessing_word and lives > 0:
        print(f'YES YOU GOT IT! THE WORD WAS: {guessing_word}')
        break


    if user_guess == "quit":
        break

    if len(user_guess) == 0:
        print("Please enter 1 letter or guess a word")
        continue

    elif user_guess in guessed_letters:
        print("You already guessed that letter!")

    elif user_guess in guessing_word:
        guessed_letters.append(user_guess)
        for index, x in enumerate(guessing_word):
            if x == user_guess:
                hangman_ui[index] = x

    if user_guess != guessing_word:
        if len(user_guess) == 1 and user_guess not in guessing_word:
            guessed_letters.append(user_guess)
            lives -= 1
            print(f'You have {lives} lives remaining')
        elif len(user_guess) > 1:
            guessed_letters.append(user_guess)
            print(f'No the word is not {user_guess}, try again or guess a letter')
            lives -= 1
            print(f'You have {lives} lives remaining')

    print(f'Letters/Words you have guessed: {guessed_letters}')
    print(" ".join(hangman_ui))
    print('\n')
