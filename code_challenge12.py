name = input("Enter your name: ")
print(f"Welcome {name}!")

for ely in range(1, 7):  
    for yan in range(7, ely, -1):
        print(" ", end="")
    for rie in range(ely, 0, -1):
        print("•" , end="")
    for yoj in range(2, ely + 1):
        print("•" , end="")
    print()