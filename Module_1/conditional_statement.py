#                                    """if Statement"""

# age =int (input("enter ypur age :"))
# if age >= 18:
#     print("your eligible for vote ")


                                #   """if-else Statement"""

# age =int (input("enter ypur age :"))
# if age >= 18:
#     print("your eligible for vote ")
# else:
#     print("you are not eligibnle for vote")


# num=int(input("Enter an number :"))       
# if num%2==0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")


                                    #  """nested-if Statement"""

# num=int(input("Enter an number :"))
# if num >0:
#     if num%2==0:
#         print(f"{num} is both positive and even")
#     else:
#          print(f"{num} is  positive but not even")
# else:
#     print(f"{num} is negative")


# num1=int(input("Enter an number :"))
# num2=int(input("Enter an number :"))
# if num1>num2:
#     print(f"{num1} is largest")
# else:
#     print(f"{num2} is largest")


# mark=int(input("Enter the mark :"))
# if mark>=40:
#     print(f"pass")
# else:
#     print("failed")


# alpebet=input("Anter an alphabet :")
# if alpebet in "aeiou":
#     print(f"{alpebet}  is  vowel")
# else:
#     print(f"{alpebet} is not an vowel")

# year=int(input("enter the year :"))
# if (year%400==0) or (year%4==0 and year%100 != 0) :
#     print(f"{year} is an leapyear")
# else:
#     print(f"{year} is not an leap year")


                                    #  """el-if Statement"""

# age=int(input("Enter your age :"))
# if age<13:
#     print("child")
# elif age <19:
#     print("teen")
# else:
#     print("Adult")




                                # Turnoury conditional operator
# num1=int(input("Enter a number :"))
# print("even " if num1%2==0 else"odd")

# num1=int(input("Enter 1st number :"))
# num2=int(input("Enter 2nd number :"))
# print("num1 is Largest" if num1>num2 else "num2 is largest")

# a=int(input("Enter 1st number :"))
# b=int(input("Enter 2nd number :"))
# c=int(input("Enter 3rd number :"))

# # print(f"{a}a is Largest" if a>=b and a>=c else ("{}b islargest" if b>=a and b>=c else"c is largest") )

# print(f"largest value is a {a}" if a>b and a>c else(f"largest value is b {b}" if b>a and b>c else f"{c} c is largest"))

a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))

if a>b and a>c:
    print(f"{a} is largest")
else:
    if b>a and b>c:
        print(f"{b} is largest")
    else:
        print(f"{c} is largest")