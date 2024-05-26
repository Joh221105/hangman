from tkinter import *
import random

word_bank = ['apple', 'watermelon', 'cat']


lives = 5

def choose_difficulty():

    # get rid of the start game button
    start_button.destroy()

    # Instruction label
    word_display = Label(root, text="Choose the length of word you want", font=("Arial", 20), pady=20)
    word_display.pack()

    # generate 3 buttons
    short_but = Button(root, text="Short word", command=lambda:generate_word(4, short_but, med_but, long_but))
    short_but.pack(pady=20)
    med_but = Button(root, text="Medium word", command=lambda:generate_word(7, short_but, med_but, long_but))
    med_but.pack(pady=20)
    long_but = Button(root, text="Long word", command=lambda:generate_word(15, short_but, med_but, long_but))
    long_but.pack(pady=20)

def generate_word(word_length, short_but, med_but, long_but):
    
    # TODO
    # destroy buttons
    short_but.destroy()
    med_but.destroy()
    long_but.destroy()

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



    print(hangman_word)

    word_display = Label(root, text="_ " * len(hangman_word), font=("Arial", 20))
    word_display.pack()

def update_blanks():
    # TODO
    # update the word blank labels
    pass


# def submit_input(event=None):
#     result_label.config(text="")
#     global lives
#     user_input = entry.get().strip()
    
#     if len(user_input) != 1 or not user_input.isalpha():
#         result_label.config(text="Invalid input, please enter a single letter")
#     else:
#         if user_input in test_word:
#             print('Yes, that letter is in the word')
#         else:
#             print('No, that letter is not in the word')
#             lives -= 1
#             if lives >= 0:
#                 canvas.itemconfig(hangman_image, image=hangman_stages[lives])
#             elif lives < 0:
#                 canvas.itemconfig(hangman_image, image=hangman_stages[6])
#                 result_label.config(text="OUT OF LIVES, YOU LOSE!", font=("Arial", 15))
    
#     entry.delete(0, 'end')


root = Tk()
root.title('Hangman')
root.minsize(width=2000, height=1000)

start_button = Button(root, text="Start Game", command=choose_difficulty)
start_button.pack()


# canvas = Canvas(root, width=1400, height=800)


# hangman_stages = [
#     PhotoImage(file="images/hangman0.png"),
#     PhotoImage(file="images/hangman1.png"),
#     PhotoImage(file="images/hangman2.png"),
#     PhotoImage(file="images/hangman3.png"),
#     PhotoImage(file="images/hangman4.png"),
#     PhotoImage(file="images/hangman5.png"),
#     PhotoImage(file="images/hangman_lose.png"),
#     PhotoImage(file="images/hangman_win.png")
# ]

# hangman_image = canvas.create_image(700, 400, image=hangman_stages[5])
# canvas.pack()

# instruction = Label(root, text="Enter a letter a-z")
# instruction.pack()

# entry = Entry(root, width=50)
# entry.pack()


# entry.bind('<Return>', submit_input)

# result_label = Label(root, text="")
# result_label.pack(pady=10)

root.mainloop()