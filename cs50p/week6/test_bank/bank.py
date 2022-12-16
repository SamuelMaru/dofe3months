
def value(greeting):
    if greeting[0] =="h" and greeting!="hello":
        return "$20"
    elif greeting[0]!="h":
        return "$100"
    else:
        return "$0"
def main():
    greeting = input("Greeting: ").lower()
    print(value(greeting))