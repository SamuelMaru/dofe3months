import sys
import csv

def is_valid(argument):
    if len(argument) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argument) > 3:
        sys.exit("Too many command-line arguments")

    if not(argument[1].endswith(".csv") and argument[2].endswith(".csv")):
        sys.exit("Could not read the file.")

    return True
def writing_csv(finput, foutput):
    try:
        with open(finput, "r", newline="") as f:
            reader = csv.DictReader(f)
            with open(foutput,"w") as newf:
                writer = csv.writer(newf)
                writer = csv.DictWriter(newf, fieldnames=["Firstname", "Lastname", "House"])
                writer.writeheader()
                for rows in reader:
                    name = rows["name"].split(",")
                    writer.writerow({"Firstname": name[1].strip(), "Lastname": name[0].strip(), "House": rows["house"].strip()})
    except FileNotFoundError:
        sys.exit("Could not read the file.")


if is_valid(sys.argv):
    writing_csv(sys.argv[1], sys.argv[2])

