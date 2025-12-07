# Employee Bonus

years = int(input("Enter years of service: "))

if years > 10:
    bonus = 0.10
elif years >= 6:
    bonus = 0.08
else:
    bonus = 0.05

print("Bonus =", bonus * 100, "%")

