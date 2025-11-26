import os

os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("---------------------------------------")

student_records = {}

while True:
    print("SELECT FROM THE OPTION BELOW \nA- Add information\nB-Print a Record\nC- Search a record\nD-modify a record\nE-Exit  ")

    choice = input("Your choice     ---> ").lower()
    
    if choice == 'a':
        os.system('cls')
        print("Adding student information")
        print("++++++++++++++++++++++")
        student_id = input("Key search for this student use this pattern(course - IDNO) ---> ")

        first_name = input("Input student first name ---> ").upper()
        last_name = input("Input student last name ---> ").upper()
        course = input("Input student course ---> ").upper()
        email = input("Input student email address ---> ").upper()

        #adding record in the dictionary
        student_records[student_id] = [first_name,last_name,course,email]
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'b':
        print("Print student record")

        for id,records in student_records.items():
            print(f"Student id {id} in student records {records}")
            continue

    elif choice == 'c':
        print("Search student record")
        print("==============================")

        search_id = input("Input id to search --->")

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("===============================")
                print("\n\nRecord found")
                print("===============================")
                for i in student_records[search_id]:
                        print(f"-{i}")

            else:
                print("===============================")
                print("\n\nRecord found")
                print("===============================")

        continue
    elif choice == 'd':
        os.system('cls')
        print("Delete student record")
        print("++++++++++++++++++++++++++++++++++++++")

        search_id = input("Input id to search --->")

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("===============================")
                print("\n\nRecord found")
                print("===============================")
                for i in student_records[search_id]:
                        print(f"--{i}")
                student_records.pop(search_id)
                print("Record deleted")     
            else   


