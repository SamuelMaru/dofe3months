import random
amountdue = random.randint(1,99)
coins = [5,10,25,50]
while amountdue>0:
    try:
        print(f"Amount due: {amountdue}")
        coin = int(input("Insert Coin: "))
        if coin in coins:
            amountdue -= coin
        else:
            raise ValueError
    except ValueError:
        print("Invalid coin")
        continue
print(f"Change owed: {-1*amountdue}")