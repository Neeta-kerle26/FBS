# withoput parametert without return value
# def add():
#     a=int(input("enter the numer 1 "))
#     b=int(input("enter the numer 2 "))
#     print(f"Addition= {a+b}")
# add()

# with para without r v

# def add(a,b):
#     print(a+b)

# a=int(input("enter the numer 1 "))
# b=int(input("enter the numer 2 "))
# add(a,b)


#Without para with RV
# def add():
#     a=int(input("enter the numer 1 "))
#     b=int(input("enter the numer 2 "))
#     return a+b
# res=add()
# print(res)

# with para with rv
def add(a,b):
    return a+b

no1=int(input("enter the numer 1 "))
no2=int(input("enter the numer 2 "))
res=add(no1,no2)
print(res)