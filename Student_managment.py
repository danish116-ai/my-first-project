students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll_no] = name
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent Records:")
        for roll_no, name in students.items():
            print(f"Roll No: {roll_no}, Name: {name}")

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
