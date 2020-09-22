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
        if(1<=userInput<=69):
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

def printAddUserMenu():
    while 1:
        print("******************")
        print("***  Add User  ***")
        print("******************")
        user=input("Enter user name: ")
 
        if('@' not in user):
            print('User without domain!')
        else:
            return user

        time.sleep(2)
        os.system(BORRAR)

def printSearchContact():
    while 1:
        print("***********************")
        print("***  Search contact  ***")
        print("************************")
        user=input("Enter user name: ")
 
        if('@' not in user):
            print('User without domain!')
        else:
            return user

        time.sleep(2)
        os.system(BORRAR)


def printAllusersMenu():
    print("*****************************")
    print("***  redes2020.xyz Users  ***")
    print("*****************************")

def printMyusersMenu():
    print("*********************")
    print("***  My contacts  ***")
    print("*********************")


def printHomeMenu():
    print("*******************")
    print("***  Main Menu  ***")
    print("*******************")
    print()
    #print("[*] Nuevo mensaje de Jorge")
    print("")
    print("1. Show all users")
    print("2. Add user")
    print("3. Search contact")
    print("4. Inbox")
    print("40. Delete account")
    print("69. Exit")

def printMenuChat(user):
    user=user[:user.find('@')]
    print("*********************")
    print("***  "+user+" Chat  ***")
    print("*********************")

def printInboxMenu(contacts):
    while 1:
        print("********************")
        print("***  Inbox Menu  ***")
        print("********************")
        for i in range(len(contacts)):
            print(f"{i+1}. {contacts[i]}")
        print(f"{len(contacts)+1}. Other")
        print(f"{len(contacts)+2}. Exit")

        userInput=input("Enter option: ")

        try:
            print(userInput)
            if(1<=int(userInput)<=len(contacts)+2):
                print('todo bien')
                if(int(userInput)==len(contacts)+2):
                    return -100, False
                if(int(userInput)==len(contacts)+1):
                    usuario=input('Ingrese el usuario: ')
                    return usuario, True
                return contacts[int(userInput)-1], False
            else:
                print('Invalid input!')
        except:
            print('Only numbers please!')

        time.sleep(2)
        os.system(BORRAR)

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
