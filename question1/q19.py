# ob Eligibility

age = int(input("Enter age: "))

if age >= 18:
    degree = input("Do you have a degree? (yes/no): ").lower() == "yes"
    if degree:
        exp = float(input("Enter years of experience: "))
        if exp > 3:
            print("Highly Eligible")
        elif exp >= 1:
            print("Eligible")
        else:
            print("Under Review")
    else:
        print("Not Eligible (No Degree)")
else:
    print("Not Eligible (Age < 18)")

