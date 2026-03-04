# a number divisible by 5 , 3 and the both
# num = int(input("enter a number :"))
# num1=num%3==0
# num2=num%5==0
# num3=num%5==0 and num%3==0
# print("The number is divisible by 3",num1)
# print("The number is divisible by 5",num2)
# print("The number is divisible by both",num3)
# print(num%3==0 or num%5==0)



# password=input("Enter your pass :")
# l=len(password)
# if l <8:
#     print("nopt a strong password")
# elif l<12:
#     print("intermediat password")
# else:
#     print("strong")

# swapp


# a=30
# b=40
# c=a+b
# a=c-a
# b=c-b
# print("value of a is",a)
# print("value of b is",b)


# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b
# print(b)
# print(a)

# num1=12
# num2=21
# temp=num1
# num1=num2
# num2=temp
# print(num2)
# print(num1)

# num1=10
# num2=22
# num1,num2=num2,num1
# print(num1)
# print(num2)


# square root

# num=int(input("enter a number :")
# print(num**0.5)

# print a digit first no and last no,
# num=1234
# last=num%10
# print(last)
# first=num//1000
# print(first)

# num=21345
# last=num%10
# print(last)
# first=num
# while first >= 10:
#     first//=10
# print(first)

# sum of a given dig

# num=123
# total=0
# while num>0:
#     dig=num%10
#     total+=dig
#     num//=10.  #remove the lasst dig
# print(total)


# amnstrong or not

# num=int(input("Enter an number :"))
# order=len(str(num))
# # print(order)
# sum_of_power=0
# temp = num

# while temp>0:
#     dig=temp%10
#     sum_of_power= sum_of_power + dig**order
#     temp //=10
# if num==sum_of_power:
#     print("armstgrong")
# else:
#     print("not armstgrong")


# num=11
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")

#     else:
#         print("prime")
#         break


# limit = int (input("Enter the limit :"))
# for num in range(2,limit):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)

# limit = int (input("Enter the limit :"))
# for num in range(2,limit):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     # if is_prime:
#     else:
#         print(num)


# reverse an string

# name="yaseen"
# reverse=""
# for char in name:
#     reverse=char+reverse
# print(reverse)


#Write a program to print sum of number
# num=int(input("enter :"))
# i=1
# total=0
# while i<=num:
#     total=total+i
#     i=i+1
# print(total)




"""Pattern Printing"""


# print rectange
#        * * * * 
#        * * * * 
#        * * * * 
# muhammedyaseen@M
# length=4
# bredth=3
# for i in range(bredth):
#     for j in range(length):
#         print("*",end=" ")
#     print()


#        * * * * * * 
#        *         * 
#        *         * 
#        *         * 
#        *         * 
#        * * * * * * 

# n=6
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==1 or row==n or col==1 or col==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()

#        0 0 0 0 
#        1 1 1 1 
#        2 2 2 2 
#        3 3 3 3 
# row=4
# col=4
# for i in range(row):
#     for j in range(col):
#         print(i,end=" ")
#     print()

#        1 2 3 
#        4 5 6 
#        7 8 9 
# row=3
# num=1
# for i in range(row):
#     for j in range(row):
#         print(num,end=" ")
#         num=num+1
        
#     print()


# multiplication  
#        3 6 9 
#        12 15 18 
#        21 24 27 

# row=int(input("Enter your :"))
# num=int(input("Enter mult :"))
# count=1
# for i in range(row):
#     for j in range(row):
#         print(num*count,end=" ")
#         count+=1
#     print()

# row=int(input("Enter your :"))
# for i in range(row+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()


#        1 
#        2 3 
#        4 5 6 

# row=int(input("Enter your :"))
# num=1
# for i in range(row+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()



#       * * * * * 
#       * * * * 
#       * * * 
#       * * 
#       * 

# row=int(input("Enter your :"))
# row=5
# for i in range(row):
#     row-=1
#     for j in range(-1,row):
#         print("*",end=" ")
#     print()

# row=6
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#.          * * * * * 
#.            * * * * 
#.              * * * 
#.                * * 
#.                  * 


# row=5
# for i in range(row):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*",end=" ")
#     print()


#         * 
#       * * 
#     * * * 
#   * * * * 

# for i in range(row,0,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*",end=" ")
#     print()


#       * * * * * 
#       * *   * * 
#       *   *   * 
#       * *   * * 
#       * * * * * 

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==n-1 or i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#           *       * 
#             *   *   
#               *     
#             *   *   
#           *       * 
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#                * 
#              * * * 
#            * * * * * 
#          * * * * * * * 
#        * * * * * * * * * 

# row=5
# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()



#                    *
#                   ***
#                  *****
#                 *******
#                *********
#                 *******
#                  *****
#                   ***
#                    *


# n=5
# for i in range(n):
#         print(" " * (n-i-1) + "*"*(2*i+1))
# for i in range(n-2,-1,-1):
#         print(" "*(n-i-1)+"*"*(2*i+1))
# print()


#               * * * * 
#               * * * 
#               * * 
#               * 
#               * * 
#               * * * 
#               * * * * 
# row=4
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(2,row+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=5hb
# # print upper
# for i in range(n,0,-1):
#     print(" *"*i)
#     # print lower
# for i in range(2,n+1):
#     print(" *"*i)