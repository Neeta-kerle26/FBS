# #pass: neglect the expected indented block error
# for i in range(1,10):
#     pass

# #break: terminate the loop
# for i in range(1,6):
#     if(i==4):
#         break
#     print(i)

# #continue: stops current iteration 
# for i in range (1,6):
#     if(i==4):
#         continue
#     print(i)

# #else: else will execute when loop executes succesfully
# for i in range(1,6):
#     if(i == 3):
#         break
#     print(i)
# else: 
#     print('else executed')    
  
    

# num= int(input('enter a number:'))
# for i in range(2,num):
#    if(num % i == 0):
#        print(f'{num} is not prime number')
#        break
# else:
#    print(f'{num} is prime number')

#prime number between 1 to 100
for num in range(1,100):
    if(num > 1):
        for i in range(2, num):
             if ( num % i == 0):
               break
        else:
            print(num, end=' ')      

   