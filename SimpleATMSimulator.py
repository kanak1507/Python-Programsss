balance = 10000.0

while True:
    print("\n===== ATM MENU =====")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)
    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully.")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid deposit amount.")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
            print("Updated Balance: ₹", balance)
        else:
            print("Insufficient balance.")
    elif choice == 4:
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")
