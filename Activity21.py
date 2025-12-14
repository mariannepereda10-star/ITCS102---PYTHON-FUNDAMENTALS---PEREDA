name = input("What is your name? ")
print(f"Welcome to Washing Machine Logic, {name}")
print("+++++++++++++++++++++++++++++++++++++++++++++")

madumi = True 

while madumi == True:
    confirm = input("Do you want to continue washing (Yes/No) ").lower()

    if confirm == 'yes':
        print("CONTINUING THE CYCLE... ")
        continue
    
    elif confirm == 'no':
        print("CYCLE STOPS")
        break
    else:
        print("Invalid choice...")
        continue
