from tkinter import *
import random

word_bank = ['apple', 'watermelon', 'cat']
guessed_letters = []


lives = 5

def choose_difficulty():

    # get rid of the start game button
    start_button.destroy()

    # word length instruction label
    word_display = Label(root, text="Choose the length of word you want", font=("Arial", 20), pady=20)
    word_display.pack()

    # generate 3 buttons to choose word length
    short_but = Button(root, text="Short word", command=lambda:generate_word(4, short_but, med_but, long_but, word_display))
    short_but.pack(pady=20)
    med_but = Button(root, text="Medium word", command=lambda:generate_word(7, short_but, med_but, long_but, word_display))
    med_but.pack(pady=20)
    long_but = Button(root, text="Long word", command=lambda:generate_word(15, short_but, med_but, long_but, word_display))
    long_but.pack(pady=20)

def generate_word(word_length, short_but, med_but, long_but, word_display):
    
    # destroy buttons and instruction label
    short_but.destroy()
    med_but.destroy()
    long_but.destroy()
    word_display.destroy()

    # Filter out words to get a word with appropriate length
    test_word = random.choice(word_bank)

    if word_length == 4:
        while len(test_word) > 4:
            test_word = random.choice(word_bank)
    elif word_length == 7:
        while len(test_word) <= 4 and len(test_word) < 7:
            test_word = random.choice(word_bank)
    elif word_length == 15: 
        while len(test_word) <=7:
            test_word = random.choice(word_bank)

    start_game(test_word)

def start_game(hangman_word):

    canvas = Canvas(root, width=1400, height=800) 

    hangman_image = canvas.create_image(700, 400, image=hangman_stages[5])
    canvas.pack()

    # instruction label for entry
    instruction = Label(root, text="Enter a letter a-z")
    instruction.pack()

    # generates _ for each letter in the word
    word_display = Label(root, text="_ " * len(hangman_word), font=("Arial", 20), pady=20)
    word_display.pack()

    hangman_game(canvas, hangman_image, word_display, hangman_word)


def hangman_game(canvas, hangman_image, word_display, hangman_word):

    guessed_list = Label(text=f'{guessed_letters}')
    guessed_list.pack()

    # listens to enter key and passes user input to submit input function
    entry = Entry(root, width=50)
    entry.pack()
    entry.bind('<Return>', lambda event: submit_input(entry, canvas, word_display, hangman_word, hangman_image, guessed_list))


def submit_input(entry, canvas, word_display, hangman_word, hangman_image, guessed_list):
    global lives, result_label
    result_label.config(text="")
    user_input = entry.get().strip()
    
    if len(user_input) != 1 or not user_input.isalpha():
        result_label.config(text="Invalid input, please enter a single letter")
    else:
        if user_input in hangman_word:
            print('Yes, that letter is in the word')
            guessed_letters.append(user_input)
            guessed_list.config(text=f'Guessed Letters: {" ".join(guessed_letters)}')
            update_blanks(word_display, user_input)
        else:
            print('No, that letter is not in the word')
            guessed_letters.append(user_input)
            guessed_list.config(text=f'Guessed Letters: {" ".join(guessed_letters)}')
            lives -= 1
            if lives >= 0:
                canvas.itemconfig(hangman_image, image=hangman_stages[lives])
            elif lives < 0:
                canvas.itemconfig(hangman_image, image=hangman_stages[6])
                result_label.config(text="OUT OF LIVES, YOU LOSE!", font=("Arial", 15))
    
    entry.delete(0, 'end')

def update_blanks(word_display, user_input):
    # TODO
    # update the word blank labels
    pass

root = Tk()
root.title('Hangman')
root.minsize(width=2000, height=1000)

start_button = Button(root, text="Start Game", command=choose_difficulty)
start_button.pack()


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

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()