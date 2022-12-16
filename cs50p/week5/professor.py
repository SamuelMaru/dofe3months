import random
def get_level():
    while True:
        try:
            n = int(input("Choose a level from 1 to 3: "))
            if not 0<n<4:
                raise ValueError
            break
        except ValueError:
            continue
    return n
def generate_integer(lvl):
    start = [0, 10, 100]
    end = [9, 99, 999]
    return random.randint(start[lvl-1], end[lvl-1])
def main():
    points = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        for j in range(3):
            try:
                isz = int(input(f"{x} + {y} ="))
                if isz != z:
                    raise ValueError
                print("Correct!")
                points += 1
                break
            except ValueError:
                print("EEE")
                continue
        print(f"The correct answer was {z}")
    print(f"You got {points} points")

if __name__ == "__main__":
    main()
