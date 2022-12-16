def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    firstnum = False
    valid = False
    abc = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
    if s[0] in abc and s[1] in abc:
        global i
        for i in s:
            try:
                if int(i)==0:
                    return False
                sedit = str(i)+ s.split(str(i), 1)[-1]
                break
            except ValueError:
                continue

        for j in abc:
            if j in sedit:
                return False
        return True
    else:
        return False







main()