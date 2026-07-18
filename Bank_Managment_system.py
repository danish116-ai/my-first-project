# Bank Management System

balance = 0

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("₹", amount, "deposited successfully.")

    elif choice == "2":
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("₹", amount, "withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    elif choice == "3":
        print("Current Balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid Choice!")
