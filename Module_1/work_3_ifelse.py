# IF-ELSE PRACTICAL QUESTIONS (Beginner Friendly)


# 1.  Check Even or Odd Write a program to check whether a given number is
#     even or odd.
# num=int(input("Enter an number :"))
# if num%2==0:
#     print("even")
# else :
#     print("odd")


# 2.  Positive, Negative or Zero Write a program to check if a number is
#     positive, negative or zero.
# num=int(input("Enter an number :"))
# if num>0:
#     print("number is positive")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is zero")



# 3.  Find the Largest of Two Numbers Take two numbers from the user and
#     print the larger one.
# num1=int(input("Enter an number :"))
# num2=int(input("Enter an number :"))
# if num1>num2:
#     print(f"{num1} is largest")
# else:
#     print(f"{num2} is largest")



# 4.  Find the Largest of Three Numbers Take three numbers and print the
#     largest among them.
# a=int(input("Enter 1st number"))
# b=int(input("Enter 2nd number"))
# c=int(input("Enter 3rd number"))
# if a>=b and a>=c:
#     print(f"{a} is grater")
# elif b>=a and b>=c:
#     print(f"{b} is grater")
# else:
#     print(f"{c} is grater")



# 5.  Check Eligibility to Vote Ask the user for their age and check if
#     they are eligible to vote (18 or above).
# age =int (input("enter ypur age :"))
# if age >= 18:
#     print("your eligible for vote ")
# else:
#     print("you are not eligibnle for vote")



# 6.  Pass or Fail Ask the user for their mark and print Pass if mark is
#     40 or above, otherwise Fail.
# mark=int(input("Enter the mark :"))
# if mark>=40:
#     print(f"pass")
# else:
#     print("failed")



# 7.  Grade System Input marks and display grade: 90+ : A 80-89 : B 70-79
#     : C 60-69 : D Below 60 : Fail
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



# 8.  Leap Year Checker Input a year and check whether it is a leap year
#     or not.
# year=int(input("enter the year :"))
# if (year%400==0) or (year%4==0 and year%100 != 0) :
#     print(f"{year} is an leapyear")
# else:
#     print(f"{year} is not an leap year")




# 9.  Divisible by 5 and 11 Check whether a number is divisible by both 5
#     and 11.
# num=int(input("Enter a number :"))
# if num%5==0 and num%11==0:
#     print(f"{num} is divisible by both 11 and 5")
# else:
#     print(f"{num} is not divisible by both 11 and 5")



# 10. Check Character Type Input a character and check if it is a vowel or
#     consonant.
# alpebet=input("Anter an alphabet :")
# if alpebet in "aeiou":
#     print(f"{alpebet}  is  vowel")
# else:
#     print(f"{alpebet} is  consonant")



# 11. Simple Login System Ask for username and password. If both are
#     correct, print Login Successful, else Login Failed.
# username="yaseen"
# password="yaseen123"
# u_username=input("Enter your username :")
# p_password=input("Enter your password :")
# if username==u_username and password==p_password:
#     print("Login successfull")
# else:
#     print("Login faild")



# 12. Number Comparison Game Take two numbers. If first is greater print
#     “First is greater”, else print “Second is greater”.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print("First is greater")
# else:
#     print("Second is greater")


# 13. Check Temperature If temperature > 30 print Hot, if between 20 and
#     30 print Warm, else Cold.
# temp=int(input("Enter the tempreature :"))
# if temp>=30:
#     print("hot")
# elif temp >=20:
#     print("warm")
# else:
#     print("cold")



# 14. Check Salary Bonus If salary > 50000, give bonus 5000 else
#     bonus 2000. Print total salary.
# salery=int(input("Enter your sallery :"))
# if salery>50000:
#     salery+=5000
#     print("bonus salery is",salery)
# else:
#     salery+=2000
#     print("bonus salery is",salery)


# 15. Check Shopping Discount If bill amount > 1000, give 10% discount
#     else no discount.
# amount=int(input("Enter the bill amount"))
# if amount>1000:
#     diss=(10/100)*amount
#     amount=amount-diss
#     print(f"finall bill amount is {amount}")
# else:
#     print(f"finall bill amount is {amount}")


# 16. Age Category If age < 13 print Child If age between 13 and 19 print
#     Teen Else print Adult
# age=int(input("Enter your age :"))
# if age<13:
#     print("child")
# elif age <19:
#     print("teen")
# else:
#     print("Adult")


# 17. Electricity Bill Calculator (Simple) If units <= 100 charge 2 per
#     unit If 101-200 charge 3 per unit Above 200 charge 5 per unit
# unit=int(input("Enter your units amount :"))
# if unit<=100:
#     unit=unit*2
#     print(f"bill amount is {unit}")
# elif unit<=200:
#     unit=unit*3
#     print(f"bill amount is {unit}")
# else :
#     unit=unit*5
#     print(f"bill amount is {unit}")


# 18. Check Number is Multiple of 3 or 7 Input a number and check if it is
#     multiple of 3 or 7.
# num=int(input("Enter a number :"))
# if num%3==0 or num%7==0:
#     print("number is multiple of 3 or 7")
# else:
#     print("number not  multiple of 3 or 7")


# 19. Check Password Strength If password length >= 8 print Strong
#     Password else Weak Password.
# password=input("Enter your pass :")
# if len(password)>=8:
#     print("strong password")
# else:
#     print("weak password")


# 20. Find Smallest of Two Numbers Take two numbers and print the smaller
#     one.
# num1=int(input("Enter 1st number :"))
# num2=int(input("Enter 2nd number :"))
# if num1<num2:
#     print(f"{num1} is smaller")
# else:
#     print(f"{num2} is smaller")



