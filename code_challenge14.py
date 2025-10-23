
name = input("What is your name: ")
print("Welcome",name, "!")
print("++++++++++++++++++++++++++++++++++++++++++++")
print("This is Odd number compiler, type '0' to terminate the loop")

sum = 0
no = "" 
el = True

while el == True:
    num = eval(input("\nEnter a number: "))
    if num % 2 == 1:
        print("ODD Detected")
        no += str(num) + "," 
        sum += num
        continue
    elif num == 0: 
        print("The loop stopped")
        break
    else:
        print("Even detected")
        print("Next... ")
        continue
print(f"\nHi, {name}! The total of all odd number: {sum}")
print(f"All odd numbers you input: {no}")
    