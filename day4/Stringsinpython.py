import random
import re
adverb_suffixes = ["ly"]
abstract_noun_suffixes = ["ness"]
verb_suffixes = ["able"]
adjective_suffixes = ["able","ible","al","ial","ical","ant","ent","ary","ful","ic","ive","ous","less","y","like","ish","ile","an",""]
suffixes = [adverb_suffixes, abstract_noun_suffixes, verb_suffixes, adjective_suffixes]
thisdict = {
    0: "adverb",
    1: "abstract noun",
    2: "verb",
    3: "adjective"
}
def typeofword(word):
    for i in range(len(suffixes)):
        for j in range(len(suffixes[i])):
            search_word = word[-4:]
            if suffixes[i][j] in search_word:
                return "Possible word types:\n"+thisdict[i]
                break
            else:
                pass
"""

word = input("word:")
r = re.search("ly$", word)
if r:
    print(True)
    
    """

def pswdchk():
    import re
    strong = False
    special_chars = ["<",">","-","/","@","!","~","#","&","?","`"," ",",",":",";","(",")","[","]","*","^",".","?","+","%"]
    while not strong:
        password = input("Password: ")
        if (6 <= len(password) < 32) and (" " not in password) and ((re.search("[A-Z]",password)) != None) and ([ele for ele in special_chars if(ele in password)]):
            strong = True
        else:
            print("Weak Password, please try again.")
    print("Strong Password.")

def pswd_security():
    password = input("Enter password: ")
    choices = [(random.randint(1,len(password)-1)),(random.randint(1,len(password)-1)),(random.randint(1,len(password)-1))]
    choices_check = [""]*3
    correct = True
    for i in range(3):
        print("Enter character",choices[i]+1," in your password: ")
        choices_check[i] = input()
    for i in range(3):
        print(password[int(choices[i])])
        if password[int(choices[i])] == choices_check[i]:
            correct = True
        else:
            correct = False

    if correct == True:
        print("They were all correct")
    else:
        print("Not all were correct")

def pswd_secsys():
    while True:
        pswd_real = "abcd"
        pswd = input("password: ")
        if pswd == pswd_real:
            while True:
                username = input("Username: ")
                if username == "end":
                    quit()
                password = input("Password: ")
                f = open("password_lists.txt", "a")
                f.write("Username: " + username+"\n")
                f.write("Password: " + password+"\n")


