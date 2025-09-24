name = input("What is your name? ")
print("Welcome to Jeepney bus" ,name, "!")

loc = input("Saan bababa (DLL, Bayan): ")
num = int(input("Ilan (1-10): "))
money = eval(input("Magkano yung bayad? "))
pwd = input("Are you PWD, Student, or Senior (Yes/No): ")
total_fare = 13
disc_rate = 0.06
tol = num * total_fare
if pwd.strip().lower() == "yes":
    disc = tol * 0.06
else:
    disc = 0

new_fare = tol - disc
if money >= new_fare:
    change = money - new_fare
    print("\nHello" ,name, "!" "\nLocation:",loc,"\nHow many:",num,"\nPrice:",money,"\nFare:",tol," \nDiscount:",disc,"\nTotal w/wth discount:",new_fare,"\nChange:",change)
else:
    print("\nHello" ,name, "!" "\nLocation:",loc,"\nHow many:",num,"\nPrice:",money,"\nFare:",tol," \nDiscount:",disc,"\nTotal w/wth discount:",new_fare)
    print("Sorry, the payment is insufficient.")
    