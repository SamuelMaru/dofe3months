import random
while True:
    try:
        n = random.randint(1, int(input("Level: ")))
        break
    except ValueError:
        continue

guess = -1
while guess != n:
    try:
        guess = int(input("Guess: "))
        if n<guess:
            print("Too large")
        elif n>guess:
            print("Too small")
        else:
            print("Just right!")
    except ValueError:
        continue

