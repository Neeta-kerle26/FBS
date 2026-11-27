#demo1
def fun(n):
    print ('Hello Neeta!')
    if(n>1):
        fun (n -1)

fun(5)


#sos
def sos (n):
    if(n<=0):
        return 0
    else:
        return n + sos(n-1)

n= 5
res = sos(n)
print(res)