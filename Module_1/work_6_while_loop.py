# while based questions 

# 4.Print the following series:10, 20, 30 … 50
# a=10
# while a<=50:
#     print(a)
#     a=a+10
    

# 5.Print the following series:20, 18, 16 … 2
# num = 20
# while num >= 2:
#     print(num)
#     num -= 2


# 6.Write a program to print sum of first 10 numbers.
# num=10
# total=0
# while num<=10:
#     total=total+num
#     num=num+1
# print(total)


# 7.Write a program to print sum of first 10 Even numbers.
# num=2
# total=0
# count=0
# while count < 10:
#     total=total+num
#     num=num+2
#     count=count+1
# print(total)

# num=int(input())
# i=1
# total=0
# while i<=num:
#     if i%2==0:
#         total=total+i
#     i=i+1
# print(total)

# 8.Write a program to print multiplication table of a number entered from the user.
# num=int(input())
# i=1
# while i<=10:
#     print(f"{i} X {num} = {i*num}")
#     i=i+1

# 9.Write a program to print all even numbers between two intervals.
# start=int(input("start dig"))
# end=int(input("end dig"))
# total=0
# while start<=end:
#     if start%2==0:
#         print(start)
#         total=total+start
#     start=start+1
# print("sum is ",total)


# 10.Write a program to check whether a number is prime or not using while loop
# num=int(input("Enter an number :"))
# i=2
# if num<=1:
#     print("not a prime")
# else:
#     is_prime=True

#     while i<num:
#         if num%i==0:
#             is_prime=False
#             break
#         i=i+1
#     if is_prime:
#         print(" prime")
#     else:
#         print("not prime")


# 11.Factorial of a number
# num=int(input())
# print(num**.5)


# 12.Reverse a number
# num=int(input("Enter an number :"))
# revers=0
# while num>0:
#     dig=num%10
#     revers=revers*10+dig
#     num=num//10
# print("Reverse =",revers)


# 13.check Palindrome or not
# num=int(input("Enter an number :"))
# another=num
# revers=0
# while num>0:
#     dig=num%10
#     revers=revers*10+dig
#     num=num//10
# # print("Reverse =",revers)
# if another==revers:
#     print("Palindrom")
# else:
#     print("NOt Palindrom")


# 14. Check whether a number is armstrong or not
# num=int(input("enter :"))
# order=len(str(num))
# sum_of_power=0
# temp=num
# while temp > 0:
#     dig=temp%10
#     sum_of_power=sum_of_power+dig**order
#     temp=temp//10
# if num==sum_of_power:
#     print("armstron")
# else:
#     print("not armstron")


# 15.Write a program to find the sum of digits of a number from the user. 
# num=int(input("enter :"))
# total=0
# while num>0:
#     dig=num%10
#     total=total+dig
#     num=num//10
# print(total)


# 16.Write a program to print fibonacci series using while loop
# num= int(input("Enter how many terms: "))
# a = 0
# b = 1
# count = 0
# while count < num:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     count += 1

    
# 17.Write a program to accept 10 numbers from the user and display it’s average
# count=0
# totoal=0
# while count<10:
#     num=int(input("Enter number :"))
#     totoal=totoal+num
#     count+=1
# avg=totoal/10
# print(avg)