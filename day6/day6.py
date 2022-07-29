import sys
import argparse
def euros_to_pounds():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="missing arguement 'num', please enter an int/float")
    args = parser.parse_args()
    try:
        print(float(args.num)*0.83215)
    except ValueError:
        print("Value must be int or float")


writer = open("temp_in_C.txt","a")
reader = open("temp_in_F.txt","r")
data = reader.read().split("\n")
for i in data:
    writer.write(str((float(i)-32)*(5/9))+"\n")
writer.close()
reader.close()
print("done")