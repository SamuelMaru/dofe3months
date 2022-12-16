def main():
    time = input("whats the time: ")
    time = convert(time)
    if 420<= time <=480:
        print("breakfast time")
    elif 720<= time <= 780:
        print("lunch time")
    elif 1080<= time <= 1140:
        print("dinner time")
    else:
        print("Nothing.")


def convert(time):
    t = time.split(":")
    return (int(t[0])*60)+int(t[1])


if __name__ == "__main__":
    main()