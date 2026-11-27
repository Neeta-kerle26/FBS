num=int(input('Enter a number'))
i = 1
while i<= 10:
    print( num * i)
    i += 1

#using 'f' string
num = int(input('enter a number'))
i = 1
while i<= 10:
   # print(num *  i)
    
    print(f'{num} * {i} = {num*i}')
    i+=1
