mari = []
anne = ""

print(" --ANIME TITLES COLLECTOR!-- ")
print("Type 'exit' to finish collecting. \n")

while anne != "exit":
    
    anne = input("Enter an anime name (or type 'exit' to finish collecting): ")
    
    if anne != "exit":
        mari.append(anne)
        print(f"'{anne}' has been added to your anime list.")

print("\n--- DONE COLLECTING ---")

print("Your Favorite Anime List:")
for title in mari:
    print(f"- {title}")
    