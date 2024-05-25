import random
import requests

website = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(website)

words = list(response.content.splitlines())

guessing_word = None

lives = None

while lives == None:
    difficulty_setting = input('Choose a difficulty: easy, medium, or hard: ').lower()
    if difficulty_setting == 'easy':
        lives = 9
    elif difficulty_setting == 'medium':
        lives = 6
    elif difficulty_setting == 'hard':
        lives = 3
    else:
        print("Sorry I didn't get that, would you like to play on easy, medium, or hard difficulty?")

length_of_word_chosen = False
temp_guess_word = None
word_chosen = False

while not length_of_word_chosen:
    length_choice = input('Type s for a short word, m for a medium word, or l for a long word: ').lower()
    if length_choice == 's':
        while not word_chosen:
            temp_guess_word = str(random.choice(words)).replace("b", "").replace('\'', "")
            if len(temp_guess_word) <=4:
                word_chosen = True
        length_of_word_chosen = True

    elif length_choice == 'm':
        while not word_chosen:
            temp_guess_word = str(random.choice(words)).replace("b", "").replace('\'', "")
            if len(temp_guess_word) > 4 and len(temp_guess_word) <= 7:
                word_chosen = True
        length_of_word_chosen = True

    elif length_choice == 'l':
        while not word_chosen:
            temp_guess_word = str(random.choice(words)).replace("b", "").replace('\'', "")
            if len(temp_guess_word) > 7 and len(temp_guess_word) <= 15:
                word_chosen = True
        length_of_word_chosen = True
    else:
        print('Sorry, please choose s for a short word, m for a medium word, l for a long word')

guessing_word = temp_guess_word

count = 0

guessed_letters = []

hangman_ui = ["_ "]*len(guessing_word)
print(" ".join(hangman_ui))

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
