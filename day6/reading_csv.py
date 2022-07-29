import csv
with open("reading.csv",mode="r") as file:
    csvFile = list(csv.reader(file))
    print(csvFile)
