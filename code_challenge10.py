name = input("Please enter your name:")
print("WELCOME", name, "!")

print(" \t\t *")
for ely in range(1,11, 1):
    for yoj in range(10, ely, -1):
        print(" ", end =' ')
    for yan in range(1, ely, 1):
        print("*", end =' ')
    for elyan in range(1, ely, 1):
        print("*", end =' ') 
    print()           