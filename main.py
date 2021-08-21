from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
start = 4
timer = None

try:
    lang_data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    lang_data = pd.read_csv('./data/french_words.csv')
finally:
    to_learn = lang_data.to_dict(orient='records')


def guessed_correct():
    global random_word
    global to_learn
    to_learn.remove(random_word)
    canvas1.itemconfig(image_container, image=img)
    canvas1.itemconfig(language, text='French')
    random_word = random.choice(to_learn)
    canvas1.itemconfig(word, text=random_word['French'])
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    count_down(start)


def guessed_incorrect():
    global random_word
    canvas1.itemconfig(image_container, image=img)
    canvas1.itemconfig(language, text='French')
    random_word = random.choice(to_learn)
    canvas1.itemconfig(word, text=random_word['French'])
    count_down(start)


def count_down(count):
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count-1)
        if count == 1:
            canvas1.itemconfig(image_container, image=img1)
            canvas1.itemconfig(language, text='English')
            meaning = random_word['English']
            canvas1.itemconfig(word, text=meaning)


window = Tk()
window.title('Flash cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas1 = Canvas(width=800, height=526)
img = PhotoImage(file='./images/card_front.png')
img1 = PhotoImage(file='./images/card_back.png')
image_container = canvas1.create_image(400, 263, image=img)
language = canvas1.create_text(400, 113, text='French', fill='black', font=('Arial', 35, 'italic'))
random_word = random.choice(to_learn)
word = canvas1.create_text(400, 263, text=random_word['French'], fill='black', font=('Arial', 45, 'bold'))
canvas1.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas1.grid(column=0, row=0, columnspan=3)

right_img = PhotoImage(file='./images/right.png')
correct = Button(image=right_img, width=100, height=100, highlightthickness=0, command=guessed_correct)
correct.grid(column=0, row=2)

wrong_img = PhotoImage(file='./images/wrong.png')
incorrect = Button(image=wrong_img, width=100, height=100, highlightthickness=0, command=guessed_incorrect)
incorrect.grid(column=2, row=2)

count_down(start)

window.mainloop()
