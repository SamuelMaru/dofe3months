def sort_with_loop(nums):
    num_list = []
    for i in (nums):
        num_list.append(i ** 2)
    return sorted(num_list)

def sort_with_lc(nums):
    return ([(ele ** 2) for ele in sorted(nums)])

print(sort_with_loop([4,-2,5,7,-12,1]))

def summation(x1,x2,x3,w1=0.95,w2=-0.7,w3=0.65):
    return 0<(x1*w1) + (x2*w2) + (x3*w3)
print(summation(3,7,3))

def recurring(inputt):
    list_new = []
    for i in list(inputt):
        if i in list_new:
            return i
        else:
            list_new.append(i)
    return None

import random
count = 0
chosen_num = random.randint(1,100)
guess = -1
print(chosen_num)
while guess != chosen_num:
    count+=1
    guess = int(input("Guess the number between 1 and 100: "))
print(str(guess)+ " Is the correct answer!\n"+"That took "+str(count)+" attempts.")

def odd(n):
    sum = 0
    for i in range(n):
        if (i % 2) != 0:
            sum +=i
    sum+=n
    return sum
print(odd(90))

def sort_with_loop(nums):
    num_list = []
    for i in (nums):
        num_list.append(i ** 2)
    return sorted(num_list)