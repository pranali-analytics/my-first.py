print("Welcome to the Student Data Organizer!")
students = {}

while True:
    print("\nselect an option:")
    print("1. add student")
    print("2. display all students")
    print("3. update student information")
    print("4. delete student")
    print("5. display subjects offered")
    print("6. exit")
    
    choice = input("enter your choice: ")
    if choice == "1":
        student_id = input("enter student ID:")
        name = input("enter student name:")
        age = input("enter student age:")
        grade = input("enter student grade:")
        dob = input("enter date of birth(YYYY-MM-DD):")
        subjects = input("enter subjects(comma- separated):")
        
        students[student_id] = {
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects.split(",")
        }
        
        
        print("student added successfully!")
    
    elif choice == "2":
        print("--- display all students---")
        
        for student_id, info in students.items():
            print("Student ID:", student_id)
            print("name:", info["name"])
            print("age:", info["age"])
            print("grade:",info["grade"])
            print("date of birth:", info["dob"])
            print("subjects;", info["subjects"])
    elif choice == "3":
        student_id = input("ente student ID to update:")
        if student_id in students:
            print("enter new student details:")
            name = input("enter new name: ")
            age = int(input("enter new age: "))
            grade = input("enter new grade: ")
            dob = input("enter new date of birth: ")
            
            subjects = input("enter new subjects(comma separated):")
            subjects = subjects.split(",")
            
            students[student_id]["name"] = name
            students[student_id]["age"] = age
            students[student_id]["grade"] = grade
            students[student_id]["dob"] = dob
            students[student_id]["subjects"] = subjects
            print("student information updated successfully!")
        else:
            print("student ID not found.")
    elif choice == "4":
        student_id = input("enter student ID to delete:")
        
        if student_id in students:
            del students[student_id]
            print("student deleted successfully!")
        else:
            print("student ID not found.")
    elif choice == "5":
        print("subjects offered:")
        print("1. python")
        print("2. java")
        print("3. c++")
        print("4. web development")
    elif choice == "6":
        print("Exiting student data orgnizer. Goodbye!")
    
    else:
        print("Invalid choice. please try Again.")
        break
        
        
        
    
    
