name = input("Enter your name:")
print("Welcome to ODD Sum",name)

odd_sum = 0
for cote in range(1, 10):
    num = eval(input(f"{cote} - Enter a number --> "))

    if num % 2 == 1:
        odd_sum += num

print(f"The sum of all the ODD numbers given is {odd_sum}",name)