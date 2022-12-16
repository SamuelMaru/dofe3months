import tabulate
import pandas as pd
import csv
import sys
def run(filename):
        try:
            print(filename)
            with open(filename) as file:
                table = pd.read_csv(filename,header = None, index_col = 0)
                print(table)
            print(tabulate.tabulate(table,tablefmt="grid"))
        except(FileNotFoundError):
            sys.exit("File not found.")

def is_valid(argument):
    if len(argument) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argument) > 2:
        sys.exit("Too many command-line arguments")

    if ".csv" not in argument[1]:
        sys.exit("Not a '.csv' file.")
    return True

if is_valid(sys.argv):
    run(sys.argv[1])
