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
# def qub(num):
#     return num**3
# print(qub(3))


# 2 Write a function to return the reverse of a string.
# def rev(str):
#     return str[::-1]
# print(rev("yaseen"))


# 3 Write a function to count the number of vowels in a given string.
# def vovel(str):
#     vw="aeiou"
#     couut=0
#     for ch in str:
#         if ch in vw:
#             couut+=1
#     return couut
# print(vovel('yaseen'))


# 4 Write a function to return the factorial of a number.
# def fact(num):
#     result=1
#     for i in range(1,num+1):
#         result*=i
#     return result
# print(fact(5))
# def fact(num):
#     if num==0 or num==1:
#         return 1
#     return num*fact(num-1)
# print(fact(5))


# 5 Write a function to return the sum of digits of a number.
# def sum(n):
    # result=0
    # for i in range(1,n+1):
    #     result+=i
    # return result
    
#     if n ==0 or n==1:
#         return 1
#     return n+sum(n-1)
# print(sum(3))    


# 6 Write a function to return the smallest element in a list.
# def small(lis):
# #     a=sorted(lis)
# #     return a[0]
# # print(small([2,4,3,1]))
#     if len(lis)==0:
#         return "List is Empty"
#     smallest=lis[0]
#     for n in lis:
#         if n < smallest:
#             smallest=n
#     return smallest
    
# s=list(map(int,input("Enter numbers :").split()))
# print(small(s))

# numbers = [int(i) for i in input("Enter numbers: ").split()]
# numbers=list(map(int,input("Enter numbers :").split()))
# print(numbers)
    
            
# 7 Write a function to return the second largest number in a list.
# def sec(lis):
#     if len(lis)==0:
#         return "List is Empty"
#     first= second = lis[0]
#     for num in lis:
#         if num > first:
#             second=first
#             first=num
#         elif num>second and num !=first:
#             second=num
#     if first==second:
#         return "no second largest"
#     return second
# s=list(map(int,input("Enter numbers :").split()))
# print(sec(s))

# def sec(lis):
#     if len(lis)==0:
#         return "List is Empty"
#     first= second = lis[0]
#     for num in lis:
#         if num < first:
#             second = first
#             first = num
#         elif num < second and num != first:
#             second = num
#     if first == second:
#         return "No second smallest"
#     return second
# s=list(map(int,input("Enter numbers :").split()))
# print(sec(s))


# 8 Write a function to return the number of words in a sentence.
# def sent(s):
#     count=0
#     words=s.split()
#     for w in words:
#         count +=1
#     return count
# print(sent("helo gys wtsa ap"))
    
    
# 9 Write a function to return True if a number is a palindrome, otherwise False.
# def pal(n):
#     s=str(n)
#     return s ==s[::-1]

# b=int(input(": "))
# print(pal(b))

# 10 Write a function to return the common elements from two lists.
# def comm(list1,list2):
#     result=[]
#     for item in list1:
#         if item in list2 and item not in result:
#             result.append(item)
#     return result
# l1=list(map(int,input("Enter 1st numbers :").split()))
# l2=list(map(int,input("Enter snd numbers :").split()))
# print(comm(l1,l2))

"""# Section C - Arguments Practice"""
# 1 Write a function student_info(name, age, course) and call it using positional arguments.
# def student_info(name, age, course):
#     print ("Name :",name)
#     print ("Age :",age)
#     print ("Course :",course)
# student_info("Yaseen", 20, "Computer Science")


# 2 Write the same function and call it using keyword arguments.
# def student_info(name, age, course):
#     print ("Name :",name)
#     print ("Age :",age)
#     print ("Course :",course)
# student_info(age=20,name="Yaseen",  course="Computer Science")


# 3 Write a function power(base, exp=2) that returns the power of a number using a default argument.
# def power(base, exp=2):
#     return base**exp
# print(power(2,3))


# 4 Write a function discount(price, percent=10) to calculate discounted price.
# def discount(price, percent=10):
#     dic=price-(price*percent/100)
#     return dic
# # print(discount(1000))
# print(discount(345,15))


# 6 Write a function that accepts any number of values using *args and returns their sum.
# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(add(1,2,3))

# 7 Write a function that accepts any number of values using *args and returns the largest one.
# def largest(*args):
#     larg=list(args)
#     sort_lg=sorted(larg)
#     return sort_lg[-1]
# print(largest(2,3,4,5,22,43,1))


# def largest(*args):
#     larg=args[0]
#     for num in args:
#         if num>larg:
#             larg=num
#     return larg
# print(largest(2,3,4,5,22,43,1))
    


# 8 Write a function that accepts user details using **kwargs and prints each key-value pair.
# def keys(**kwargs):
#     for k,v in kwargs.items():
#         print( k,v)
# keys(name="yaseen",place="Mlp")
    

# 9 Write a function bill(item, quantity, price) and calculate total bill.
# def bill(item, quantity, price):
#     total=quantity*price
#     print(f"Item :{item}")
#     print(f"Quantity :{quantity}")
#     print(f"Price Per Item :{price}")
#     print(f"Total bill :{total}")
# # bill("pen",3,20)
# itm=input("item :")
# qnt=int(input("quantity :"))
# pric=float(input("price :"))
# bill(itm,qnt,pric)



# 10 Write a function marks_total(*marks) that returns total and average marks.
# def marks_total(*marks):
#     total=0
#     for i in marks:
#         total+=i
#     avg=total/len(marks)
#     return total,avg
# t,av=marks_total(80,32,4,54,3,44)
# print("Total Mark :",t)
# print("Average Mark :",av)



"""# Section D - String-Based Function Problems"""
# 1 Write a function to check whether a string is a palindrome.
# def palindrom(string:str):
#     string=string.lower()
#     if string==string[::-1]:
#         return "Its is a palindrom"
#     else:
#         return "Not an palindrom"
# st=input()
# print(palindrom(st))


# 2 Write a function to count uppercase and lowercase letters in a string.
# def lowe_up(text:str):
#     upper=0
#     lower=0
#     for ch in text:
#         if ch.isupper():
#             upper+=1
#         elif ch.islower():
#             lower+=1
#     return upper,lower
# tx=input(" :")
# u,l=lowe_up(tx)
# print("Uper case count :",u)
# print("Lower case count :",l)


# 3 Write a function to remove all spaces from a string.
# def remspace(text:str):
#     rem=text.split()
#     join="".join(rem)
#     print(join)
# txt=input(". :")
# remspace(txt)



# 4 Write a function to find the frequency of a given character in a string.
# def freq(text :str,char):
#     tt=0
#     for ch in text:
#         if ch == char:
#             tt+=1
#     return tt
# print(freq("hello world","l"))


# 5 Write a function to convert the first letter of each word to uppercase.
# def upper(text:str):
#     return text.title()
# print(upper("muhammed yaseen python"))
    

# 6 Write a function to replace all vowels in a string with '*'.
# def vowel(text):
#     vow="aeiouAEIOU"
#     result=""
#     for ch in text:
#         if ch in vow:
#             result+="*"
#         else:
#             result+=ch
#     return result
# print(vowel("yaseen"))



# 7 Write a function to check whether two strings are anagrams.
# def angram(str1:str,str2:str):
#     str1=str1.replace(" ", "").lower()
#     str2=str2.replace(" ", "").lower()
    
#     return sorted(str1) == sorted(str2)
# print(angram("listen" ,"silent"))


# 8 Write a function to return the longest word in a sentence.
# def long(text:str):
#     word=text.split()
#     longest=word[0]
#     for w in word:
#         if len(w) > len(longest):
#             longest=w
#     return f"Longest word is : {longest}"
# st=input(" :")
# print(long(st))


# 9 Write a function to count how many times a word appears in a sentence.
# def cont(text:str,word:str):
#     w=text.lower().split()
#     word=word.lower()
#     count=w.count(word)
#     return f"'{word}' appears {count} times"
# print(cont("iam jose mourinho and iam the coach of man united and iam a title winnwer","iam"))


# 10 Write a function to split a sentence and return only words with length greater than 4.
# def grate(text:str):
#     res=""
#     word=text.split()
#     for w in word:
#         if len(w)>4:
#             res+=w+" "
#     return res.strip()
# print(grate("muh yaseen sachu"))
            
    
# def grate(text:str):
#     res=[]
#     word=text.split()
#     for w in word:
#         if len(w)>4:
#             res.append(w)
#     return res
# print(grate("muh yaseen sachu"))
            
    


"""# Section E - List-Based Function Problems"""
# 1 Write a function to return only even numbers from a list.
# def even(num:list):
#     ev=[]
#     for n in num:
#         if n%2==0:
#             ev.append(n)
#     return ev

# numbers=list(map(int,input("enter the list elements :").split()))
# # print(numbers)
# print(even(numbers))  

# numbers = [int(i) for i in input ("enter element").split() ]
# print(numbers)
# data = input("enter the list elements : ").split()
# print(data)
# for i in data:
#     numbers.append(int(i))

# print(numbers)
    

# 2 Write a function to return only prime numbers from a list.
# def isprme(numbers):
#     primee=[]
#     for num in numbers:
#         if num>1:
#             is_prime=True
#             for i in range(2,num):
#                 if num%i==0:
#                     is_prime=False
#                     break
#             if is_prime:
#                 primee.append(num)
#     return primee
# # numb=list(map(int,input("Numbers :").split()))
# # numb=[i for i in range(1,100)]
# # print(isprme(numb))
# def isprme(numbers):
#     primee=[]
#     for num in numbers:
#         if num>1:
#             for i in range(2,num):
#                 if num%i==0:
#                     break
#             else: 
#                 primee.append(num)
#     return primee
# numb=[i for i in range(1,100)]
# print(isprme(numb))


# 3 Write a function to remove duplicates from a list without changing the order.
# def dupe(numbers):
#     dup=[]
#     for i in numbers:
#         if i not in dup:
#             dup.append(i)
#     return dup
# lis=[int(i) for i in input("enter the list :").split()]
# print(dupe(lis))


# 4 Write a function to return the sum of all odd numbers in a list.
# def odd(numbers):
#     sum=0
#     for i in numbers:
#         if i%2==1:
#             sum+=i
#     return sum
# lis=[int(i) for i in input("enter the list :").split()]
# print(odd(lis))


# 5 Write a function to find the index positions of a given element in a list.
# def index(list:list,ind):
#     ide=[]
#     for i in range(len(list)):
#         if list[i]==ind:
#             ide.append(i)
#     return ide
# lis=[int(i) for i in input("enter the list :").split()]
# num=int(input())
# print(index(lis,num))


# 6 Write a function to merge two lists and return a sorted result.
# def merg(lis1,lis2):
#     merged=lis1+lis2
#     merged.sort()
#     return merged
# list1=[int(i) for i in input("enter the 1st list :").split()]
# list2=[int(i) for i in input("enter the 2nd list :").split()]
# print(merg(list1,list2))


# 7 Write a function to count positive and negative numbers in a list.
# def pos(numbers):
#     negative_ct=0
#     positve_ct=0
#     for i in numbers:
#         if i >0:
#             positve_ct+=1
#         else:
#             negative_ct+=1
#     return positve_ct,negative_ct
# list1=[int(i) for i in input("enter the 1st list :").split()]
# p,v=pos(list1)
# print("positive ;",p)
# print("negative ;",v)


# 8 Write a function to return the maximum difference between two elements in a list.
# def diffren(lis):
#     # return max(lis)-min(lis)
#     sr=sorted(lis)
#     return sr[-1] - sr[0]
# list1=[int(i) for i in input("enter the 1st list :").split()]
# print(diffren(list1))

# 9 Write a function to rotate a list to the right by one position.
# def rotate(lis):
#     if len(lis)==0:
#         return lis
#     return [lis[-1]]+lis[:-1]
# list1=[int(i) for i in input("enter the 1st list :").split()]
# print(rotate(list1))


# 10 Write a function to return a new list containing squares of all elements.
# def sqr(lis):
#     squares=[]
#     for i in lis:
#         sq=i**2
#         squares.append(sq)
#     return squares
# list1=[int(i) for i in input("enter the 1st list :").split()]
# print(sqr(list1))


"""# Section F - Number Logic Function Problems"""
# 1 Write a function to check whether a number is prime.
# def prime(num):
#     if num <=1:
#         print("not a prime")
#         return
#     for i in range(2,num):
#         if num%i==0:
#             print("Not a Prime")
#             return
#     print("Prime Numner")

# n=int(input("Enter the number :"))
# prime(n)


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


# def add(num1):
#     return num1**2
# print(add(2))
# list1=[1,2,4,5,78]
# result=list(map(add,list1))
# print(result)