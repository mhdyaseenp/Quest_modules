"""while loop"""

# syntax:-
# while condition:
#     body
#     increment/ decrement


# i=0
# while i<=20:
#     print("yaseen")
#     i+=1


# print 1-20
# i=0
# while i<=20:
#     # i+=1
#     print(i)
#     i+=1


# print even numbers
# i=0
# while i<=20 :
#     print(i)
#     i+=2


# sum of 1st 10 dig
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)
    

# print reverse 
# i=20
# while i>=0:
#     print(i)
#     i-=1


# how many 3s multiples in an user entered number eg input 10 output 3
# num=int(input("Enter a number :"))
# x=0
# count=0
# while x<=num:
#     if x%3==0:
#         count+=1
#     x+=1
#     print(count)

# while x<=num:
#     count+=1
#     print(count)
#     x+=3


# multiplication table of 2
# num=2
# i=1
# while i<=10:
#     # print(i,"*",num, "=",i*num)
#     print(f"{i}x2 = {i*2}")
#     i+=1

# user input multiplication table
# num=int(input("Enter a number :"))
# i=1 
# while i<=10:
#     print(f"{i}x{num} = {i*num}")
#     i+=1
    
# reverse an given number 123 -> 321
# num=123
# reverse=0
# while num<0:
#     dig=num%10
#     reverse=reverse*10+dig
#     num=num//10
#     print(reverse)




"""FOR LOOP"""

# name="yaseen"
# for char in name:
#     print(char)


# for i in range(20):
#     print(i)

# Diffrence b/w for and while

# i=0                 for i in range(10):
# while i<10:             print(i)
#     print(i)
#     i+=1


# Range
# syntax:-
        # range(start,stop,step)

        # stop start will be 0

# for i in range(10):
# for i in range(15):
#     print(i)

        # start and stop

# for x in range(0,11):
# for x in range(4,11):
#     print(x)

        # start,stop and step

# for x in range(0,11,1):    
# for x in range(0,11,2):    even numbers
# for x in range(1,11,2):    odd numbers
# for x in range(0,100,3):   miltiple of 3
# for x in range(0,100,5):   
#     print(x)


# for y in range(11,-1,-1):
# for y in range(0,10,-1):
#     print(y)


# sum of 1st 10 dig
# product=0
# for i in range(1,11):
#     product+=i
# print(product) 

# multiplication table of 2

# for i in range(1,11): 
#     print(f"{i}x2 = {i*2}")

# num=int(input("Enter a number :"))
# for i in range(1,11):
#     print(f"{i}x{num}={i*num}")



"""Nested Loops"""


# for i in range(1,4):
#     for j in range(1,3):
#         print(i,j)

# for i in range(1,4):
#     for j in range(i):
#         print(j,end="")
#     print()

# row=5
# for i in range(row):
#     for j in range(row):
#         print("*",end=" ")
#     print()
    
# print rectange

# length=4
# bredth=3
# for i in range(bredth):
#     for j in range(length):
#         print("*",end=" ")
#     print()


# n=6
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==1 or row==n or col==1 or col==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()

# row=4
# col=4
# for i in range(row):
#     for j in range(col):
#         print(i,end=" ")
#     print()