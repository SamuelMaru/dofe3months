

def main():
    inp = input("Input: ")
    print(shorten(inp))

def shorten(inp):
    for characters in "aeiouAEIOU":
        inp = inp.replace(characters, "")
    return inp


if __name__ == "__main__":
    main()