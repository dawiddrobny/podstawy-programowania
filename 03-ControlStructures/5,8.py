###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111'  # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check PIN")
    print("6. Change PIN")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("PIN is incorrect.")
    elif choice == '6':
        new_pin = input("Enter new PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN has been changed.")
        else:
            print("Invalid PIN. Please enter exactly 4 digits.")
    else:
        print("Invalid option. Please try again.")
