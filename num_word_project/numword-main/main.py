GERMAN_SMALL_NUMBERS = [
    "null",
    "ein",
    "zwei",
    "drei",
    "vier",
    "fünf",
    "sechs",
    "sieben",
    "acht",
    "neun",
    "zehn",
    "elf",
    "zwölf",
    "dreizehn",
    "vierzehn",
    "fünfzehn",
    "sechszehn",
    "siebtzehn",
    "achtzehn",
    "neunzehn",
    "zwanzig",
]
GERMAN_MULTIPLES_OF_TEN = [
    "null",
    "zehn",
    "zwanzig",
    "dreizig",
    "vierzig",
    "fünfzig",
    "sechszig",
    "siebzig",
    "achtzig",
    "neuzig",
]
GERMAN_POWERS_OF_THOUSAND = [
    "",
    "tausend",
    "million",
    "milliarde",
    "billion",
    "billiarde",
    "trillion",
]

GERMAN_SMALL_THOUSAND_POWER_ROOTS = [
    "",
    "m",
    "bez",
    "b",
    "quadr",
    "quint",
    "sext",
    "sept",
    "okt",
    "quin",
    "dez",
]
GERMAN_ADDITIVE_THOUSAND_POWER_ROOTS = [
    "",
    "un",
    "duo",
    "tre",
    "quattuor",
    "quin",
    "sex",
    "septen",
    "octo",
    "novem",
]
GERMAN_TEN_THOUSAND_POWER_ROOTS = [
    "",
    "deztillion",
    "dezilliarde",
    "trigintillion",
    "quadragintillion",
    "quinquagintillion",
    "sexagintillion",
    "septuagintillion",
    "oktogintillion",
    "nonagintillion",
]


def convert_fractional_german(n):
    if n[-1] == "0":
        return ""
    else:
        parts = []
        n = str(n)
        for i in range(len(n)):
            parts.append(GERMAN_SMALL_NUMBERS[int(n[i])])
        return "-point-" + "-".join(parts[0:])


def power_of_thousand_german(n):
    if n == 0:
        return ""
    n -= 1
    if n == 0:
        return "tausend"
    if n < 10:
        return GERMAN_SMALL_THOUSAND_POWER_ROOTS[n] + "illion"
    if n == 100:
        return "centillion"
    return (
        GERMAN_ADDITIVE_THOUSAND_POWER_ROOTS[n % 10]
        + GERMAN_TEN_THOUSAND_POWER_ROOTS[n // 10]
    )


def convert_section_german(n, power):
    if n == 0:
        return
    if n >= 100:
        yield GERMAN_SMALL_NUMBERS[n // 100]
        yield "hundert"
        if n % 100 != 0:
            yield "und"
    n %= 100
    if 0 < n < 20:
        yield GERMAN_SMALL_NUMBERS[n]
    elif n != 0:
        yield GERMAN_MULTIPLES_OF_TEN[n // 10]
        if n % 10 != 0:
            yield GERMAN_SMALL_NUMBERS[n % 10]
    if power:
        yield power


def convert_int_german(n):
    parts = []
    power = 0
    done_and = False
    while n:
        section = "-".join(
            convert_section_german(n % 1000, power_of_thousand_german(power))
        )
        if not done_and and n >= 1000 and section:
            if n % 1000 < 100:
                section = f"und-{section}"
            done_and = True
        if section:
            parts.append(section)
        n //= 1000
        power += 1
    if parts == []:
        return "null"
    return "-".join(parts[::-1])


def convert_number_german(n):
    if "." in str(n):
        N_SECTION = str(n).split(".")
        return_value = convert_int_german(
            int(N_SECTION[0])
        ) + convert_fractional_german(str(N_SECTION[1]))
    else:
        return_value = convert_int_german(n)
    return return_value


ENGLISH_SMALL_NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
]
ENGLISH_MULTIPLES_OF_TEN = [
    "zero",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
ENGLISH_POWERS_OF_THOUSAND = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
]

ENGLISH_SMALL_THOUSAND_POWER_ROOTS = [
    "",
    "m",
    "b",
    "tr",
    "quadr",
    "quint",
    "sext",
    "sept",
    "oct",
    "non",
    "dec",
]
ENGLISH_ADDITIVE_THOUSAND_POWER_ROOTS = [
    "",
    "un",
    "duo",
    "tre",
    "quattuor",
    "quin",
    "sex",
    "septen",
    "octo",
    "novem",
]
ENGLISH_TEN_THOUSAND_POWER_ROOTS = [
    "",
    "dec",
    "vigint",
    "trigint",
    "quadragint",
    "quinquagint",
    "sexagint",
    "septuagint",
    "octogint",
    "nonagint",
]


def convert_fractional_english(n):
    if n[-1] == "0":
        return ""
    else:
        parts = []
        n = str(n)
        for i in range(len(n)):
            parts.append(ENGLISH_SMALL_NUMBERS[int(n[i])])
        return "-point-" + "-".join(parts[0:])


def power_of_thousand_english(n):
    if n == 0:
        return ""
    n -= 1
    if n == 0:
        return "thousand"
    if n < 10:
        return ENGLISH_SMALL_THOUSAND_POWER_ROOTS[n] + "illion"
    if n == 100:
        return "centillion"
    return (
        ENGLISH_ADDITIVE_THOUSAND_POWER_ROOTS[n % 10]
        + ENGLISH_TEN_THOUSAND_POWER_ROOTS[n // 10]
        + "illion"
    )


def convert_section_english(n, power):
    if n == 0:
        return
    if n >= 100:
        yield ENGLISH_SMALL_NUMBERS[n // 100]
        yield "hundred"
        if n % 100 != 0:
            yield "and"
    n %= 100
    if 0 < n < 20:
        yield ENGLISH_SMALL_NUMBERS[n]
    elif n != 0:
        yield ENGLISH_MULTIPLES_OF_TEN[n // 10]
        if n % 10 != 0:
            yield ENGLISH_SMALL_NUMBERS[n % 10]
    if power:
        yield power


def convert_int_english(n):
    parts = []
    power = 0
    done_and = False
    while n:
        section = "-".join(
            convert_section_english(n % 1000, power_of_thousand_english(power))
        )
        if not done_and and n >= 1000 and section:
            if n % 1000 < 100:
                section = f"and-{section}"
            done_and = True
        if section:
            parts.append(section)
        n //= 1000
        power += 1
    if parts == []:
        return "zero"
    return "-".join(parts[::-1])


def convert_number_english(n):
    if "." in str(n):
        N_SECTION = str(n).split(".")
        return_value = convert_int_english(
            int(N_SECTION[0])
        ) + convert_fractional_english((str(N_SECTION[1])))
    else:
        return_value = convert_int_english(n)
    return return_value


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("NUMWORD")
window.geometry("900x350")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=350,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(675.0, 308.0, image=image_image_1)

outputspace = canvas.create_text(
    518.0,
    305.0,
    anchor="nw",
    text="OUTPUT",
    fill="#BEB7DF",
    font=("Roboto Bold", 9 * -1),
)
copy_image=Image.open("C:\\SAMUEL_FOLDER\DofE\\num_word_project\\numword-main\\assets\\copy.png")


copy_image=copy_image.resize((45, 35))
copy_image = ImageTk.PhotoImage(copy_image)

copy_button = Button(
    image= copy_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copy(),
    relief="raised",
    bg="white",
    activebackground="white",
)
copy_button.place(x=850.0, y=280.0, width=45.0, height=53.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: changemodeger(),
    relief="raised",
    bg="white",
    activebackground="#B266FF",
)
button_1.place(x=591.0, y=67.0, width=84.0, height=53.0)


button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: changeoutput(),
    relief="raised",
    bg="white",
    activebackground="white",
)
button_2.place(x=488.0, y=206.0, width=369.0, height=62.0)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(674.0, 32.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(225.0, 175.0, image=image_image_3)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: changemodeeng(),
    relief="raised",
    bg="white",
    activebackground="#B266FF",
)
button_3.place(x=487.0, y=67.0, width=84.0, height=53.0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(672.5, 164.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#F4F4F4", highlightthickness=0)
entry_1.place(x=510.5, y=142.0, width=324.0, height=43.0)



def changemodeeng():
    file = open("data.txt", "w")
    file.write("ENG")
    file.close()
    button_1.config(bg="white")
    button_3.config(bg="#6600CC")


def changemodeger():
    file = open("data.txt", "w")
    file.write("GER")
    file.close()
    button_3.config(bg="white")
    button_1.config(bg="#6600CC")


current_mode = "ENG"
def copy():
    file = open("data.txt", "r")
    cur_mode = file.readline()
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    if cur_mode == "ENG":
        window.clipboard_append(str(convert_number_english(float(entry_1.get()))))
    if cur_mode == "GER":
        window.clipboard_append(str(convert_number_german(float(entry_1.get()))))

def changeoutput():
    file = open("data.txt", "r")
    cur_mode = file.readline()
    file.close()
    if cur_mode == "GER":
        print("converting ger")
        inp = entry_1.get()
        canvas.itemconfig(outputspace,fill="black", text=str(convert_number_german(float(inp))))
    elif cur_mode == "ENG":
        print("converting eng")
        inp = entry_1.get()
        canvas.itemconfig(outputspace,fill="black", text=str(convert_number_english(float(inp))))
    else:
        print("Something's gone wrong...")



window.resizable(False, False)
window.mainloop()