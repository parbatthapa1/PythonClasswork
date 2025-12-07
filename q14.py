w = float(input("Enter Earth weight: "))
p = int(input("Enter planet number: "))

if p == 1: print(w * 0.38)
elif p == 2: print(w * 0.91)
elif p == 3: print(w * 0.38)
elif p == 4: print(w * 2.53)
elif p == 5: print(w * 1.07)
elif p == 6: print(w * 0.89)
elif p == 7: print(w * 1.14)
else:
    print("Invalid planet number")

