from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


window = Tk()
window.title("Anki Clone")

window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("./data/french_words.csv")
    all_cards = og_data.to_dict(orient='records')
else:
    all_cards = data.to_dict(orient='records')
    
    
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

card = canvas.create_image(400,263, image = card_front)
lang = canvas.create_text(400,100,text="Language", font=("Ariel", 20))
words = canvas.create_text(400, 250, text="Word", font=("Ariel", 40))

def flip_card():
    canvas.itemconfig(card, image = card_back)
    canvas.itemconfig(words, text = current_card["English"], fill="white")
    canvas.itemconfig(lang, text = "English", fill = "white")

flip_timer = window.after(3000, func=flip_card)

words_learnt = []
to_learn = all_cards
def learnt():
    
    to_learn.remove(current_card)
    words_learnt.append(current_card)
    
    next_card()
    
def save_files():
    if messagebox.askyesno("Save Progress", "Do you want to save your progress?") == True:
        words_to_learn = pandas.DataFrame(to_learn)
        words_to_learn.to_csv("data/words_to_learn.csv", index=False, mode="w")
        words_learnt_df = pandas.DataFrame(words_learnt)
        words_learnt_df.to_csv("./data/words_learnt.csv")
        window.destroy()
    else:
        window.destroy()
        

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image = card_front)
    current_card = random.choice(all_cards)
    canvas.itemconfig(lang, text = "French", fill="black")
    canvas.itemconfig(words, text = current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

next_card()

canvas.grid(row=0, column=0, columnspan=2, sticky="EW")
rht_btn = Button(width=100, height=100, image=right_img, command=learnt, highlightthickness=0)
wrng_btn = Button(width=100, height=100, image=wrong_img, command=next_card, highlightthickness=0)
rht_btn.grid(row=1, column=0)
wrng_btn.grid(row=1, column=1)

window.protocol("WM_DELETE_WINDOW", save_files)
window.mainloop()
