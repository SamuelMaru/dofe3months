with open("temp_in_C.txt","a") as writer, open("temp_in_F.txt","r") as reader:
    data = reader.read().split("\n")
    for i in data:
        writer.write(str((float(i)-32)*(5/9))+"\n")
    writer.close()
    reader.close()
    print("done")

