# Store Discount

amount = float(input("Enter total amount: "))
is_member = input("Member? (yes/no): ").lower() == "yes"

if amount > 1000:
    if is_member:
        amount -= amount * 0.20
    else:
        amount -= amount * 0.10

print("Final amount:", amount)

