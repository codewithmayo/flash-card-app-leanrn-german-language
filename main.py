import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_lean.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def tick_button():
    to_learn.remove(current_card)
    data2 = pandas.DataFrame(to_learn)
    data2.to_csv("words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_photo)
    flip_timer = window.after(3000, func=flip_card)


# flip card
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(10000, func=flip_card)

data = pandas.read_csv("data/german_words.csv")
card_back_image = PhotoImage(file="images/card_back.png")

# --------------------------------GUI--------------------------------------
# card
canvas = Canvas(width=800, height=526)
card_front_photo = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_photo)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
right_button = Button(image=tick_image, highlightthickness=0, command=tick_button)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
