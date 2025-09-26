name = input("Please enter your name:")
print("Welcome to Ascending or Descending Order",name)

wnt = input("Choose (Ascending or Descending):" )

if wnt.lower() == "ascending":
    for x in range(1, 21):
        print(x)
elif wnt.lower() == "descending":
    for x in range(20, 0, -1):
        print(x)
else:
    print("Try again.")      
    