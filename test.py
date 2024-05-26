from tkinter import *
import random

word_bank = ['apple', 'watermelon', 'cat']
test_word = random.choice(word_bank)

lives = 5

def submit_input(event=None):
    result_label.config(text="")
    global lives
    user_input = entry.get().strip()
    
    if len(user_input) != 1 or not user_input.isalpha():
        result_label.config(text="Invalid input, please enter a single letter")
    else:
        if user_input in test_word:
            print('Yes, that letter is in the word')
        else:
            print('No, that letter is not in the word')
            lives -= 1
            if lives >= 0:
                canvas.itemconfig(hangman_image, image=hangman_stages[lives])
            elif lives < 0:
                canvas.itemconfig(hangman_image, image=hangman_stages[6])
                result_label.config(text="OUT OF LIVES, YOU LOSE!", font=("Arial", 15))
    
    entry.delete(0, 'end')


root = Tk()
root.title('Hangman')
root.minsize(width=2000, height=1000)


canvas = Canvas(root, width=1400, height=800)


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

hangman_image = canvas.create_image(700, 400, image=hangman_stages[5])
canvas.pack()

instruction = Label(root, text="Enter a letter a-z")
instruction.pack()

entry = Entry(root, width=50)
entry.pack()

word_display = Label(root, text="_ " * len(test_word), font=("Arial", 20))
word_display.pack()

entry.bind('<Return>', submit_input)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()