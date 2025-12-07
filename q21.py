# 21. ATM System

is_valid = True
balance = 50000
correct_pin = 123

pin = int(input("Enter PIN: "))

if pin == correct_pin:
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = int(input("Enter amount: "))
        balance -= amt
        print("Withdrawn. New balance =", balance)

    elif choice == 2:
        print("Balance =", balance)

    elif choice == 3:
        print("Thank you for visiting")

    else:
        print("Invalid Option")
else:
    print("Wrong PIN")
