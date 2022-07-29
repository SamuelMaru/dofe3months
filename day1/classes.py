class Person:
    def __init__(self, name, age, height, likes):
        self.name = name.title()
        self.age = age
        self.height = height
        self.likes = likes
    
    def __str__(self):
        return "{0} is {1} years old.\n{0} is {2}cm tall.\n{0} likes: {3}.".format(self.name, self.age, self.height,self.likes)
    
name = input("Input your name: ")
age = input("Input your age(years): ")
height = input("Input your height(cm): ")
likes = input("List things that you like: ")

tester = Person(name,age,height,likes)
print(tester)