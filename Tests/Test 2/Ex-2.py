num = int (input('Enter a number:'))

first = num// 100
second = (num //10)%10
third = num %10

if first == second*2 and first == third/2:
    print("yes,you have done it")
else:
    print("Please try next time")