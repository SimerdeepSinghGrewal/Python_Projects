from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


def word_select():
    global rand_word, timer
    window.after_cancel(timer)
    rand_word = random.choice(data_dict)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=rand_word["French"], fill="black")
    canvas.itemconfig(display, image=front_img)
    timer = window.after(3000, eng_word)


def know_word():
    global rand_word, data_dict
    data_dict.remove(rand_word)
    word_select()


def not_know():
    global rand_word, new_dict
    new_dict.append(rand_word)
    unknown = pandas.DataFrame(new_dict)
    unknown.to_csv("data/words_to_learn.csv", index=False)
    word_select()


def eng_word():
    canvas.itemconfig(display, image=back_img)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=rand_word["English"], fill="white")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)

timer = window.after(3000, eng_word)
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
display = canvas.create_image(400, 263, image=front_img)
lang = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

button_r = Button(image=right_img, highlightthickness=0, command=know_word)
button_r.grid(column=0, row=1)
button_w = Button(image=wrong_img, highlightthickness=0, command=not_know)
button_w.grid(column=1, row=1)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
rand_word = {}
new_dict = []
word_select()

window.mainloop()
