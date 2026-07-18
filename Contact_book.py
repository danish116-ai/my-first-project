contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        if contacts:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(name, "-", phone)
        else:
            print("No Contacts Found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")

