num = int(input("Enter a three digit number: "))

original = num

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10

rev = (a * 100) + (b * 10) + c

if original == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")