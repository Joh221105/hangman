from tkinter import *

root = Tk()
root.title('Hangman')
root.minsize(width=2000, height=1000)

lives = 5

canvas = Canvas(width=975, height=605)

hangman_stages = [
    PhotoImage(file="images/hangman0.png"),
    PhotoImage(file="images/hangman1.png"),
    PhotoImage(file="images/hangman2.png"),
    PhotoImage(file="images/hangman3.png"),
    PhotoImage(file="images/hangman4.png"),
    PhotoImage(file="images/hangman5.png"),
]

conditional_images = [
    PhotoImage(file="images/hangman_lose.png"),
    PhotoImage(file="images/hangman_win.png"),
]

def decrease_life():
    global lives, hangman_image
    lives -= 1
    if lives >= 0:
        canvas.itemconfig(hangman_image, image=hangman_stages[lives])
        print("Lives:", lives)


button = Button(text = 'Decrease Life', command = decrease_life)    
button.pack()

hangman_image = canvas.create_image(500, 350, image=hangman_stages[lives])
canvas.pack()




root.mainloop()