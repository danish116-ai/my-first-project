expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((item, amount))
        print("Expense Added!")

    elif choice == "2":
        if expenses:
            print("\nExpenses:")
            for item, amount in expenses:
                print(item, "-", amount)
        else:
            print("No expenses found!")

    elif choice == "3":
        total = 0
        for item, amount in expenses:
            total += amount
        print("Total Expense =", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
