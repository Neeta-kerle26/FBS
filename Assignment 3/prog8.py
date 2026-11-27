# Generate a four-digit random number like CAPTCHA.
# Logic:
# 1. Accept user ID and password.
# 2. Verify the credentials.
# 3. Generate a random four-digit number.
# 4. Ask the user to enter that number.
# 5. Compare both numbers.
# 6. Display success or failure.
# Code:



import random

userid = input("Enter user ID: ")
password = input("Enter password: ")

if userid == "admin" and password == "12345":

    captcha = random.randint(1000, 9999)
    print("Your CAPTCHA is:", captcha)

    user_captcha = int(input("Enter CAPTCHA: "))

    if user_captcha == captcha:
        print("Login successful")
    else:
        print("CAPTCHA failed")
else:
    print("Invalid user ID or password")