name = input("Input your name: ")
age = input("Input your age: ")
height = input("Input your height(cm): ")
print("List three things that you like: ")
likes = []
for i in range(3):
    like = input("List a thing that you like: ")
    likes.append(like)
    
print(name)
print(age)
print(height)
for i in range(3):
    print("Like["+str(i+1)+"]:",likes[i])