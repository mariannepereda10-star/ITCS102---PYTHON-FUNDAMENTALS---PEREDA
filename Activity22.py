import os
name = input("What is your name? ")
print(f"Welcome to Guess the number, {name}")
print("++++++++++++++++++++++++++++++++++++++++++++")

import random

print("Let guess the number ")

random = random.randint(1,5)
tries = 0
ely = True

while ely == True:
    num = int(input("Input a number u guess(1-5): "))
    tries += 1
    os.system('cls')
    if num == random:
        print(f"Congrats, {name}, your guess is CORRECT!!!")
        print(f"the number is {num}")
        print(f"only took {tries} tries")
        break

    else:
        print("Incorrect")
        print("Try again...")
        continue
 