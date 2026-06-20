balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully!")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid Choice!")
 