def add(a,b):
    return a+b


def reversee(st):
    return st[::-1]

def integerRev(n):
    ss=str(n)
    rev=ss[::-1]
    
    nn=int(rev)
    return nn


# def integerRev(n):
#     reversedd=0
#     while n>0:
#         dig=n%10
#         reversedd=reversedd*10+dig
#         n=n//10
#     return reversedd
# print(integerRev(11267))




def NegativeintegerRev(n):
    reversedd=0
    while n>0:
        dig=n%10
        reversedd=reversedd*10+dig
        n=n//10
    return -(reversedd)

# print(NegativeintegerRev(83))

def div(a,b):
    return a/b

# print(div(-10,-5))






def get_data():
    None