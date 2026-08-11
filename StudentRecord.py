students = []
while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student Record")
    print("2. View Student Records")
    print("3. Search Student Record")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        mark1 = float(input("Enter marks in Python: "))
        mark2 = float(input("Enter marks in Java: "))
        mark3 = float(input("Enter marks in C: "))
        total = mark1 + mark2 + mark3
        average = total / 3
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"
        student = {
            "Roll Number": roll_no,
            "Name": name,
            "Python": mark1,
            "Java": mark2,
            "C": mark3,
            "Total": total,
            "Average": average,
            "Grade": grade
        }
        students.append(student)
        print("Student record added successfully.")
    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n===== STUDENT RECORDS =====")
            for student in students:
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Python:", student["Python"])
                print("Java:", student["Java"])
                print("C:", student["C"])
                print("Total:", student["Total"])
                print("Average:", round(student["Average"], 2))
                print("Grade:", student["Grade"])
                print("----------------------------")
    elif choice == 3:
        roll_no = int(input("Enter Roll Number to search: "))
        found = False
        for student in students:
            if student["Roll Number"] == roll_no:
                print("\n===== RECORD FOUND =====")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Total:", student["Total"])
                print("Average:", round(student["Average"], 2))
                print("Grade:", student["Grade"])
                found = True
                break
        if not found:
            print("Student record not found.")
    elif choice == 4:
        roll_no = int(input("Enter Roll Number to update: "))
        found = False
        for student in students:
            if student["Roll Number"] == roll_no:
                student["Name"] = input("Enter new name: ")

                student["Python"] = float(
                    input("Enter new Python marks: ")
                )
                student["Java"] = float(
                    input("Enter new Java marks: ")
                )
                student["C"] = float(
                    input("Enter new C marks: ")
                )
                student["Total"] = (
                    student["Python"]
                    + student["Java"]
                    + student["C"]
                )
                student["Average"] = student["Total"] / 3
                if student["Average"] >= 90:
                    student["Grade"] = "A"
                elif student["Average"] >= 75:
                    student["Grade"] = "B"
                elif student["Average"] >= 60:
                    student["Grade"] = "C"
                elif student["Average"] >= 40:
                    student["Grade"] = "D"
                else:
                    student["Grade"] = "F"
                print("Student record updated successfully.")
                found = True
                break
        if not found:
            print("Student record not found.")
    elif choice == 5:
        roll_no = int(input("Enter Roll Number to delete: "))
        found = False
        for student in students:
            if student["Roll Number"] == roll_no:
                students.remove(student)
                print("Student record deleted successfully.")
                found = True
                break
        if not found:
            print("Student record not found.")
    elif choice == 6:
        print("Thank you for using the Student Record Management System.")
        break
    else:
        print("Invalid choice. Please try again.")