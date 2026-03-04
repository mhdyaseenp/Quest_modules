"""STRING SLICING IN PYTHON – LAB PRACTICAL QUESTIONS"""

"""BASIC LEVEL"""

# 1.  Write a Python program to take a string from the user and print the
#     first character using slicing.
# name=input("Enter your name :")
# print(name[:1])

# 2.  Write a program to display the last character of a string using
#     slicing.
# name=input("Enter your name :")
# print(name[-1])

# 3.  Given a string, print the first 5 characters using slicing.
# name=input("Enter your name :")
# print(name[:6])

# 4.  Write a program to print all characters of a string except the first
#     one.
# name=input("Enter your name :")
# print(name[1::])

# 5.  Write a program to print all characters of a string except the last
#     one.
# name=input("Enter your name :")
# print(name[:-1])

# 6.  Given a string, print characters from index 2 to index 6.
# name=input("Enter your name :")
# print(name[2:8])

# 7.  Write a program to print every character at even index positions
#     using slicing.
# name=input("Enter your name :")
# print(name[::2])

# 8.  Write a program to print every character at odd index positions
#     using slicing.
# name=input("Enter your name :")
# print(name[1::2])


# 9.  Write a program to reverse a string using slicing.
# name=input("Enter your name :")
# print(name[::-1])

# 10. Given a string, print the middle character(s) using slicing (assume
#     length can be even or odd).
# s=input("Enter your name :")
# n=len(s)
# print(n)
# if n%2==0:
#     middle=s[n//2-1:n//2+1]
# else:
#     middle=s[n//2]
# print("MIddle ch is ",middle)

"""INTERMEDIATE LEVEL"""

# 11. Write a program to check whether a string is a palindrome using
#     slicing.
# name=input("Enter your name :")
# ch=name
# if ch[::-1]==name:
#     print("palindrom")
# else:
#     print("not")


# 12. Given a string, extract the first half and second half using slicing
#     and print them separately.
# s=input("Enter your name :")
# n=len(s)
# if n%2==0:
#     first=s[:n//2]
#     second=s[n//2:]
# else:
#     first=s[:n//2]
#     second=s[n//2:]
# print(f"First Half is {first} Second Half is {second}")


# s = input("Enter a string: ")
# n = len(s)
# mid = n // 2
# first_half = s[:mid]
# second_half = s[mid:]
# print("First Half:", first_half)
# print("Second Half:", second_half)


# 13. Write a program to remove the first and last two characters from a
#     string using slicing.
# s = input("Enter a string: ")
# print(s[2:-2])


# 14. Given a string, print characters from index 1 to the second last
#     character.
# s = input("Enter a string: ")
# print("Output:", s[1:-1])


# 15. Write a program to extract every third character from a string using
# #     slicing.
# s = input("Enter a string: ")
# print("Output:", s[::3])


# 16. Given a string, reverse only the first half of the string using
#     slicing.
# s = input("Enter a string: ")
# n = len(s)
# mid = n // 2
# first_half = s[:mid]
# rev=first_half[::-1]
# print(rev)


# 17. Write a program to extract the domain name from an email ID using
#     slicing.
# email=input("Enter email id: ")
# position=email.index("@")
# domain=email[position+1:]
# print(domain)


# 18. Given a sentence, extract and print the last word using slicing.
# s=input("Eter the sentence :")
# pos=s.rindex(" ")
# word=s[pos+1:]
# print(word)


# 19. Write a program to swap the first and last characters of a string
#     using slicing.
# name=input("Eter the word :")
# swap=name[-1] + name[1:-1] + name[0]
# print(swap)


# 20. Given a string, print all characters except vowels using slicing and
#     looping logic.
# s=input("Eter the word :")
# vovel="AEIOUaeiou"
# for ch in s:
#     if ch not in vovel:
#         print(ch,end="")


# 21. Write a program to split a string into two parts based on a given
#     index using slicing.
# s=input("Eter the word :")
# index=int(input("Enter the split index :"))
# first=s[:index]
# second=s[index:]
# print(f"First part: {first}")
# print(f"Second part: {second}")


# 22. Given a string, print the string in reverse order skipping every
#     second character.
# s=input("Eter the word :")
# print(s[::-2])


# 23. Write a program to extract the username from an email ID using
# #     slicing.
# email=input("Enter email id: ")
# position=email.index("@")
# user_name=email[:position]
# print(user_name)


# 24. Given a string, check whether the first half and second half are
#     equal using slicing.
# s=input("Enter a String :")
# n=len(s)
# # midd=n//2
# if n%2==0:
#     first=s[:n//2]
#     second=s[n//2:]
# else:
#     first=s[:n//2]
#     second=s[n//2+1:]
# if first==second:
#     print("Both are equal")
# else:
#     print("not eqal")


# 25. Write a program to count how many characters are present in a
#     substring obtained using slicing.
# s = input("Enter a string: ")
# start = int(input("Enter start index: "))
# end = int(input("Enter end index: "))
# sub=s[start:end]
# count=len(sub)
# print("Substrin :" ,sub)
# print("Number of substring :" ,count)


"""CONCEPT-FOCUSED PRACTICE"""

# 26. Write a program to demonstrate positive and negative indexing using
#     slicing.

# 27. Given a string, show the difference between string[start:end] and
#     string[start:end:step].

# 28. Write a program to demonstrate slicing with only start index, only
#     end index, and only step.

# 29. Write a program to safely slice a string even if the index range
#     exceeds the string length.

# 30. Write a program to show that string slicing does not modify the
#     original string.

# NOTE FOR STUDENTS:

# • Python string slicing format: string[start : end : step] • Start index
# is inclusive, end index is exclusive • Step defines the jump between
# characters • Strings are immutable in Python

# End of Lab Questions
