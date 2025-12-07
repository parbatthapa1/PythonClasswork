# Check Positive then Even/Odd

n = int(input("Enter number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not Positive")
