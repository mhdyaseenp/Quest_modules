"""Python Functions - Practical Questions"""
# Beginner to Intermediate Level (Excluding Higher Order Functions)
# This worksheet contains practical lab questions focused on Python functions only. Topics include function
# definition, arguments, return values, default arguments, keyword arguments, variable-length arguments,
# recursion, and small real-world logic problems.
""" Section A - Basic Function Questions"""

# 6 Write a function find_largest(a, b) to return the larger number.
# def find_largest(a, b):
#     if a >b:
#         return a
#     else:
#         return b
# print(find_largest(5,8))


# 7 Write a function check_positive(num) to check whether a number is positive, negative, or zero.
# def find_largest(num):
#     if num>0:
#         return "positive"
#     elif num < 0:
#         return "negative"
#     else:
#         return "Zero"
# print(find_largest(int(input())))

# 8 Write a function multiply(a, b) and call it using user input.
# def mult(a,b):
#     return a*b

# num1=int(input("Enter first num :"))
# num2=int(input("Enter second num :"))
# result=mult(num1,num2)
# print(result)


# 9 Write a function full_name(first, last) that returns the full name.
# def full_name(first, last):
#     return first+" "+last
# st1=input("fisrt name :")
# st2=input("lasat name :")
# res=full_name(st1,st2)
# print(res)


# 10 Write a function calculate_area(length, width) to return the area of a rectangle.
# def calculate_area(length, width):
#     return length * width
# print("area is ",calculate_area(5,10))



"""# Section B - Functions with Return Values"""
# 1 Write a function to return the cube of a number.
# 2 Write a function to return the reverse of a string.
# 3 Write a function to count the number of vowels in a given string.
# 4 Write a function to return the factorial of a number.
# 5 Write a function to return the sum of digits of a number.
# 6 Write a function to return the smallest element in a list.
# 7 Write a function to return the second largest number in a list.
# 8 Write a function to return the number of words in a sentence.
# 9 Write a function to return True if a number is a palindrome, otherwise False.
# 10 Write a function to return the common elements from two lists.
"""# Section C - Arguments Practice"""
# 1 Write a function student_info(name, age, course) and call it using positional arguments.
# 2 Write the same function and call it using keyword arguments.
# 3 Write a function power(base, exp=2) that returns the power of a number using a default argument.
# 4 Write a function discount(price, percent=10) to calculate discounted price.
# 5 Write a function introduce(name, city='Kochi') and test it with and without the city argument.
# 6 Write a function that accepts any number of values using *args and returns their sum.
# 7 Write a function that accepts any number of values using *args and returns the largest one.
# 8 Write a function that accepts user details using **kwargs and prints each key-value pair.
# 9 Write a function bill(item, quantity, price) and calculate total bill.
# 10 Write a function marks_total(*marks) that returns total and average marks.
"""# Section D - String-Based Function Problems"""
# 1 Write a function to check whether a string is a palindrome.
# 2 Write a function to count uppercase and lowercase letters in a string.
# 3 Write a function to remove all spaces from a string.
# 4 Write a function to find the frequency of a given character in a string.
# 5 Write a function to convert the first letter of each word to uppercase.
# 6 Write a function to replace all vowels in a string with '*'.
# 7 Write a function to check whether two strings are anagrams.
# 8 Write a function to return the longest word in a sentence.
# 9 Write a function to count how many times a word appears in a sentence.
# 10 Write a function to split a sentence and return only words with length greater than 4.
"""# Section E - List-Based Function Problems"""
# 1 Write a function to return only even numbers from a list.
# 2 Write a function to return only prime numbers from a list.
# 3 Write a function to remove duplicates from a list without changing the order.
# 4 Write a function to return the sum of all odd numbers in a list.
# 5 Write a function to find the index positions of a given element in a list.
# 6 Write a function to merge two lists and return a sorted result.
# 7 Write a function to count positive and negative numbers in a list.
# 8 Write a function to return the maximum difference between two elements in a list.
# 9 Write a function to rotate a list to the right by one position.
# 10 Write a function to return a new list containing squares of all elements.
"""# Section F - Number Logic Function Problems"""
# 1 Write a function to check whether a number is prime.
# 2 Write a function to generate the Fibonacci series up to n terms.
# 3 Write a function to check whether a number is an Armstrong number.
# 4 Write a function to return all divisors of a number.
# 5 Write a function to find the GCD of two numbers.
# 6 Write a function to find the LCM of two numbers.
# 7 Write a function to convert a decimal number to binary.
# 8 Write a function to count the number of digits in an integer.
# 9 Write a function to check whether a number is a perfect number.
# 10 Write a function to return the multiplication table of a number.
"""# Section G - Recursion (Without Higher Order Functions)"""
# 1 Write a recursive function to find the factorial of a number.
# 2 Write a recursive function to calculate the sum of first n natural numbers.
# 3 Write a recursive function to print numbers from 1 to n.
# 4 Write a recursive function to reverse a string.
# 5 Write a recursive function to find the nth Fibonacci number.
# 6 Write a recursive function to calculate the power of a number.
# 7 Write a recursive function to count digits in a number.
# 8 Write a recursive function to check whether a string is a palindrome.
# 9 Write a recursive function to find the sum of digits of a number.
# 10 Write a recursive function to find the product of elements in a list.
"""# Section H - Mini Real-World Function Tasks"""
# 1 Write a function to calculate electricity bill based on units consumed.
# 2 Write a function to calculate employee salary after bonus deduction/tax.
# 3 Write a function to calculate student grade from marks.
# 4 Write a function to check login using username and password.
# 5 Write a function to generate a simple receipt for purchased items.
# 6 Write a function to calculate simple interest and compound interest.
# 7 Write a function to validate whether a mobile number is valid.
# 8 Write a function to check password strength.
# 9 Write a function to calculate age from birth year.
# 10 Write a function to simulate an ATM withdrawal check (balance vs withdrawal amount).
"""# Section I - Lab Exam Style Questions"""
# 1 Write a menu-driven program using functions for basic calculator operations.
# 2 Write a program with separate functions to input, process, and display student details.
# 3 Write a function to take a list of numbers and return both the largest and smallest.
# 4 Write a function to accept a sentence and return the number of vowels, consonants, and spaces.
# 5 Write a function to accept marks of 5 subjects and return total, average, and grade.
# 6 Write a function to accept a number and print whether it is prime, palindrome, and Armstrong.
# 7 Write a function to manage a simple contact list (add, search, display).
# 8 Write a function-based program to count how many even and odd numbers are in a list.
# 9 Write a function to simulate a shopping cart total with discount calculation.
# 10 Write a function to accept a matrix (list of lists) and print row-wise sums.
"""# Bonus Challenge Questions"""
# 1 Create a library of utility functions for numbers, strings, and lists in one Python file.
# 2 Build a student result system using functions only.
# 3 Create a bank menu program using functions for deposit, withdraw, and balance check.
# 4 Create a quiz game where each task is handled by a separate function.
# 5 Build a small text-based calculator app using reusable functions.
# Tip for Students: Try solving each question first without looking at old code. Focus on function design, input
# handling, return values, and clean logic.
