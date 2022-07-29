def task_rainfall_():
    TEMPERATURE = [0]*12
    MONTH = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
    for i in range(12):
       TEMPERATURE[i] = input("Please enter temperature for " +MONTH[i])

    for i in range(12):
       print(MONTH[i] + ": " + TEMPERATURE[i])

    RAINFALL = [0]*12
    MONTH = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
    for i in range(12):
       RAINFALL[i] = float(input("Please enter rainfall for " +MONTH[i]+": "))


    total = 0
    for i in range(12):
      total += RAINFALL[i]

    average = total/12
    count = 0
    for i in range(12):
      if RAINFALL[i] > average:
        count += 1

    for i in range(12):
       print(MONTH[i] + ": ",RAINFALL[i])

    print("Total Rainfall:",round(total,1))
    print("Average:",average)
    print("Number of months above average:",count)

def task3():
    name = [0]*3
    marks = [[0]*5]*3
    for s in range(3):
        name[s] = input("Please enter student name: ")
        total = 0
        for m in range(5):
            marks[s][m] = int(input("Enter mark: "))
            total += marks[s][m]

        print("Total for Student",name[s],"is ",total)
        averageMark = total / 5
        print("Average mark for " + name[s] + " is " + str(averageMark))

task3()

