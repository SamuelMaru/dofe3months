lst = []
i=1
while True:
    try:
        item = str(i)+" "+(input("Item: ").upper())
        lst.append(item)
    except EOFError:
        for j in lst:
            print(j)
        break