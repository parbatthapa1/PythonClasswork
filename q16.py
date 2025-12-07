# Bike Tax
price = int(input("Enter bike price: "))

if price > 100000:
    tax = 0.15 * price
elif price > 50000:
    tax = 0.10 * price
else:
    tax = 0.05 * price

print("Road tax =", tax)

