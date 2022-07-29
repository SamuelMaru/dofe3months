import csv
import os

with open("goldmedals.csv","r") as medals:
    reader = list(csv.reader(medals))
    total = 0
    for i in reader[1]:
        total += int(i)
print(total)