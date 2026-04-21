"""  Python Lab Practical Questions
     Topic: Sets in Python (Beginner → Advanced)"""

""" Section 1 - Basic Set Programs"""
# 1. 2. 3. 4. 5. 6. 7. 8. 9. Create a set containing 5 numbers and print the set.
# Create a set with mixed data types and print each element.
# Write a program to create a set from a list.
# Write a program to remove duplicate elements from a list using a set.
# Create an empty set and add three elements to it.
# Write a program to check if an element exists in a set.
# Create a set and print all elements using a for loop.
# Write a program to find the length of a set without using len().
# Write a program to convert a tuple into a set.
# 10. Write a program to convert a set into a list.
""" Section 2 - Adding and Removing Elements"""
# 11. Create a set and add a new element using add().
# 12. Write a program to add multiple elements to a set using update().
# 13. Write a program to remove an element using remove().
# 14. Write a program to remove an element using discard().
# 15. Write a program to remove a random element using pop().
# 16. Write a program to clear all elements from a set.
# 17. Write a program to copy a set into another set.
# 18. Write a program to add elements from a list into a set.
# 19. Write a program to add elements from a tuple into a set.
# 20. Write a program to update a set with another set.
""" Section 3 - Set Operations"""
# 21. Write a program to find the union of two sets.
# set1 = {1, 2, 3,5}
# set2 = {3, 4, 5}
# print(set1 | set2)


# 22. Write a program to find the intersection of two sets.
# set1 = {1, 2, 3,5}
# set2 = {3, 4, 5}
# print(set1 & set2)


# 23. Write a program to find the difference between two sets.
# set1 = {1, 2, 3,5}
# set2 = {3, 4, 5}
# print(set1 - set2)


# 24. Write a program to find the symmetric difference between two sets.
# set1 = {1, 2, 3,5}
# set2 = {3, 4, 5}
# print(set1 ^ set2)



# 25. Write a program to update a set using intersection_update().
# set1 = {1, 2, 3,5}
# set2 = {3, 4, 5}
# set1.intersection_update(set2)
# print(set1)


# 26. Write a program to update a set using difference_update().


# 27. Write a program to update a set using symmetric_difference_update().


# 28. Write a program to check if one set is a subset of another set.
# set1 = {1, 2, 3,5}
# set2 = {3, 4, 5}
# print(set1.issubset(set2))

# 29. Write a program to check if one set is a superset of another set.
# set1 = {1, 2, 3,5}
# set2 = {1, 2, 5}
# print(set1.issuperset(set2))

# 30. Write a program to check if two sets are disjoint.
""" Section 4 - Logical Set Problems"""
# 31. Write a program to find common elements between two lists using sets.
# a=[1,2,3,45]
# b=[1,3,45,6,3]

# set1=set(a)
# set2=set(b)
# print(set1 & set2)


# 32. Write a program to find unique elements from two lists.


# 33. Write a program to find elements present in the first list but not in the second list.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5]
# result = list(set(list1) - set(list2))
# print(result)


# 34. Write a program to remove duplicates from a sentence using sets.
# text="python is easy and python is fun"
# words=text.split()
# print(words)

# sentence = "python is easy and python is fun"
# words = sentence.split()
# res=[]
# for w in words:
#     if w not in res:
#         res.append(w)
# fin=" ".join(res)
# print(fin)


# 35. Write a program to find unique characters in a string using sets.
# text = "programming"
# uniq=set(text)
# print(uniq)


# 36. Write a program to count unique words in a sentence.
# sentence = "python is easy and python is fun"
# words = sentence.split()
# uniq=set(words)
# for w in uniq:
#      count=words.count(w)
     # print(w,count)


# 37. Write a program to find the difference between two strings using sets.
# str1 = "hello"
# str2 = "world"
# set1 = set(str1)
# set2 = set(str2)
# print(set1 - set2)


# 38. Write a program to find vowels present in a string using sets.
# st='yaseen'
# vowel='aeiou'
# # result=set()
# # for ch in st:
# #     if ch in vowel:
# #         result.add(ch)
# # print(result)
    
# text=set(st)
# vowel_set=set(vowel)
# print(text & vowel_set)


# 39. Write a program to check whether two strings contain the same characters.
# str1 = "listen"
# str2 = "silent"
# if set(str1) == set(str2):
#     print("Same characters")
# else:
#     print("Different characters")


# 40. Write a program to find common characters between two strings.
# str1 = "hello"
# str2 = "world"
# result = set(str1) & set(str2)
# print(result)



""" Section 5 - Set Comprehension"""
# 41. Write a program to create a set of squares from numbers 1–10 using set
# # comprehension.
# sqr={i*i for i in range(1,11)}
# print(sqr)

# 42. Write a program to create a set of cubes using set comprehension.
# qub={x:x**3 for x in range(1,11)}
# print((qub))


# 43. Write a program to create a set of even numbers from 1–20 using set comprehension.
# evn={x for x in range(1,21) if x%2==0}
# print(evn)


# 44. Write a program to create a set of odd numbers using set comprehension.
# odd={x for x in range(1,21) if x%2==1}
# print(odd)


# 45. Write a program to create a set containing lengths of words in a sentence.
# sent = "python is easy and fun"
# length=[len(w) for w in sent.split()]
# print(length)


""" Section 6 - Industry Based Problems"""
# 46. Given two sets representing students enrolled in Python and Java, find students
# enrolled in both courses.
# 47. Given two sets representing users who logged in today and yesterday, find new users
# today.
# 48. Given two sets representing available skills and required job skills, find missing skills.
# 49. Create a set representing product categories in an e-commerce system and remove a
# category dynamically.
# 50. Given two datasets of email IDs, remove duplicates and print all unique email IDs.
""" Bonus Interview Questions"""
# 1. 2. 3. 4. 5. Why are sets unordered in Python?
# What is the difference between remove() and discard()?
# Why can't sets contain mutable elements like lists?
# What is the difference between difference() and difference_update()?
# When should sets be used instead of lists in real-world applications? 