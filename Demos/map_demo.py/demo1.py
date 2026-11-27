data = [1,2,3,4,5,6,7,8,9,10]

res = list(map (lambda num : num ** 2,data))

print(res)

def cube(n):
    return n * n* n #n**3

    data = [1,2,3,4,5,6,7,8,9,10]

res = list(map (cube,data))

print(res)


#reduce_demo.py
from functools import reduce

data = 1,2,3,4,5,6,7,8,9,10

print(reduce (lambda x, y: x + y, data))