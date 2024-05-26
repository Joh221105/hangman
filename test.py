from tkinter import *
import random

word_bank = ['apple', 'watermelon', 'cat']
test_word = random.choice(word_bank)


def submit_input(event=None):
    try:
        user_input = int(entry.get())
        
        if 0 <= user_input <= 5:
            canvas.itemconfig(hangman_image, image=hangman_stages[user_input])
        else:
            result_label.config(text="Please enter a number between 0 and 5")
    except ValueError:
        result_label.config(text="Invalid input, please enter a valid number")
    finally:
        entry.delete(0, 'end')


root = Tk()
root.title('Hangman')
root.minsize(width=2000, height=1000)


canvas = Canvas(root, width=975, height=605)


hangman_stages = [
    PhotoImage(file="images/hangman0.png"),
    PhotoImage(file="images/hangman1.png"),
    PhotoImage(file="images/hangman2.png"),
    PhotoImage(file="images/hangman3.png"),
    PhotoImage(file="images/hangman4.png"),
    PhotoImage(file="images/hangman5.png"),
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