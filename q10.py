#  10. Greater of two + sign check
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    print("Greater =", a)
elif b > a:
    print("Greater =", b)
else:
    print("Equal")

    if a > 0: print("Positive")
    elif a < 0: print("Negative")
    else: print("Zero")
