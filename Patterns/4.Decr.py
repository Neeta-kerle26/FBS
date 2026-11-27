
# Left alingnment (Decrement Pattern)
#Ex:1
for i in range (1,6):
    for j in range (1, 7 - i):
        print('*', end = ' ')
    print()


# Right alignment (DecrementPattern)
#Ex:2
for i in range(1,6):
    for j in range(1,i+1):
        print ('-', end =' ')
    for j in range(1,7-i):
        print('*', end =' ')
    print()

#Ex:3
for i in range(1,6):
    for j in range(1,i): #NOTE:- this iteration is used to reduce extra column
        print ('-', end =' ')
    for j in range(1,7-i):
        print('*', end =' ')
    print()

