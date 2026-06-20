books = {}

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        books[book_id] = book_name
        print("Book Added Successfully!")

    elif choice == "2":
        print("\nLibrary Books:")
        for book_id, book_name in books.items():
            print(f"Book ID: {book_id}, Book Name: {book_name}")

    elif choice == "3":
        book_id = input("Enter Book ID to Search: ")
        if book_id in books:
            print("Book Found:", books[book_id])
        else:
            print("Book Not Found!")

    elif choice == "4":
        book_id = input("Enter Book ID to Delete: ")
        if book_id in books:
            del books[book_id]
            print("Book Deleted Successfully!")
        else:
            print("Book Not Found!")

    elif choice == "5":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid Choice!")