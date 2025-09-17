print("MULTIPLICATION TABLE MAKER")
num = int(input("Enter a number: "))
print("Multiplication table for", num, ": ")

for cote in range(1, 11):
    result = num * cote
    print(num ,"*", cote, "=",result)