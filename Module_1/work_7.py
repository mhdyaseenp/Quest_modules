# Python Practical Lab Questions (Logic Building & Interview Prep)
"""Phase 1: Basic Logic & Variable Handling"""
# 2. Create a script that takes a user's name and age as input and prints a message telling them
# the year they will turn 100.
# name=input("Enter your Name :")
# age=int(input("Enter your Age :"))
# year=2026+100
# year=year-age
# print(f"Hey {name} you will turn 100 in {year} ")


# 3. Write a program to convert temperature from Celsius to Fahrenheit and vice versa.
# celsius=int(input("Enter digree celsius :"))
# farent=(celsius*1.8)+32
# bac_celsius=(farent-32)*5/9
# print("Temperature in Fahrenheit:", farent)
# print("Temperature in Celsius:", bac_celsius)


# 4. Calculate the area and perimeter of a rectangle where dimensions are provided by the
# user.
# length=int(input("Enter the length :"))
# width=int(input("Enter the width :"))
# area=length*width
# perimeter=2*(length + width)
# print("Area of rectangle is :",area)
# print("Perimeter of rectangle is :",perimeter)


# 5. Write a program to calculate the simple interest based on principal, rate, and time input.
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time (in years): "))
# simple_interest = (principal * rate * time) / 100
# print("Interest is:", simple_interest)


# 6. Create a program that takes a character as input and displays its ASCII value.

# 7. Write a script to calculate the distance between two points (x1, y1) and (x2, y2) using the
# Pythagorean theorem.
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))
# distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
# print("Distance between the two points is:", distance)
\

# 8. Develop a program that accepts an integer 'n' and computes the value of n + nn + nnn
# (e.g., if n=5, result is 5 + 55 + 555).
# num=input("enter a digits :")
# term1=num
# term2=num+num
# term3=num+num+num
# total=int(term1)+int(term2)+int(term3)
# print(total)


# 9. Write a program to extract the last digit of a number (e.g., for 1234, the output should be
# num=109012
# print(num%10)

# 10. Create a program to find the square root of a number without using the math module (use
# the exponent operator).
# num=2
# print(num**2)


"""Phase 2: Operators & Conditional Logic"""

# 11. Write a program to check if a number is even or odd using the modulo operator.
# num=int(input("Enter an number :"))
# if num%2==0:
#     print("even number ")
# else:
#     print("not an even number ")


# 13. Write a program to check if a year is a leap year (consider the century year rule).
# 
# year=2025
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print("leap year ")
# else:
#     print("not a leap year ")


# 14. Create a basic calculator that performs Addition, Subtraction, Multiplication, and
# Division based on user choice.
# num1=110
# num2=20
# adition=num1+num2
# substraction=num1-num2
# multiplication=num1*num2
# division=num1/num2
# print(f"Sum is :{adition} product is :{multiplication} substract is {substraction} divider is :{division}")


# 15. A student’s grade is determined by their score: 90+ (A), 80-89 (B), 70-79 (C), below 70
# (Fail). Write a program using if-elif-else.
# mark=int(input("Enter your mark :"))
# if mark>=90:
#     print("A grade")
# elif mark>=80:
#     print("B grade")
# elif mark>=70:
#     print("C grade")
# elif mark>=60:
#     print("D grade")
# else:
#     print("Fail")

# 16. Write a program to check if a given character is a vowel or a consonant.
# char = input("Enter a charecter :")
# if char in "aeoiuAEIOU":
#     print("vovel")
# else:
#     print("constant")


# 17. Implement a "Login System" where the user has 3 attempts to enter the correct password
# before being locked out.
# correct_password = "1234"
# attempts = 3
# while attempts > 0:
    
#     password = input("Enter password: ")
#     if password == correct_password:
#         print("Login Successful")
#         break
#     else:
#         attempts = attempts-1
#         print("Wrong password")
#         print("Attempts left:", attempts)
# if attempts == 0:
#     print("Account Locked")


# 18. Write a program that checks if a triangle is equilateral, isosceles, or scalene based on its
# side lengths.
# a=int(input("Enter 1st length :"))
# b=int(input("Enter 2nd length :"))
# c=int(input("Enter 3rd length :"))
# if a==b==c :
#     print("Equilateral")
# elif a==b or b==c or c==a:
#     print("Isosceles")
# else:
#     print("Scalene")


# 19. Create a script to check if a given number is a multiple of both 5 and 11.
# num=int(input("Enter the number :"))
# if num%5==0 and num%11==0:
#     print("Multiple of 11 and 5")
# else:
#     print("Not an Multiple of 11 and 5")


# 20. Use a ternary operator to check if a person is eligible to vote (Age >= 18).
# age=22
# print("eligible for vot " if age>=18 else "minor")

"""Phase 3: Loop Structures (While & For)"""

# 21. Write a program to print the first 10 numbers of the Fibonacci sequence using a while
# loop.
# 22. Create a script to find the factorial of a number using a for loop.
# num=4
# print(num**0.5)

# 23. Write a program to reverse a given integer (e.g., 1234 becomes 4321).
# num=1234
# limit=len(str(num))
# reve=0
# for i in range(1,limit+1):
#     dig=num%10
#     reve=reve*10+dig
#     num=num//10
# print(reve)


# 24. Implement a program to check if a number is a Palindrome (reads the same forward and
# backward).
# num=int(input("Enter an number :"))
# limit=len(str(num))
# orginal=num
# reve=0
# for i in range(1,limit+1):
#     dig=num%10
#     reve=reve*10+dig
#     num=num//10
# if orginal==reve:
#     print("palindrom")
# else:
#     print("not palindrom")


# 25. Write a program to check if a number is a Prime number.
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


# 26. Print all prime numbers between 1 and 100.
# if num <= 1:
#     print("Not Prime")
# else:  
#     for i in range(2, num):
#         if num % i == 0:
#             print("not Prime")
#             break
#     else:
#         print(" Prime")


# num=int(input())
# if num<=1:
#     print("not prime")
# else:
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             # print("not prime")
#             break

#     if is_prime:
#         print("prime")
#     # else:
#     #     print("not prime")


# 27. Create a multiplication table (1 to 10) for any number entered by the user.
# num = int(input("Enter a number: "))



# 28. Write a program to find the sum of all digits of a number (e.g., 123 = 1+2+3 = 6).
# num=int(input("Enter an number :"))
# limit=len(str(num))
# total=0
# for i in range(0,limit+1):
#     dig=num%10
#     total=total+dig
#     num=num//10
# print(total)


# 29. Implement a "Guess the Number" game where the loop continues until the user guesses
# the correct secret number.
# num=21
# guss=int(input("Enter your guus :"))
# while guss!=num:
#     print("wrong guss")
#     guss=int(input("Enter your guus :"))
# print("your guss is correct")


# 30. Write a program to count the number of vowels in a string provided by the user.
# text=input("Enter a string :")
# count=""
# for ch in text:
#     if ch in "aeiouAEIOU":
#         count=count+1 
#         # count=count+ch
# # print(len(str(count)))
# print(count)


"""Phase 4: Pattern Printing & Nested Loops"""

# 31. Print a right-angled triangle pattern of stars (*).
# 32. Print an inverted right-angled triangle pattern of stars.
# 33. Print a Pyramid pattern using stars.
# 34. Print a Diamond pattern using stars.
# 35. Create a program to print a 5x5 grid of coordinates (e.g., (0,0) (0,1)...).
# 36. Print a Floyd’s Triangle (consecutive numbers in a triangle format).
# 37. Use nested loops to find and print all "Armstrong Numbers" between 1 and 500.
# 38. Write a program to print a Pascal’s Triangle up to 'n' rows.
# 39. Print a square boundary pattern (stars on the edges, spaces in the middle).
# 40. Write a script that prints a multiplication table from 1 to 5 using nested loops.

# Phase 5: Industrial Logic & Optimization (Interview Style)

# 41. Write a program to find the GCD (Greatest Common Divisor) of two numbers.
# 42. Implement a script to find the LCM (Least Common Multiple) of two numbers.
# 43. Create a program that removes all duplicates from a list (without using set()).
# 44. Write a script to find the second largest number in a list of integers.
# 45. Implement a "FizzBuzz" program: Print numbers 1-50; for multiples of 3 print "Fizz", for
# 5 print "Buzz", and for both print "FizzBuzz".
# 46. Write a program to check if two strings are Anagrams (e.g., "listen" and "silent").
# 47. Create a script to find the frequency of each character in a string.
# 48. Write a program that takes a sentence and reverses each word in its place (e.g., "Hello
# World" -> "olleH dlroW").
# 49. Implement a logic to find the "Perfect Numbers" between 1 and 1000 (a number equal to
# the sum of its divisors).
# 50. Write a program to simulate a simple ATM machine: balance inquiry, deposit, and
# withdrawal (with insufficient balance check).
