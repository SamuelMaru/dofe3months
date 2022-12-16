#print(exec(input("Expression: ")))

# alternatively:

def evaluate(n):
    ns = n.split(" ")
    x,y,z = float(ns[0]), ns[1], float(ns[2])
    if y =="-":
        print(round(x-z,1))
    elif y == "+":
        print(round(x + z, 1))
    elif y == "*":
        print(round(x * z, 1))
    elif y == "/":
        print(round(x / z, 1))
    else:
        print("Incorrect input format.")

