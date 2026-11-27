num = int(input("Enter a three digit number: "))

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10

rev = (a * 100) + (b * 10) + c

print("Reversed number:", rev)