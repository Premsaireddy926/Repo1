# Student Management System

students = {}

def enroll_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    students[student_id] = {
        'name': name,
        'attendance': [],
        'grades': [],
        'messages': []
    }
    print(f"Student {name} enrolled successfully!")

def mark_attendance():
    student_id = input("Enter student ID: ")
    if student_id in students:
        date = input("Enter date (YYYY-MM-DD): ")
        students[student_id]['attendance'].append(date)
        print("Attendance marked.")
    else:
        print("Student not found.")

def add_grade():
    student_id = input("Enter student ID: ")
    if student_id in students:
        grade = input("Enter grade: ")
        students[student_id]['grades'].append(grade)
        print("Grade added.")
    else:
        print("Student not found.")

def send_message():
    student_id = input("Enter student ID: ")
    if student_id in students:
        message = input("Enter message: ")
        students[student_id]['messages'].append(message)
        print("Message sent.")
    else:
        print("Student not found.")

def view_student_info():
    student_id = input("Enter student ID: ")
    if student_id in students:
        student = students[student_id]
        print(f"\nStudent Name: {student['name']}")
        print(f"Attendance: {student['attendance']}")
        print(f"Grades: {student['grades']}")
        print(f"Messages: {student['messages']}\n")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Enroll Student")
        print("2. Mark Attendance")
        print("3. Add Grade")
        print("4. Send Message")
        print("5. View Student Info")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            enroll_student()
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            add_grade()
        elif choice == '4':
            send_message()
        elif choice == '5':
            view_student_info()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()