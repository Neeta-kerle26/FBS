gender=input('Enter gender(M/F):')
age=input('Enter age:')

if(gender== 'M'):
    if(age>="21"):
        print('Boy is eligible for marriagge')
    else:
        print('Boy is not eligible for marriage')

else:
    if(age>="18"):
        print('Girl is eligible for marriage')
    else:
        print('Girl is not eligible')  
    
