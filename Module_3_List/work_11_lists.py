"""Python Data Structures (Lists) – Lab Practical"""

""" Section 1: Beginner Level"""

# 1. Create a list of five integers and print all elements using a for loop
# s=[2,4,5,24,4]
# for i in s:
#     print(i,end=" ")

# 2. Write a program to find the length of a list without using len().
# s=[2,4,5,24,4]
# count=0
# for i in s:
#     count+=1
# print(count)


# 3. Create a list of numbers and print the maximum and minimum values.
# numbers=[10,30,40,50,60,3]

# minimum=min(numbers)
# maximun=max(numbers)
# print("Maximumx value :",maximun)
# print("Miinimum value :",minimum)


# 4. Write a program to append a new element to a list entered by the user
# s=[1,2,3,4,5,6]
# y=int(input("Enter a number :"))
# s.append(y)
# print(s)

# 5. Insert an element at a specific position in a list.
# s=[1,2,3,4,5]
# y=int(input("Enter a position :"))
# z=input("Enter a vlaue :")
# s.insert(y,z)
# print(s)


# 6. Remove an element from a list using remove() and pop().
# list1=[1,2,3,4,5,6]
# # y=list1.pop()
# list1.remove(5)
# print(list1)



# 7. Write a program to check whether a given element exists in a list.
# list=[1,2,3,4,5,6]
# y=int(input("enter the number :"))
# if y in list:
#     print ("its exixst",list)
# else:
#     print ("dosnot exixst",list)


# 8. Reverse a list without using reverse().
# list=[1,2,3,4,5,6]
# sl=list[::-1]
# print(sl)


# 9. Sort a list of numbers in ascending and descending order.
# list=[3,5,2,6,4,1]
# list.sort()
# print("Assending",list)
# list.sort(reverse=True)
# print("Desending",list)


# 10. Create a list of numbers and print only the even numbers.
# s=[2,3,5,35,6,8,45,10]
# for i in s:
#     if i%2==0:
#         print(i,end=" ")


#11. Count how many times a specific element appears in a list.
# s=[2,3,5,35,6,8,45,6,6]
# x=int(input("Enter the searching number :"))
# cont=s.count(x)
# print(cont)


#12. Write a program to copy one list into another list.
# list1=[1,2,3,4,5]
# list2=list1.copy()
# print("orginal :",list1)
# print("copy :",list2)


#13. Concatenate two lists using the + operator.
# list1=[1,2,3]
# list2=[4,5,6]
# result=list1+list2
# print(result)

#14. Repeat a list three times using the * operator.
# list1=[1,2,3]
# result=list1*3
# print(result)

#15. Demonstrate positive and negative indexing in a list.
# nums = [10, 20, 30, 40, 50]

# # Positive indexing
# print("Positive Indexing:")
# print(nums[0])   # first element
# print(nums[2])   # third element

# # Negative indexing
# print("\nNegative Indexing:")
# print(nums[-1])  # last element
# print(nums[-3])  # third from end

"""" Section 2: Intermediate Level"""
# 16. Write a program to remove duplicates from a list.
# s=[1,2,3,4,5,5,5,66]
# z=[]
# for i in s:
#    if i not in z:
#         z.append(i)
# print(z)


# 17. Find the second largest element in a list.
# s=[1,2,33,4,5,5,5,66]
# s.sort()
# print(s[-2])


# 18. Write a program to rotate a list to the left by one position.
# num=[1,2,3,4,5]
# nums=num[1::]+[num[0]]
# print(nums)


# 19. Write a program to rotate a list to the right by one position.
# num=[1,2,3,4,5]
# nums=[num[-1]]+num[:-1]
# print(nums)


# 20. Move a specific element (e.g., 50) to the first position of a list.
# num=[10,20,30,40,50,60]
# num.remove(50)
# num.insert(0,50)
# print(num)


# 21. Create a list of squares of numbers from 1–10 using list comprehension.
# square=[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)


# 22. Create a list containing only odd numbers from 1–50 using list comprehension.
# odd=[]
# for i in range(1,50):
#     if i %2==1:
#         odd.append(i)
# print(odd)


# 23. Write a program to merge two lists and remove duplicates.
# list1=[1,2,34,5,2,42,4]
# list2=[4,6,4,3,9,50,1,2]
# list3=list1+list2

# result=[]
# for i in list3:
#     if i not in result:
#         result.append(i)
# print(result)


# 24. Find the sum of all elements in a list without using sum().
# num=[1,2,3]
# total=0
# for i in num:
#     total+=i
# print(total)


# 25. Write a program to find common elements between two lists.
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common = []
# for i in list1:
#     if i in list2 and i not in common:
#         common.append(i)
# print(common)



# 26. Write a program to split a list into two halves.
# num=[1,2,3,4,56,7,8]
# mid=len(num)//2
# first=num[:mid]
# last=num[mid:]
# print(first)
# print(last)


# 27. Find the index of a given element without using index().
# num=[1,2,3,2,4,5,6,7,8]
# x=int(input("eneter :"))
# ind=-1
# for i in range(len(num)):
#     if num[i]==x:
#         ind=i
#         break
# if ind != -1:
# # if ind == i:
#     print(ind)
# else:
#     ("elemenet not found")


# 28. Write a program to flatten a nested list.
# num = [[1, 2], [3, 4], [5, 6]]
# flat=[]
# for i in num:
#     # print(i)
#     for j in i:
#         flat.append(j)
#         # print(j)
# print(flat)


# 29. Create a program to find the frequency of each element in a list.
# nums = [1, 2, 2, 3, 1, 4, 2]
# for i in nums:
#     print(i,":",nums.count(i))


# 30. Reverse each element of a list of strings.
# word=['hello','yaseeen','python']
# result=[]
# for w in word:
#     result.append(w[::-1])
# print(result)

"""Section 3: Advanced Level"""
# 31. Implement a matrix using nested lists and print it in matrix format.
# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# for i in matrix:
#     for j in i:
#         print(j,end=" ")
#     print()


# 32. Write a program to add two matrices using nested lists.

# 33. Write a program to transpose a matrix.
# 34. Flatten a 2D list into a single list using list comprehension.
# 35. Find the largest sublist length in a nested list.
# 36. Write a program to find the intersection of multiple lists.
# 37. Write a program to group list elements by their length (strings).
# 38. Implement a simple stack using a Python list.
# 39. Implement a queue using a Python list.
# 40. Write a program to shuffle elements in a list.
# 41. Write a program to find the kth largest element in a list.
# 42. Write a program to check whether a list is a palindrome.
# 43. Write a program to generate all possible pairs from a list.
# 44. Create a list of prime numbers within a given range using list comprehension.
# 45. Write a program to remove all negative numbers from a list.
"""# Section 4: Logical / Problem Solving"""
# 46. Given a list of numbers, move all zeros to the end while maintaining order.
# 47. Find the first non-repeating element in a list.
# 48. Find the highest frequency element in a list.
# 49. Find all pairs whose sum equals a given target value.
# 50. Write a program to detect duplicates in a list.
# 51. Given two lists, determine whether they contain the same elements regardless of order.
# 52. Write a program to partition a list into even and odd numbers.
# 53. Implement bubble sort using lists.
# 54. Implement selection sort using lists.
# 55. Write a program to remove consecutive duplicate elements.
""""# Section 5: Interview-Oriented Questions"""
# 56. Explain the difference between list.copy() and copy.deepcopy(). Demonstrate with code.
# 57. What is list comprehension? Write examples and compare it with loops.
# 58. What happens when you modify a list during iteration? Demonstrate with an example.
# 59. Explain the difference between append(), extend(), and insert().
# 60. Demonstrate shallow copy behavior using lists.
# 61. Explain time complexity of list operations (append, insert, pop).
# 62. Write a program to implement a stack using a list and explain push/pop.
# 63. Write a program to remove duplicates while preserving order.
# 64. Explain the difference between mutable and immutable data structures in Python.
# 65. Write a Python program to simulate a simple task queue using lists.