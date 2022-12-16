import sys

def is_valid(arg):
    if ".py" not in arg:
        sys.exit("Invalid file type: not a python file")
    if len(arg) > 2:
        sys.exit("Too many arguments")
    elif len(arg)<2:
        sys.exit("Too few arguments")
    return True

def lines(filename):
    lines = []
    try:
        file = open(filename,"r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    return lines

def linelen(lines):
    num = 0
    for i in lines:
        line = line.strip()
        if len(line)>0 and line[0] != "#":
            num +=1

    return num


if is_valid(sys.argv):
    print(linelen(lines(sys.argv[1])))

else:
    pass
