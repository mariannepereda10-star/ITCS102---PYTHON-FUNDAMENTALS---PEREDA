from Activity25_1 import *

name  = input("What is your name: ")

print(f"Welcome {name} to my File compiler")

ely = True

while ely == True:
    print("Select a program")
    print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activigty 4\nE - Exit")

    cute = input("What program would you like to run: ").lower()

    if cute == "a":
        Activity1()
        continue
    elif cute == "b":
        Activity2()
        continue
    elif cute == "c":
        Activity3()
        continue
    elif cute == "d":
        Activity4()
    elif cute == "e":
        print("Exit... ")
        break
    else:
        print("try again...")
