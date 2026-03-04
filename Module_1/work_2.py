# I. Arithmetic & Assignment Operators (1-15)

# 3. Calculate the compound interest for a given principal, rate, and time.
# amount=int(input("Enter your amount :"))
# intrest=int(input("Enter your intrest rate :"))
# time=int(input("Enter the duration :"))
# total=amount*(1+intrest/100)**time
# print("total amount is :",total)


# 4. Write a program to swap two variables using only arithmetic operators ($+$ and $-$).
# a=int(input("Enter a number :"))
# b=int(input("Enter second number :"))
# print(f"before a :{a} b:{b}")
# a=a+b
# b=a-b
# a=a-b
# print(f"After a :{a} b:{b}")


# 5. Demonstrate the difference between / (float division) and // (floor division) using
# positive and negative numbers.
# a=int(input("Enter a number :"))
# b=int(input("Enter second number :"))
# div=a/b
# fdiv=a//b
# print(f"div using float {div} div using floor{fdiv}")


# 6. Find the remainder of $12345$ divided by $67$ using the modulo operator.
# a=123445
# b=67
# c=a%b
# print("remainder is :",c)


# 8. Create a simple "Tip Calculator": Input bill amount and percentage, output the final total.
# amount=int(input("Enter the bill amount :"))
# persentage=int(input("Enter the percentage :"))
# total=(amount*persentage/100)-amount
# print("total amount is :",total)


# 9. Use the += operator to keep a running total of 5 user-input numbers.
# a=int(input("Enter the 1st no :"))
# b=int(input("Enter the 2nd no :"))
# c=int(input("Enter the 3rd no :"))
# d=int(input("Enter the 4th no :"))
# e=int(input("Enter the 5th no :"))
# a+=b
# a+=c
# a+=d
# a+=e
# # total=a+e
# print("total :",a)


# 11. Write a program to convert Celsius to Fahrenheit: $F = (C \times 9/5) + 32$.
# celcios=int(input("Enter digree Celsius :"))
# F = (celcios*1.8) + 32
# print("Fahrenheit :",F)


# 12. Calculate the surface area of a sphere given its radius.
# radius=int(input("Enter the Radius :"))
# pi=3.14
# area=4*pi*radius*radius
# print("SUrface area of speare :",area)


# 13. Implement a program that calculates the BMI (Body Mass Index) based on weight
# (kg) and height (m).
# kg=int(input("Enter your weight :"))
# m=int(input("Enter your height in meter :"))
# bmi=kg/(m*m)
# print("your body bmi is :",bmi)



# Relational & Comparison Operators (16-25)

# 16. Write a program to check if a user-input number is even or odd.
# num=int(input("Enter an number :"))
# even=num%2==0
# odd=num%2==1
# print("Number is Even :",even," NUmber is odd :",odd)



# 17. Compare two strings entered by the user and print which one comes first
# alphabetically.
# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
# if string1 < string2:
#     print(string1, "comes first alphabetically")
# elif string1 > string2:
#     print(string2, "comes first alphabetically")
# else:
#     print("Both strings are equal")


# 22. Check if a number is a perfect square
# num = int(input("Enter a number: "))
# if int(num ** 0.5) ** 2 == num:
#     print("Perfect square")
# else:
#     print("Not a perfect square")


# 23. Find the largest of three numbers
# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# c=int(input("enter therid number :"))
# if a>=b and a>=c:
#     print(f"{a} is largest")
# elif b>=a and b>=c:
#     print(f"{b} is largest")
# else:
#     print(f"{c} is largest")



# 25. Validate triangle using three angles
# a=int(input("Enter first angle :"))
# b=int(input("Enter second angle :"))
# c=int(input("Enter therid angle :"))
# if a+b+c==180 and a>0 and b>0 and c>0:
#     print(f"Valid triangle")
# else:
#     print("Invalid")


# III. Logical Operators (26-35)
# 26. Check if a number is divisible by both 3 and 5.
# num = int(input("enter a number :"))
# num1=num%3==0
# num2=num%5==0
# num3=num%5==0 and num%3==0
# print("The number is divisible by 3",num1)
# print("The number is divisible by 5",num2)
# print("The number is divisible by both",num3)


# 27. Write a program to check if a number is between 10 and 50 (inclusive).
# num = int(input("enter a number :"))
# num1=num>=10 or num<=50
# num2=num<=10 or num>=50
# print("number is inclusive :",num1," Number is not inclusive :",num2)



# 28. Create a login logic: Check if username == "admin" AND password == "1234".
# username = input("Enter username: ")
# password = input("Enter password: ")
# check=username=="admin" and password=="123"
# print("username and password is :",check)


# 29. Use the not operator to reverse a boolean result of a comparison.
# num = int(input("enter a number :"))
# result=num<10
# print("number is less than 10 :",result)
# print("number is less than 10 :",not result)


# 30. Determine if a person is eligible to vote (Age $\ge 18$ AND has a Voter ID).
# age =int (input("enter ypur age :"))
# if age >= 18:
#     print("your eligible for vote ")
# else:
#     print("you are not eligibnle for vote")



# 31. Check if a number is either positive OR even.
# num=int(input("Enter an number :"))
# if num >0:
#     if num%2==0:
#         print(f"{num} is both positive and even")
#     else:
#          print(f"{num} is  positive but not even")
# else:
#     print(f"{num} is negative")



# 32. Demonstrate "Short-circuit evaluation" using and where the first condition is False.


# 33. Write a program that checks if a character is a vowel using the or operator
# vowel=(input("enter the charecter :"))
# if vowel=="a" or vowel=="e" or vowel=="i" or vowel=="o" or vowel=="u":
#     print(f"{vowel} is an vowel")
# else:
#     print(f"{vowel} is not an vowel")


# 34. Check if a number is NOT divisible by 7.
# num=int(input("Enter a number :"))
# if not(num%7==0):
#     print(f"{num} is not divisible by 7")
# else:
#     print(f"{num} is  divisible by 7")


# 35. Combine and, or, and not in a single expression to evaluate a complex condition.
# num = int(input("Enter a number: "))
# if num > 10 and (num % 2 == 0 or not (num % 2 == 1)):
#     print("Condition is True")
# else:
#     print("Condition is False")



# V. Intermediate Logic Building (46-50)

# 46. The Range Checker: Take a number and check if it’s outside the range 100-200.
# num=int(input("Enter a number :"))
# if num<100 or num>200:
#     print(f"{num} is outside the range5 ")
# else:
#     print(f"{num} is with inthe range")


# 47. Quadratic Formula: Solve for $x$ in $ax^2 + bx + c = 0$ using arithmetic operators
# (assume real roots).


# 48. Multiple Comparisons: Write a single expression to check if $a < b < c$ (Chained
# operators).



# 49. Shopping Discount: Apply a 10% discount using *= only if the total is above $500.
# amount=int(input("Enter the bill amount :"))
# if amount>500:
#     amount *= 0.90
# print("Final amount :",amount)


# 50. Bit-like logic with Math: Determine the last digit of a number without using strings.
# num=int(input("Enter an number :"))
# last_dig=num%10
# print(last_dig)