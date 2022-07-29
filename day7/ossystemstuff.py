import datetime
import os
import random

print(os.getcwd())
os.chdir("C:/SAMUEL_FOLDER/DofE/pythonProject")
print(os.getcwd())
if os.path.exists("C:/SAMUEL_FOLDER/DofE/pythonProject/day7/test"):
    raise FileExistsError("Folder already exists.")
os.makedirs("C:/SAMUEL_FOLDER/DofE/pythonProject/day7/test")

os.chdir("C:/SAMUEL_FOLDER/DofE/pythonProject/day7/test")
with open("bytesinfile.txt", "w") as writer:
    writer.write("*"*random.randint(1,100))
print("bytesinfile.txt has "+str(os.path.getsize("bytesinfile.txt"))+" bytes")
print("bytesinfile.txt was last edited at",datetime.datetime.fromtimestamp(os.stat("bytesinfile.txt").st_mtime))
