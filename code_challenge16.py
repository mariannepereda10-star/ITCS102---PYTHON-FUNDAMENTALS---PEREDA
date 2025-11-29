import os
import json
os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("---------------------------------------")

student_records = {}

while True:
    print("SELECT FROM THE OPTION BELOW \nA - Add information\nB - Print a Record\nC - Search a record\nD - Modify a record\nE - Edit a record\nF - Export a record\nG - Import a record\nH - Exit  ")

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
                print("\n\nNo Record found")
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
            else:
                print("===============================")
                print("\n\nNo Record found")
                print("===============================")
            break
        continue

    elif choice == 'e':
        os.system('cls')
        print("EDIT / MODIFY STUDENT RECORD")
        print(" ======================================= ")

        search_id = input("Input ID to search ----> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("===============================")
                print("\n\nRecord found")
                print("===============================")
                for i in student_records[search_id]:
                        print(f"--{i}")

                first_name = input("Input new student first name ---> ").upper()
                last_name = input("Input new student last name ---> ").upper()
                course = input("Input new student course ---> ").upper()
                email = input("Input new student email address ---> ")

                student_records[search_id][0] = first_name
                student_records[search_id][1] = last_name
                student_records[search_id][2] = course
                student_records[search_id][3] = email

                print("DATA UPDATED")
                continue

            else:
                print("===============================")
                print("\n\nNo Record found")
                print("===============================")
                
                
    elif choice == 'f':
        os.system('cls')
        print("Export Student Record")

        with open('student_record.json', 'w') as new_file:
            json.dump(student_records, new_file, indent=4)
        
        print("DATA EXPORTED TO JSON")

        continue

    elif choice == 'g':
        os.system('cls')
        print("Important Student Record")

        with open("student_record.json", "r") as new_file:
            student_json = json.load(new_file)

        student_records = student_json
        print("DATA IMPORTED TO JSON")

        continue

    elif choice == 'h':
        print("Exit")
        break