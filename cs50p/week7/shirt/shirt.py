import sys
from os.path import splitext
from PIL import Image, ImageOps


def is_valid(argument):
    if len(argument) < 3:
        sys.exit("Too few command-line arguments")
    if len(argument) > 3:
        sys.exit("Too many command-line arguments")

    file1, file2 = splitext(argument[1]) , splitext(argument[2])

    if file1[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input.")

    if file2[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output.")

    if not(file1[1] == file2[1]):
        sys.exit("Input file and output file have different extensions.")

    return True


def overlay_shirt(photo, overlayed):
    try:
        with Image.open("shirt.png") as photo:
            with Image.open(photo) as img:
                img = ImageOps.fit(img, photo.size).paste(photo, photo).save(overlayed)



    except FileNotFoundError:
        sys.exit("File does not exist")
    except OSError:
        sys.exit("Can not convert image")

if is_valid(sys.argv):
    overlay_shirt(sys.argv[1], sys.argv[2])