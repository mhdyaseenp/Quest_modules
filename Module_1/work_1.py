# Q1-Write a program to input two numbers from the user and print their sum
# num1 = int(input("enter a number"))
# num2 = int(input("enter second number"))
# print("Sum is ",num1+num2)


# Q2-Write a program to input two numbers and display:
#    a) Addition
#    b) Subtraction
#    c) Multiplication
#    d) Division
#    (Perform all operations in one program)
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter second number :"))
# print("a) Adition :",num1+num2,
#       "b) Substraction :",num1-num2,
#       "c) Multiplication :",num1*num2,
#       "d) Division :",num1/num2,)


# Q3. Write a program to input two integers and find their product.
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter second number :"))
# product =num1*num2
# print("The Produt is ",product)


#  Q4-Write a program to input a number and print its square.
# num = int(input("Enter a number :"))
# print("square is",num**2)


# Q5. Write a program to input a number and print its cube.
# num = int(input("Enter a number :"))
# print("Cube is",num**3)


# Q6. Write a program to input the length and breadth of a rectangle and calculate its area.
# length = int(input("Enter the length of the rectangel :"))
# bredth = int(input("Enter the bredth of the rectangel :"))
# print("Area of a rectangle  is",length*bredth)


# Q7. Write a program to input the base and height of a triangle and calculate its area.
# height = int(input("Enter the height of the triangle :"))
# length = int(input("Enter the length of the triangle :"))
# print("Area of a triangle  is",.5*(height*length))


# Q8. Write a program to input the radius of a circle and calculate its area.(Use π = 3.14)
# radus = int(input("Enter the radius of the the cicle :"))
# π = 3.14
# print("Area of circle is",π*radus**2)


# Q9. Write a program to input two numbers and find the difference between them.
# num1 = int(input("enter a number"))
# num2 = int(input("enter second number"))
# print("Diffrence b/w the numbers is ",num1-num2)


# Q10. Write a program to input two numbers and find the average.
# num1 = int(input("enter a number :"))
# num2 = int(input("enter second number :"))
# print("Average of two numbers ",(num1+num2)/2)

# --------------------------------------------------

# =====================
# INTERMEDIATE LEVEL
# =====================

# 11. Write a program to input two numbers and find the remainder using the modulus operator.
# num1 = int(input("enter a number :"))
# num2 = int(input("enter second number :"))
# result=num1%num2
# print("Remainder is ",result)


# 12. Write a program to input two numbers and perform integer division using floor division.
# num1 = int(input("Enter a number :"))
# num2 = int(input("enter second number :"))
# result=num1//num2
# print("Floor is ",result)


# 13. Write a program to input a number of days and convert it into:
    # a) Weeks
    # b) Remaining days
# days=int(input("Enter the days :"))
# weeks=days//7
# re_day=days%7
# print("number od weeks :",weeks," remaining days :",re_day)


# 14. Write a program to input a total amount and number of people, then calculate how much each person should pay.
# amount = int(input("Enter the amount :"))
# people = int(input("Enter the number of people :"))
# result =amount/people
# print("Each person should pay ",result)


# 15. Write a program to input a 3-digit number and calculate the sum of its digits.
#     (Hint: use // and % operators)
# num=int(input("Enter a 3-dig number :"))
# first=num//100
# middle=(num//10)%10
# last=num%10
# total=first+middle+last
# print("Sum is :",total)

# 16. Write a program to input a 3-digit number and reverse the number.
#     Example:
#     Input: 123
#     Output: 321
# num=int(input("Enter a number :"))
# num1=num%10
# num2=(num//10)%10
# num3=num//100
# print(f"{num1}{num2}{num3}")
# print(num1,num2,num3)

#reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
#print(reverse)



# 17. Write a program to input total seconds and convert it into:
#     a) Minutes
#     b) Remaining seconds
# seconds=int(input("Enter the seconds :"))
# minuts=seconds//60
# re_second=seconds%60
# print("MInuts :",minuts," remaining Second :",re_second)


# 18. Write a program to input the total marks of 5 subjects and calculate:
#     a) Total marks
#     b) Average marks
# sub1=int(input("Enter the 1st sub1 :"))
# sub2=int(input("Enter the 2nd sub2 :"))
# sub3=int(input("Enter the 3rd sub3 :"))
# sub4=int(input("Enter the 4th sub4 :"))
# sub5=int(input("Enter the 5th sub5 :"))
# totoal=sub1+sub2+sub3+sub4+sub5
# avg=totoal/5
# print("a) totoal mark ",totoal," avg mark ",avg)


# 19. Write a program to input a number and check whether it is even or odd using the modulus operator.
# num=int(input("Enter a number "))
# even=num%2==0
# odd=num%2==1
# print("number is even",even,  "  number is odd ",odd)


# 20. Write a program to input a number and calculate:
#     a) Square using **
#     b) Cube using **
# num=int(input("Enter a number "))
# square =num**2
# cube =num**3
# print("sqare is ",square," cube is ",cube)
 


                                                                            #  comma seperation 
                                                                            # string concatination using + operators
                                                                            # formated string or f string print(f"hello {name})

# --------------------------------------------------

# =====================
# LOGIC BUILDING TASKS
# =====================

# 21. Write a program to input two numbers and swap them using arithmetic operators (without using a third variable).

# a = input("Enter a number :")
# b = input("Enter the second number :")2
# a,b = b,a
# print("a = ",a)
# print("b = ",b)

12
# 22. Write a program to input the cost price and selling price and calculate the profit or loss amount.
# sellig=int(input("Selling  amount :"))
# cost=int(input("Cost of the product  :"))
# profit=sellig-cost
# print("Profit =",profit)


# 23. Write a program to input salary and calculate:
#     a) 10% HRA
#     b) 5% DA
#     c) Total salar
# salary=int(input("Salary :"))
# hra =salary * 10 / 100
# da = salary * 5 / 100
# total=salary+hra+da
# print(total)


# 24. Write a program to input total distance (in km) and fuel consumed (in liters) and calculate mileage
# km=int(input("Enter km coverd :"))
# fuel=int(input("Fuel in liters :"))
# milage=km/fuel
# print("Avg Milage per liter :",milage)


# 25. Write a program to input a number and calculate the sum of first and last digit.
# num=int(input("Enter an 3 dig number  :"))
# first=num//100
# last=num%10
# total=first+last
# print("Sum is :",total)

