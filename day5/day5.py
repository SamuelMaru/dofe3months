import sys
import argparse
def task1():
    print("Platform: "+ str(sys.platform))
    print("Version: " + str(sys.version))
    if "--verbose" in sys.argv:
        print("Path: "+str(" ".join(sys.path)))

def task2():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",action="store_true")
    args = parser.parse_args()
    print(args)
    if args.name:
        print("name flag was used")
    else:
        print("name flag was not used")

def task3():
    print("Platform: " + str(sys.platform))
    print("Version: " + str(sys.version))
    parser = argparse.ArgumentParsr()
    parser.add_argument("--verbose",action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print("Path",sys.path)


def euros_to_pounds():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="missing arguement 'num', please enter an int/float")
    args = parser.parse_args()
    try:
        print(float(args.num)*0.83215)
    except:
        print("Value must be int or float")

euros_to_pounds()

