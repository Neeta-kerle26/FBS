# Accept five subject marks and display the grade.
# Logic:
# 1. Accept marks of five subjects.
# 2. Calculate total marks.
# 3. Calculate percentage.
# 4. Use if-elif-else to display the grade.
# The assignment does not specify grade boundaries, so we'll use these example criteria:
# - 75% and above: Distinction
# - 60% to below 75%: First class
# - 50% to below 60%: Second class
# - 35% to below 50%: Pass class
# - Below 35%: Fail
# Code:

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
m4 = int(input("Enter subject 4 marks: "))
m5 = int(input("Enter subject 5 marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First class")
elif percentage >= 50:
    print("Second class")