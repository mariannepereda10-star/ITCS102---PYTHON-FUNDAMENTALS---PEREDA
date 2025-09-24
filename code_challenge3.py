name = input("Enter your name: ")
print("Welcome to Fazebuk", name)
user_name = 'Marianne_ly'
password = '5555'
user = input("Please enter your username: ")
pw = input("Please enter your password: ")

if user == user_name and pw == password:
    print("Access Granted" , "\nWelcome",user_name,"!")
else:
    print("Access Denied", "\nPlease try again.")