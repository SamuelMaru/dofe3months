#
#          DO NOT EDIT
#
#          THIS IS WHERE WE STORE THE SEPERATE PARTS,
#          THE ACTUAL PROGRAM IS AT main.py
#


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x350")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 350,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    675.0,
    308.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    450.0,
    350.0,
    fill="#BEB7DF",
    outline="")

canvas.create_text(
    48.0,
    31.0,
    anchor="nw",
    text="NUMWORD",
    fill="#FFFFFF",
    font=("Roboto Bold", 64 * -1)
)

canvas.create_text(
    80.0,
    107.0,
    anchor="nw",
    text="Computing Competition 2020/21",
    fill="#FFFFFF",
    font=("Roboto", 18 * -1)
)

canvas.create_text(
    633.0,
    299.0,
    anchor="nw",
    text="OUTPUT",
    fill="#BEB7DF",
    font=("Roboto Bold", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg='white'
)
button_1.place(
    x=591.0,
    y=67.0,
    width=84.0,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg='white'
)
button_2.place(
    x=488.0,
    y=206.0,
    width=369.0,
    height=62.0
)

canvas.create_text(
    488.0,
    23.0,
    anchor="nw",
    text="Lucas Curran 10A      Alex Cleaton 10A      Samuel Maru 10A",
    fill="#BEB7DF",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    139.0,
    259.0,
    anchor="nw",
    text="Available Languages:",
    fill="#FFFFFF",
    font=("Roboto", 18 * -1)
)

canvas.create_text(
    145.0,
    277.0,
    anchor="nw",
    text="English & Mandarin",
    fill="#FFFFFF",
    font=("Roboto", 18 * -1)
)

canvas.create_text(
    42.0,
    170.0,
    anchor="nw",
    text="Simply enter a language along with a number,",
    fill="#FFFFFF",
    font=("Roboto", 18 * -1)
)

canvas.create_text(
    95.0,
    191.0,
    anchor="nw",
    text="and we’ll have it parsed as text!",
    fill="#FFFFFF",
    font=("Roboto", 18 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg='white'
)
button_3.place(
    x=487.0,
    y=67.0,
    width=84.0,
    height=53.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    672.5,
    164.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F4F4F4",
    highlightthickness=0
)
entry_1.place(
    x=510.5,
    y=142.0,
    width=324.0,
    height=43.0
)
window.resizable(False, False)
window.mainloop()
