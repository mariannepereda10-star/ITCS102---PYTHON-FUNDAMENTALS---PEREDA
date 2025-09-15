total = 0
for kyut in range(1, 11,1): 
    number = eval(input("Enter a number: "))
    if number % 2:
        total += number
print("The sum of all odd number is",total) 