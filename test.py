from tkinter import *
import random

word_bank = ['apple', 'watermelon', 'cat']
test_word = random.choice(word_bank)


def submit_input(event=None):
    user_input = entry.get().strip()
    
    if len(user_input) != 1 or not user_input.isalpha():
        result_label.config(text="Invalid input, please enter a single letter")
    else:
        if user_input in test_word:
            print('Yes, that letter is in the word')
        else:
            print('No, that letter is not in the word')
        result_label.config(text="")
    
    entry.delete(0, 'end')


root = Tk()
root.title('Hangman')
root.minsize(width=2000, height=1000)


canvas = Canvas(root, width=975, height=605)


hangman_stages = [
    PhotoImage(file="hangman/images/hangman0.png"),
    PhotoImage(file="hangman/images/hangman1.png"),
    PhotoImage(file="hangman/images/hangman2.png"),
    PhotoImage(file="hangman/images/hangman3.png"),
    PhotoImage(file="hangman/images/hangman4.png"),
    PhotoImage(file="hangman/images/hangman5.png"),
]

hangman_image = canvas.create_image(500, 350, image=hangman_stages[5])
canvas.pack()

instruction = Label(root, text="Enter a number between 0 and 5:")
instruction.pack()

entry = Entry(root, width=50)
entry.pack()

word_display = Label(root, text="_ " * len(test_word), font=("Arial", 20))
word_display.pack()

entry.bind('<Return>', submit_input)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()