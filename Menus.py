import time
import os
import platform

if(platform.system()=='Windows'):
	BORRAR='cls'
else:
	BORRAR='clear'

def printMenuInicial():
    print("***********************")
    print("***  Welcome back!  ***")
    print("***********************")
    print("1. Log in")
    print("2. Register")
    print("3. Exit")

def validarInputMenuInicial(userInput):
    try:
        userInput=int(userInput)
        if(1<=userInput<=3):
            return 1
        else:
            print('Invalid Option!')
            time.sleep(1)
            return 0
    except:
        print('Invalid Option!')
        time.sleep(1)
        return 0

def validarInputHome(userInput):
    try:
        userInput=int(userInput)
        if(1<=userInput<=5):
            return 1
        else:
            print('Invalid Option!')
            time.sleep(1)
            return 0
    except:
        print('Invalid Option!')
        time.sleep(1)
        return 0

def printMenuLogIn():
    print("***************")
    print("***  Login  ***")
    print("***************")
    user=input("Enter your user name: ")
    password=input("Enter your password: ")
    return user,password

def printHomeMenu():
    print("*******************")
    print("***  Main Menu  ***")
    print("*******************")
    print()
    #print("[*] Nuevo mensaje de Jorge")
    print("")
    print("1. Show all users")
    print("2. Add user")
    print("3. Inbox")
    print("4. Delete account")
    print("5. Exit")

def printMenuRegister():
    while 1:
        print("**************************")
        print("***  Register Account  ***")
        print("**************************")
        user=input("Enter your user name: ")
        password=input("Enter your password: ")
        confirmPassword=input("Confirm your password: ")
        if('@' not in user):
            print('User without domain!')
        if(password != confirmPassword):
            print('Passwords do not match!')
        if(('@' in user) and (password==confirmPassword)):
            print('Todo bien')
            return user,password

        print(user)
        print(password)
        print(confirmPassword)
        time.sleep(2)
        os.system(BORRAR)