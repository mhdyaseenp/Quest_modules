# Python Lab Practical Questions: For Loop and Range Function Level:
# Beginner to Intermediate

# 3.  Write a program to print even numbers from 1 to 50.
# for i in range(0,50,2):
#     print(i)


# 4.  Write a program to print odd numbers from 1 to 50.
# for i in range(1,50,2):
#     print(i)


# 6.  Write a program to print the multiplication table of a given number.
# num=int(input("Enter a number :"))
# for i in range(1,11):
#     print(f"{i}x{num}={i*num}")


# 7.  Write a program to find the sum of numbers from 1 to N.
# num=int(input("Enter a number :"))
# product=0
# for i in range(0,num+1):
#     product+=i
# print(product) 


# 8.  Write a program to find the factorial of a number.
# num=int(input("Enter a number :"))
# product=1
# for i in range(1,num+1):
#     product*=i
# print(product) 


# 9.  Write a program to print the square of numbers from 1 to 10.
# for i in range(1,11):
#     print(f"{i}^2 ={i*i}")


# 10. Write a program to print the cube of numbers from 1 to 10.
# for i in range(1,11):
#     print(f"{i}^3 ={i*i*i}")


# 11. Write a program to count numbers from 1 to 100.
# for x in range(1,101):
#     print(x)


# 12. Write a program to print all multiples of 3 between 1 and 50.
# for i in range(0,50,3):
    # print(i)

# for i in range(1,51):
#     if i%3==0:
#         print(i)

# 13. Write a program to print numbers divisible by both 2 and 5 between 1
#     and 100.
# for x in range(1,101):
#     if x%2==0 and x%5==0:
#         print(x)


# 14. Write a program to print characters of a string using a for loop.
# name="yaseen"
# for ch in name:
#     print(ch)


# 15. Write a program to count the number of characters in a string.
# name="yaseen"
# count=0
# for ch in name:
#     count+=1
# print(count)


# 16. Write a program to count vowels in a string.
# name=input("Enter a string :")
# count=0
# for ch in name:
#     if ch in "aeiou":
#         count+=1
# print(count)


# 17. Write a program to print numbers from N to 1.
# num=int(input("Enter an number :"))
# for i in range(num,0,-1):
#     print(i)

# 18. Write a program to find the sum of even numbers from 1 to 100.
# product=0
# for i in range(0,11,2):
#     product+=i
# print(product) 


# 19. Write a program to find the sum of odd numbers from 1 to 100.
# product=0
# for i in range(1,10,2):
#     product+=i
# print(product) 


# 20. Write a program to print the first 10 natural numbers.
# for i in range(1,11):
#     print(i)


# 21. Write a program to print numbers from 1 to 100 with a step of 5.
# for i in range(1,101,5):
#     print(i)


# 22. Write a program to print the following pattern:

# -    **

# 23. Write a program to print the following pattern: 1 12 123 1234 12345


# 24. Write a program to check whether a number is prime or not.
# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Not Prime")
# else:  
#     for i in range(2, num):
#         if num % i == 0:
#             print("not Prime")
#             break
#     else:
#         print(" Prime")
# limit = int (input("Enter the limit :"))
# for num in range(2,limit):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)
# 25. Write a program to print Fibonacci series up to N terms.
