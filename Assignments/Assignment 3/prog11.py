
ticket = float(input("Enter ticket amount per person: "))

total = 0

for i in range(1, 6):
    age = int(input("Enter age: "))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)
    elif age > 59:
        amount = ticket - (ticket * 50 / 100)
    else:
        amount = ticket

    total = total + amount

print("Total ticket amount:", total)