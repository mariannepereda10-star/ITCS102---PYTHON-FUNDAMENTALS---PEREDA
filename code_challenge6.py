number = eval(input("Please enter a number: "))
num = 1
for yza in range(number,0,-1):
    num *= yza
print("the factorial of", number ,"is",num)