import random
import os

#-------------------------Varibales----------------------

rightNumber = 0
correctGusses = 0
wrongGusses = 0
max = 1000

#------------------------Functions---------------------
def Intro():
    os.system('cls')
    print("----------------------------------------")
    print("Welcome to the gameeeee Lower Or Higher!")
    print("________________________________________")
    playerInput = input("Number you put in is: ")
    print("You puted 3 LOWER!")
    playerInput = input("Number you put in is: ")
    print("You puted 1 Higher!")
    playerInput = input("Number you put in is: ")

    if(playerInput != 2):
        print("How you could fail that lets say it was a bug and your awnswer was 2!")
    else:
        print("Nice!")
    Level = 0
    os.system('cls')

def Game():
    global correctGusses
    global wrongGusses

    print("------------------------")
    try: playerInput = int(input("Number: "))
    except ValueError:
        print("Only numbers!")
        os.system('cls')
        return
    if(playerInput == rightNumber):
        print("Nice!")
    while(playerInput != rightNumber):
        print("------------------------")
        if(rightNumber < playerInput):
            wrongGusses += 1
            print("Lower!")
        elif(rightNumber > playerInput):
            wrongGusses += 1
            print("Higher!")
        print("------------------------")
        try: playerInput = int(input("Number: "))
        except ValueError:
            print("Only numbers!")
            os.system('cls')
            return
        if(playerInput == rightNumber):
            correctGusses += 1
            os.system('cls')
            print("+1")
            print("Correct!!!")


#----------------------------Game--------------------------
Intro()
while(True):
    rightNumber = random.randint(0,max)
    print("------------------------")
    print("Correct gusses:",correctGusses,"\nWrong gusses:",wrongGusses,)
    Game()