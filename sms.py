students = []

def add_student():
    student = {}
    student['id'] = input("Enter Student ID: ")
    student['name'] = input("Enter Student Name: ")
    student['age'] = input("Enter Student Age: ")
    student['grade'] = input("Enter Student Grade: ")
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
    print()

def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s['id'] == sid:
            print(f"Found -> ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}\n")
            return
    print("Student not found.\n")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for i, s in enumerate(students):
        if s['id'] == sid:
            del students[i]
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")

def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s['id'] == sid:
            s['name'] = input("Enter new name: ")
            s['age'] = input("Enter new age: ")
            s['grade'] = input("Enter new grade: ")
            print("Student updated successfully.\n")
            return
    print("Student not found.\n")

def menu():
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
