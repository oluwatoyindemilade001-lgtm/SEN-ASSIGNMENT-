students = []

def add_student():
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    department = input("Enter department: ")

    student = {
        "name": name,
        "matric": matric,
        "department": department
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students available.\n")
        return

    for student in students:
        print("Name:", student["name"])
        print("Matric:", student["matric"])
        print("Department:", student["department"])
        print("----------------------")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")
