lst = []
while True:
    try:
        lst.append(input("Name: "))
    except EOFError:
        break
if len(lst)==1:
    print(f"Adieu, adieu to {lst[0]}")
elif len(lst)==2:
    print(f"Adieu, adieu to {lst[0]} and {lst[1]}")
else:
    print(f"Adieu, adieu to {', '.join(lst[:-1])} and {lst[-1]}")
