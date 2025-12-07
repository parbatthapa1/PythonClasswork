# Marks, Percentage, Grade

a = int(input())
b = int(input())
c = int(input())
d = int(input())

total = a + b + c + d
percent = total / 4

print("Total =", total)
print("Percent =", percent)

if percent > 70: print("Distinction")
elif percent > 60: print("First Division")
elif percent > 40: print("Pass")
else: print("Fail")

