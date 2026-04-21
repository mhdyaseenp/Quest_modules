# PYTHON FULL STACK TRAINING: TUPLE LOGIC & INTERVIEW

""" --- PART 1: BASICS & INITIALIZATION ---"""
# 1. Create a tuple containing five different data types (int, float, string, list, boolean).
# tuple=(2,2.4,'yaseen',[2,3,4])
# print(tuple)

# 2. Write a script to check the type of a tuple with a single element. Show the difference
# between (5) and (5,).
# tuple=(5,)
# print(type(tuple))

# 3. Access the last element of a tuple without knowing its length.
# tuple=(2,4,5,6,5,4,3)
# last=tuple[-1]
# print(last)

# 4. Access the second to last element of a tuple using negative indexing.
# tuple=(2,4,5,6,5,4,3)
# second_last=tuple[-2]
# print(second_last)

# 5. Given nested_tuple = ("Python", [10, 20, 30], (5, 15, 25)), print the number 20.
# nested_tuple = ("Python", [10, 20, 30], (5, 15, 25))
# number=nested_tuple[-2][-2]
# print(number)

# 6. Check if the element 'Sreeraj' exists in a tuple using a membership operator.
# person=('richu','shabin','shahal','yaseen','sreeraj')
# print('sreeraj' in person)
# print('shakir'  in person)


# 7. Find the memory size of a list vs. a tuple with the same elements using the sys module.
# import sys
# list=[10,20,30,40,50]
# tuple=(10,20,30,40,50)
# list_size=sys.getsizeof(list)
# tuple_size=sys.getsizeof(tuple)

# print(list_size)
# print(tuple_size)

# 8. Unpack a tuple of 3 elements into three variables: x, y, and z.
# tuple=('yaseen','jasil','shakir')
# x,y,z=tuple
# print(x)
# print(y)
# print(z)

# 9. Demonstrate what happens if you try to unpack a tuple of 4 elements into 3 variables.
# error

# 10. Use the 'extended iterable unpacking' (using *) to grab the first element and the rest into a
# list.
# tuple=('yaseen','jasil','shakir','niyas')
# x,y,*z=tuple
# print(x)
# print(y)
# print(z)
""" --- PART 2: IMMUTABILITY LOGIC ---"""
# 11. Write code that attempts to change the first element of a tuple and handle the resulting
# TypeError gracefully.
# tuple=(10,20,30,40,50)
# temp_tup=list(tuple)
# temp_tup[0]=100
# print(temp_tup)


# 12. Given a tuple: t = (1, 2, [3, 4]). Change the value 3 to 30. Explain why this works despite
# tuples being immutable.
# t = (1, 2, [3, 4])
# t[-1][0]=30
# print(t)                      #tuple is a immutable but list is mutable


# 13. Create two tuples, concatenate them, and assign them to a new variable.
# tuple1=(10,20,30,40,50)
# tuple2=(70,43,4,10,20)
# samp=tuple1+tuple2
# print(samp)


# 14. Use the repetition operator (*) to create a tuple of ten zeros.
# tuple1=(10,20,30,40,50)
# tuple1+=(0,)*10
# print(tuple1)


# 15. Swap two variables a and b using tuple unpacking logic in a single line.
# a=(10,20,30)
# b=(40,50,60)
# a,b=b,a
# print(a)
# print(b)


# 16. Write a program to "add" an item to a tuple by converting it to a list first.
# a=(10,20,30)
# change=list(a)
# change.append(40)
# print(change)


# 17. Write a program to "remove" an item from a tuple.
# a=(10,20,30,50,40,75)
# change=list(a)
# # change.pop()
# # change.remove(30)
# print(change)


# 18. Delete an entire tuple variable from memory and verify its absence using a try-except
# block.
# tup=(49,49,39,39)
# tup+=(74,)
# del tup
# try:
#     print(tup)
# except NameError:
#     print("tuple is deleted")

# 19. Sort a tuple of integers and return the result as a new tuple.
# t = (5,2,9,1,7)
# sort=sorted(t)
# print(sort)

# 20. Reverse a tuple using the slicing method [::-1].
# t=(74,54,4,3,5,3,33)
# rev=t[::-1]
# print(rev)
""" --- PART 3: METHODS & AGGREGATION ---"""
# 21. Find the index of the first occurrence of the number 10 in a tuple.
# t=(3,43,4,5,3,2,10,2304)
# ind=t.index(10)
# print(ind)

# 22. Count how many times the string "Python" appears in a tuple of job roles.
# job=('python','yase','python','shakir')
# count=job.count('python')
# print(count)

# 23. Find the maximum and minimum values in a tuple of stock prices.
# t=(29,39,39,33,399,398,390,23)
# change=sorted(t)
# minimum=change[0]
# maximum=change[-1]
# print("minimum value :",minimum)
# print('maximum value :',maximum)

# 24. Calculate the sum of all numeric elements in a tuple.
# t=(1,3,4,3,5,'s',23.4)
# total=0
# for item in t:
#     try:
#         total+=float(item)
#     except:
#         pass
# print('total= ',total)



# 25. Given a tuple of tuples: ((1, 2), (3, 4), (5, 6)), calculate the sum of the second element of
# each internal tuple.
# t=((1, 2), (3, 4), (5, 6))
# total=0
# for item in t:
#     for sec in item[1:]:
#         total+=sec
# print(total)


# 26. Use the index() method to find the position of 'Apple' starting from index 3 in a large fruit
# tuple.
# fruits = ('Banana','Orange','Mango', 'Grapes','Apple','Pineapple','Apple')
# position = fruits.index('Apple',3)
# print(position)


# 27. Write a function that takes a tuple and returns a new tuple containing only the even
# numbers.
# t=(2,3,45,2,4,3,6,7,89,88,76,9)
# even=[]
# for i in t:
#     if i%2==0:
#         even.append(i)
# print(tuple(even))


# 28. Convert a list of tuples into a single flat list.
# data=[(1, 2),(3, 4),(5, 6)]
# flat=[]
# for i in data:
#     for j in i:
#         flat.append(j)
# print(flat)


# 29. Create a tuple from a user-input string where each character is an element.
# inp=input("enter :")
# # tup=tuple(inp)
# # print(tup)
# result=()
# for ch in inp:
#     result+=(ch,)
# print(result)

# 30. Check if all elements in a tuple are truthy using the all() function.
# t=(1,2,3,4)
# if all(t):
#     print("All elements are truthy")
# else:
#     print("Some elements are falsy")


""" --- PART 4: SLICING & LOOPING ---"""
# 31. Extract a sub-tuple containing the elements from index 2 to 5 (inclusive).
# t = (10, 20, 30, 40, 50, 60, 70)
# print(t[2:5])


# 32. Use slicing to get every second element of a tuple.
# t = (10, 20, 30, 40, 50, 60, 70)
# print(t[1::2])


# 33. Write a 'for' loop to print each element of a tuple with its corresponding index number.
# t = (10, 20, 30, 40, 50, 60, 70)
# for i in range(len(t)):
#     print("index :",i,"element :",t[i])


# 34. Use a 'while' loop to iterate through a tuple backwards.
# t = (10, 20, 30, 40, 50, 60, 70)
# len=len(t)-1
# while len >=0:
#     print(t[len],end=" ")
#     len-=1

# 35. Create a tuple of 10 numbers and slice it to get the last 3 elements.
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(t[-3:])

# 36. Slice a tuple to remove the first and last elements.
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(t[1:-1])


# 37. Use a for loop to concatenate all strings in a tuple into a single sentence.
# t = ("Hello", "this", "is", "a", "sentence")
# result = ""
# for w in t:
#     result+=w+" "
# print(result)

# 40. Zip two tuples together to create a list of coordinate pairs.
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# result = list(zip(t1, t2))
# print( result)


""" PART 5 - Logical Tuple Problems"""
# 31. Create a tuple of numbers and find the second largest number.
# t=(23,34,3,53,42,45,56,99,-2)
# lis=list(t)
# sort=sorted(lis)
# print("second laarg :",sort[-2])
# largest=0
# second=0
# # largest=t[0]
# # second=t[0]
# for num in t:
#     if num > largest:
#         second=largest
#         largest=num
#     elif num > second and num != largest:
#         second=num
# print(second)


# 32. Write a program to remove duplicate elements from a tuple.
# t=(23,34,3,53,42,45,56,99,2,3,2,3)
# result=[]
# for i in t:
#     if i not in result:
#         result.append(i)
# print(result)


# 33. Write a program to find the frequency of each element in a tuple.
# t=(23,34,3,53,42,45,56,99,2,3,2,3)
# freq=[]
# for i in t:
#     if i not in freq:
#         print(i, ":", t.count(i))
#         freq.append(i)


# 34. Write a program to convert a list of tuples into a dictionary.
# Example:
# [(1,'A'), (2,'B'), (3,'C')]

# lis=[(1,'A'), (2,'B'), (3,'C')]
# print(dict(lis))



# 36. Write a program to sort a tuple of tuples based on the second element.
# Example:
# ((1,5),(3,2),(4,8))
# t = ((1, 5), (3, 2), (4, 8))
# lst = list(t)
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i][1] > lst[j][1]:
#             lst[i], lst[j] = lst[j], lst[i]
# sorted_tuple = tuple(lst)
# print("Sorted tuple:", sorted_tuple)


# 37. Write a program to find common elements between two tuples.
# t1 =(1,2,3,4,5)
# t2 =(3,4,5,6,7)
# common = tuple(set(t1) & set(t2))
# common = tuple(set(t1).intersection( set(t2)))
# print("Common :", common)


# 38. Write a program to convert a tuple into a string.
# t = ('y','a','s','e','e','n')
# result =''.join(t)
# print("String:", result)

# 39. Write a program to count vowels present in a tuple of characters.
# t = ('y','a','s','e','e','n')
# vowel='aeiou'
# cont=0
# for ch in t:
#     if ch in vowel:
#         cont+=1
# print(cont)


# 40. Write a program to find the product of all numbers in a tuple.
# t =(1,2,3,4,5)
# product=1
# for item in t:
#     product*=item
# print("Product :",product)


"""--- PART 6: INDUSTRIAL TRENDS & ADVANCED (MISSING TOPICS)  --- 
"""
# 41. [NamedTuple] Use 'collections.namedtuple' to create a 'Student' object with fields 'name',
# 'roll_no', and 'course'.

# 42. [Dictionary Keys] Demonstrate using a tuple as a key in a dictionary (e.g.,
# latitude/longitude). Explain why a list cannot be a key.
# 43. [Data Integrity] Write a function that returns multiple values (name, age, salary) as a
# tuple.
# 44. [Efficiency] Iterate through a tuple of 1,000,000 integers and measure the time taken.
# Compare it with a list.
# 45. [Nested Logic] Given a list of tuples representing products: [("Laptop", 1000), ("Mouse",
# 25)]. Sort the list based on the price (the second element).
# 46. [String Formatting] Use a tuple to provide values for an old-style string formatting:
# "Hello %s, your ID is %d".
# 47. [Function Arguments] Write a function that accepts *args and prints the type of 'args'.
# 48. [Hashing] Use the hash() function on a tuple. Then try it on a list. Note the difference.
# 49. [Conversion] Convert a tuple of single-character strings into a single string.
# 50. [Filtering] Use the filter() function with a lambda to remove all None values from a tuple.