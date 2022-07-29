def pounds_to_euros(pounds = None):
    """
    converts pounds into euros, £1 = €1.2017
    :param pounds:  int
    :return: euros
    """
    if type(pounds) != int and type(pounds) != float:
        raise ValueError("Invalid type, type must be float or int")
    return pounds*1.2017

def euros_to_pounds(euros = None):
    """
    converts euros into pounds, €1 = £0.83215
    :param pounds:  int
    :return: euros
    """
    if type(euros) != int and type(euros) != float:
        raise ValueError("Invalid type, type must be float or int")
    return euros*0.83215



















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
    import random
    password = input("Enter password: ")
    choices = [(random.randint(0,len(password)-1)),(random.randint(0,len(password)-1)),(random.randint(0,len(password)-1))]
    choices_check = [""]*3
    for i in range(3):
        print("Enter character",choices[i]+1," in your password: ")
        choices_check[i] = input()
        if password[int(choices[i])] == choices_check[i]:
            print("Correct")
        else:
            print("Incorrect")

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

pswd_security()
