
correct_id = "admin"
correct_password = "1234"

attempt = 0

while attempt < 3:
    userid = input("Enter user ID: ")
    password = input("Enter password: ")

    if userid == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect ID or Password")
        attempt = attempt + 1

if attempt == 3:
    print("Account Locked")
