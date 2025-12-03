# Lift Movement

current = 5
press = int(input("Enter floor: "))

if press > current:
    print("Lift going UP")
elif press < current:
    print("Lift going DOWN")
else:
    print("Lift stays")

