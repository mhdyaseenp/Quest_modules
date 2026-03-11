
# a="qest"
# b="calicut"
# a,b = b,a
# print(a)
# print(b)

# ch=input("Enter string:")
# # rev=ch[::-1]
# # if ch==rev:
# if ch==ch[::-1]:
#     print("Palindrom")
# else:
    # print("Not an Palindrom")


# • 4. Find the most frequent character in a string.
# s=input("ENter the string :")
# result=""
# for ch in s:
#     if ch not in result:
#         count=s.count(ch)
#         if count >1:
#             print(ch,count)
#         result+=ch

# s="hello world"
# for i in range(len(s)):
#     count=0
#     for j in range(len(s)):
#         if s[i]==s[j]:
#             count+=1
#     print(s[i],":",count)

# from collections import Counter
# s="hello world"
# print(Counter(s))


# First repeating charecter in string
# s=input()
# result=""
# for ch in s:
#     if ch in result:
#         print(ch)
#         # break
#     else:
#         result+=ch

# s="programming"
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i]!=s[j]:
#             print("first repeat charecter :",s[i])
#             break


# First non repeating charecter in string
# s = "pprogramming"

# for ch in s:
#     if s.count(ch) == 1:
#         print("First non repeating character:", ch)
#         break