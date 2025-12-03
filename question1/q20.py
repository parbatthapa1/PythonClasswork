# Wage Calculation

age = int(input("Enter age: "))
gender = input("Gender (M/F): ").upper()

if age >= 18 and age < 30:
    if gender == "M": print("Wage = 700")
    else: print("Wage = 750")

elif age >= 30 and age <= 40:
    if gender == "M": print("Wage = 800")
    else: print("Wage = 850")
