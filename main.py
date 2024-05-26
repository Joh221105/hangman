from tkinter import *
import random
import requests

website = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(website)

words = list(response.content.splitlines())

guessed_letters = []
word_list_form = []


lives = 5

def choose_difficulty(start_button):

    # get rid of the start game button
    start_button.destroy()

    # word length instruction label
    word_display = Label(root, text="Choose the length of word you want", font=("Arial", 20))
    word_display.pack(ipady=100)

    # generate 3 buttons to choose word length
    short_word_button = Button(root, text="Short word", command=lambda:generate_word(4, short_word_button, medium_word_button, long_word_button, word_display), font=("Arial", 15))
    short_word_button.pack(pady=20)
    medium_word_button = Button(root, text="Medium word", command=lambda:generate_word(7, short_word_button, medium_word_button, long_word_button, word_display),font=("Arial", 15))
    medium_word_button.pack(pady=20)
    long_word_button = Button(root, text="Long word", command=lambda:generate_word(15, short_word_button, medium_word_button, long_word_button, word_display),font=("Arial", 15))
    long_word_button.pack(pady=20)

def generate_word(word_length, short_word_button, medium_word_button, long_word_button, word_display):
    
    # destroy buttons and instruction label
    short_word_button.destroy()
    medium_word_button.destroy()
    long_word_button.destroy()
    word_display.destroy()

    # Filter out words to get a word with appropriate length
    test_word = str(random.choice(words)).replace("b", "", 1).replace('\'', "")

    if word_length == 4:
        while len(test_word) > 4:
            test_word = str(random.choice(words)).replace("b", "", 1).replace('\'', "")
    elif word_length == 7:
        while len(test_word) <= 4 and len(test_word) > 7:
            test_word = str(random.choice(words)).replace("b", "", 1).replace('\'', "")
    elif word_length == 15: 
        while len(test_word) <=7:
            test_word = str(random.choice(words)).replace("b", "", 1).replace('\'', "")

    start_game(test_word)

def start_game(hangman_word):

    global word_list_form

    result_label = Label(root, text="", font=('Arial', 20))
    result_label.pack(pady=10)

    canvas = Canvas(root, width=1400, height=800) 

    hangman_image = canvas.create_image(700, 400, image=hangman_stages[5])
    canvas.pack()

    # instruction label for entry
    instruction = Label(root, text="Enter a letter a-z")
    instruction.pack()

    word_list_form = ["_ "]*len(hangman_word)

    # generates _ for each letter in the word
    word_display = Label(root, text="_ " * len(hangman_word), font=("Arial", 20), pady=20)
    word_display.pack()

    hangman_game(canvas, hangman_image, word_display, hangman_word, result_label)


def hangman_game(canvas, hangman_image, word_display, hangman_word, result_label):

    guessed_list = Label(text=f'{guessed_letters}', font=('Arial', 20), pady=20)
    guessed_list.pack()

    # listens to enter key and passes user input to submit input function
    entry = Entry(root, width=50, font=("Arial", 20))
    entry.pack()
    entry.bind('<Return>', lambda event: submit_input(entry, canvas, word_display, hangman_word, hangman_image, guessed_list, result_label))


def submit_input(entry, canvas, word_display, hangman_word, hangman_image, guessed_list,result_label):
    global lives
    result_label.config(text="")
    user_input = entry.get().strip().lower()
    
    if not user_input.isalpha():
        result_label.config(text="Invalid input, please enter a single letter/word")

    elif user_input in guessed_letters:
        result_label.config(text=f"YOU ALREADY GUESSED THE LETTER: {user_input}", font=("Arial", 15))

    elif user_input == hangman_word and lives >= 0:
        result_label.config(text=f"YOU WIN! THE WORD WAS: {hangman_word.upper()}", font=("Arial", 15))
        word_display.config(text=f"{hangman_word}")
        entry.destroy()
        replay_button = Button(root, text="Replay", command=reset_game, font=("Arial", 15))
        replay_button.pack()
        return None

    elif user_input != hangman_word and len(user_input) > 1 and lives >=0:
        result_label.config(text=f"Wrong! The word is not {user_input}, guess again", font=("Arial", 15))
        guessed_letters.append(user_input)
        lives -= 1
        canvas.itemconfig(hangman_image, image=hangman_stages[lives])
        guessed_list.config(text=f'Guessed Letters/Words: {", ".join(guessed_letters)}')

    else:
        if user_input in hangman_word:
            guessed_letters.append(user_input)
            guessed_list.config(text=f'Guessed Letters/Words: {", ".join(guessed_letters)}')
            update_blanks(word_display, hangman_word, user_input)
            if '_ ' not in word_list_form and lives >= 0:
                canvas.itemconfig(hangman_image, image=hangman_stages[7])
                result_label.config(text=f"YOU WIN! THE WORD WAS: {hangman_word.upper()}", font=("Arial", 15))
                entry.destroy()
                replay_button = Button(root, text="Replay", command=reset_game, font=("Arial", 15))
                replay_button.pack()
                return None
        else:
            guessed_letters.append(user_input)
            guessed_list.config(text=f'Guessed Letters/Words: {", ".join(guessed_letters)}')
            lives -= 1
            if lives >= 0:
                canvas.itemconfig(hangman_image, image=hangman_stages[lives])
            elif lives < 0:
                canvas.itemconfig(hangman_image, image=hangman_stages[6])
                result_label.config(text=f"OUT OF LIVES, THE WORD WAS {hangman_word.upper()}", font=("Arial", 15))
                entry.destroy()
                replay_button = Button(root, text="Replay", command=reset_game, font=("Arial", 15))
                replay_button.pack()
                return None
    
    entry.delete(0, 'end')

def update_blanks(word_display, hangman_word, user_input):

    global word_list_form

    for index, x in enumerate(hangman_word):
            if x == user_input:
                word_list_form[index] = x
    word_display.config(text=f"{' '.join(word_list_form)}")

def reset_game():
    global guessed_letters, lives, word_list_form

    for widget in root.winfo_children():
        widget.destroy()
    guessed_letters = []
    lives = 5
    word_list_form = []
    start_button = Button(root, text="Start Game", command=lambda: choose_difficulty(start_button),font=("Arial", 15))
    start_button.pack(pady=500)
    


root = Tk()
root.title('Hangman')
root.minsize(width=2000, height=1500)

start_button = Button(root, text="Start Game", command=lambda:choose_difficulty(start_button), font=("Arial", 15))
start_button.pack(pady=500)


hangman_stages = [
    PhotoImage(file="images/hangman0.png"),
    PhotoImage(file="images/hangman1.png"),
    PhotoImage(file="images/hangman2.png"),
    PhotoImage(file="images/hangman3.png"),
    PhotoImage(file="images/hangman4.png"),
    PhotoImage(file="images/hangman5.png"),
    PhotoImage(file="images/hangman_lose.png"),
    PhotoImage(file="images/hangman_win.png")
]

root.mainloop()