calculation = ""
while not("=" in calculation):
    calculation += input("enter: ")
print("\nThe Answer is:",eval(calculation[0:-1]))