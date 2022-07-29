import day4

choice = input("Enter the currency you are converting from (£ or €): ")
amount = int(input("How many "+choice+" are you converting: "))

if choice == "£":
    print(choice+str(amount)+" is €"+str(day4.pounds_to_euros(amount)))
elif choice == "€":
    print(choice+str(amount)+" is £"+str(day4.euros_to_pounds(amount)))