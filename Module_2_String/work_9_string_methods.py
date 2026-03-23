# """------------------Python Strings  Lab Practical Questions------------------"""
"""Beginner Level"""
# • 1. Create a string and print it.
# ch="yaseen"
# print(ch)

# • 2. Print each character of a string using indexing.
# ch="yaseen"
# for i in ch:
#     print(i)


# • 3. Print the first and last character of a string.
# ch="yaseen"
# first=ch[0 ]
# last=ch[-1]
# print(first)
# print(last)


# • 4. Demonstrate positive and negative indexing on a string.



# • 5. Extract the first five characters from a string using slicing.
# ch="hello guyss"
# print(ch[:6])


# • 6. Reverse a string using slicing.
# ch="yaseen"
# print(ch[::-1])


# • 7. Count the length of a string without using len().
# ch="yaseen"
# count=0
# for i in ch:
#     count+=1
# print(count)


# • 8. Convert a string to uppercase and lowercase.
# ch="yaseen"
# print("lower case :",ch.lower())
# print("upper case :",ch.upper())


# • 9. Capitalize the first letter of a string.
# ch="muhammed yaseen"
# print(ch.title())


# • 10. Swap the case of each character in a string.
# ch="YasEen"
# print(ch.swapcase())


# • 11. Check whether a string starts with a specific substring.
# ch="yaseen"
# print(ch.startswith("y"))


# • 12. Check whether a string ends with a specific substring.#
# ch="yaseen"
# print(ch.endswith("n"))


# • 13. Count the number of occurrences of a character in a string.
# ch="yaseen"
# print(ch.count("e"))


# • 14. Replace a word in a string with another word.
# ch="yaseen"
# print(ch.replace('y','Y'))


# • 15. Remove leading and trailing spaces from a string.
# ch="        yaseen        "
# rint(ch.strip())


"""Intermediate Level"""
# • 1. Check whether a string contains only alphabets.
# ch=input("")
# if ch.isalpha():
#     print("string contains only alphas")
# else:
#     print("string contains othe charectes")


# • 2. Check whether a string contains only digits.
# ch=input("")
# if ch.isdigit():
#     print("string digits only ")
# else:
#     print("string contains othe charectes")


# • 3. Check whether a string is alphanumeric.
# ch=input("")
# if ch.isalnum():
#     print("string contains alphas and digits only ")
# else:
#     print("string contains othe charectes")


# • 4. Split a sentence into words using split().
# ch="hello iam muhammed"
# print(ch.split())


# • 5. Join a list of words into a single string.
# ch="hello iam muhammed"
# spl=ch.split()
# print(" ".join(spl))


# • 6. Find the first occurrence of a substring in a string.
# ch="yaseen"
# print(ch.find("e"))

# • 7. Find the last occurrence of a substring in a string.
# ch="yaseen"
# print(ch.rfind("e"))

# • 8. Remove a prefix from a string.
# ch="muh Yaseen"
# print(ch.removeprefix("muh "))

# • 9. Remove a suffix from a string.
# ch="muh Yaseen P"
# print(ch.removesuffix("P"))

# • 10. Center align a string within a given width.
# ch="yasen"
# print(ch.center(25,'*'))


# • 11. Left justify and right justify a string.
# ch="yaseen"
# print(ch.ljust(10,'*'))
# print(ch.rjust(10,'*'))


# • 12. Pad a number string with zeros using zfill().
# ch='947845' 
# print(ch.zfill(10))


# • 13. Use format() method in string formatting.
# name="yaseen"
# age=28
# print("iam {} ,iam {} year old".format(name,age))


# • 14. Create a formatted string using f-strings.d
# name="yaseen"
# age=28
# print(f"iam {name} ,iam {age} year old")


# • 15. Use partition() to split a string into three parts.
# ch="Iam muh yaseen"
# print(ch.partition(" "))

""" Logical Problem Solving"""

# • 1. Check whether a string is a palindrome.
# ch=input("enter string :")
# rev=ch
# if rev[::-1]==ch:
#     print("palindrom")
# else:
#     print("not an palindrom")


# • 2. Count the number of vowels and consonants in a string.
# ch="yaseenrr"
# vovel="aeiouAEIOU"
# count=0
# c_count=0
# for i in ch:
#     if i in vovel:
#         count+=1
#     else:
#         c_count+=1
# print("vowels",count)
# print("consonants",c_count)


# • 3. Remove duplicate characters from a string.
# ch="yaseennppn"
# result=""
# for i in ch:
#     if i not in result:
#         result+=i
# print(result)


# • 4. Find the most frequent character in a string.
# s = input("Enter a string :")
# max_char = ""
# max_count = 0
# for ch in s:
#     count = s.count(ch)
#     # print(ch,count)
#     if count > max_count:
#         max_count = count
#         max_char = ch
# print("Most frequent character:", max_char)
# print("Frequency:", max_count)



# • 5. Check if two strings are anagrams.   
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# # ch1=s1.upper()
# # ch2=s2.upper()
# # if sorted(ch1) == sorted(ch2):
# if sorted(s1.upper()) == sorted(s2.upper()):
#     print("anogram")
# else:
#     print("not anogram")


# • 6. Reverse each word in a sentence without reversing the sentence order.
# s="Hello World Python"
# word=s.split()
# reves=""
# for w in word:
#     reves+=w[::-1]+" "
# print(reves)


# • 7. Find the longest word in a sentence.
# s=input("Sentence :")
# words=s.split()
# longest=words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest=word
# print(longest)


# • 8. Compress a string (example: aaabb → a3b2).
# ch=input("Enter :") 
# result=""
# for i in ch:
#     if i not in result:
#         count=ch.count(i)
#         result=result + i + str(count)
# print(result)


# • 9. Remove all spaces from a string.
# s=input("Sentence :")
# result=""
# for ch in s:
#     if ch !=" ":
#         result+=ch
# print(result)


# • 10. Convert the first letter of every word to uppercase without using title().
# s=input("Sentence :")
# result=""
# words=s.split()
# for word in words:
#     result=result+word[0].upper()+word[1:]+" "
# print(result)


# • 11. Extract digits from a string and store them separately.
# s="anbf8385"
# digit=""
# for ch in s:
#     if ch.isdigit():
#         digit+=ch
# print(digit)


# • 12. Count the number of words in a sentence.
# s="anbf8385"
# words=""
# for ch in s:
#     if ch.isalpha():
#         words+=ch
# print(words)


# • 13. Replace multiple spaces with a single space.
# s = "Python   is    easy  to   learn"
# result = " ".join(s.split())
# print(result)


# • 14. Check whether a string contains special characters.
# s="anbf2@#@8385"
# words=""
# for ch in s:
#     if not ch.isalnum():
#         words+=ch
# print(words)


# • 15. Find the ASCII value of each character.
# s = "yaseen"
# for ch in s:
#     print(ch, "=", ord(ch))

 
# Advanced / Real-world Tasks
# • 1. Encode and decode a string.
# • 2. Create a translation table using maketrans() and translate characters.
# s=input("Enter :")
# # print(s.translate({121:"¥",97:"丹",115:"丂",101:"⼹",110:"Ⓝ"}))  
# table = str.maketrans("abcdefghijk","ꥃᙫⓒᙄ⼹ꘘǤҤ𝔦ڶꝄ")                
# result = s.translate(table)
# print(result)

# print(ord("¶"))             #
# print(ord("§"))
# print(ord("y"))
# print(ord("¥"))
# print(ord("n"))

# table=s.maketrans("y")
# • 3. Simulate a simple password validator using string methods.
# • 4. Parse key-value pairs from a string like 'name=John;age=25'.
# • 5. Implement a simple email validation using string methods.
# • 6. Extract hashtags from a text.
# • 7. Mask sensitive data like phone numbers.
# • 8. Implement basic text formatting similar to markdown.

# • 9. Check if a sentence is a pangram.
# s=input("enter :")
# alphabets="abcdefghijklmnopqrsvwxyz"
# for ch in alphabets:
#     if ch not in s.lower():
#         print("Not an pangram")
#         break
# else:
#     print("pangram")


# • 10. Sort characters in a string alphabetically.
# s="yaseen"
# sort=sorted(s)
# print("".join(sort))

# Interview-Oriented Questions
# • 1. Explain the difference between find() and index() with code.
# • 2. Explain the difference between split() and rsplit() with examples.
# • 3. Explain the difference between strip(), lstrip(), and rstrip().
# • 4. Explain the difference between isdigit(), isnumeric(), and isdecimal().
# • 5. Check whether two strings are rotations of each other.


# s="fhfb dfh nfndk fnf"
# print(s.split())