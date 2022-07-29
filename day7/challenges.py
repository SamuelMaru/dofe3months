import csv

def challenge1():
    with open("data_ch1.txt", "r") as reader:
        lines = reader.readlines()
        lines.remove("Year Number_of_Bicycle Hires\n")
        total = 0
        for i in lines:
            total += int(i[5:-1])
        print(total)

def challenge2():
    with open("sample.csv", mode="r") as file:
            csvFile = list(csv.reader(file))
            print(csvFile)
challenge2()