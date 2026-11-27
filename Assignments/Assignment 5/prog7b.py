
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    term = n ** i
    sum = sum + term

print("Sum =", sum)
