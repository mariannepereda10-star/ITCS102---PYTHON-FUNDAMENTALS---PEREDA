
print("Adding data to dictionary")
print(" ============================= ")
tuloy = True 

empty_dictionary = {}

def print_anime():
    for i,j in empty_dictionary.items():
        print(f"CODE {i} TITLE -- {j}")

while tuloy == True:
    keys = input("Input keys for this anime ---> ")

    value = input("Enter anime title ---> ")

    empty_dictionary[keys] = value

    choice = input("Would you like to continue adding anime (y, n, p)" ).lower()

    if choice == 'y':
        print("Continuing... ")
        continue
    elif choice == 'n':
        print("program stops ")
        break
    elif choice == 'p':
        print_anime()
        continue
    else:
        print("invalid choice")
        continue
