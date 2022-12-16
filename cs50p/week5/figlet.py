import sys
import Figlet
if len(sys.argv)>3:
    sys.exit("Too many arguements")
elif sys.argv[1]=="font":
    print("hello",sys.argv[2])
    f = Figlet(font=sys.argv[2])
else:
    print("Bad input")
text = input("Input")
print(f.renderText(text))