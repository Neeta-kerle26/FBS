
n = int(input("Enter number of students: "))
total_percentage = 0

for i in range(1, n + 1):
    total = 0

    print("Student", i)

    for j in range(1, 6):
        marks = int(input("Enter subject marks: "))
        total = total + marks

    percentage = total / 5
    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average percentage =", average)
