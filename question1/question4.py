# Movie Ticket System

age = int(input("Enter age: "))
has_card = input("Membership card? (yes/no): ").lower() == "yes"

if age < 12:
    print("Ticket = Free")
else:
    if age <= 60:
        if has_card:
            print("Ticket = 150")
        else:
            print("Ticket = 200")
    else:
        print("Ticket = 100")
