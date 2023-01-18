from tkinter import *
import requests
import random

quotes = {0: "איזה ארטיק קרח באלך?",
          1: "בוא אני אצייר לך מכונית",
          2: "ראש כרוב יש לך אתה",
          3: "אה טיטוש",
          4: "מי הדליק את הדוד?",
          5: "אני הלכתי",
          6: "היידה בי היידה בו היידה מכבי יפו",
          7: "למה לא 100?"}


def get_quote():
    # response = requests.get(url="https://api.kanye.rest/n")
    # response.raise_for_status()
    # data = response.json()
    # with open(file="dadigenerator\quotes", mode="w") as file:

    current_quote = quotes[random.randint(0, len(quotes) - 1)]
    canvas.itemconfig(quote_text, text=current_quote)


window = Tk()
window.title("dadi Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="../../PycharmProjects/dadigenerator/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Dadi Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

dadi_img = PhotoImage(file="dadi.png")
kanye_button = Button(image=dadi_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
