
a = int(input("Enter a: "))
sum = 0

for i in range(1, 11):
    term = (a ** i) / i
    sum = sum + term

print("Sum =", sum)
