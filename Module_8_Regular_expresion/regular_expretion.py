import re


"""search()"""
# entire string scan and print first occurence
#Scan through string looking for a match to the pattern, returning a Match object, or None if no match was found

# data='my phonr number is 9037279877'                              #<re.Match object; span=(19, 22),match='903'>
# data='my phonr number is 90jddfjslk37279877'                      #<re.Match object; span=(29, 32),match='372'>
# pattern= r'\d\d\d'

# result=re.search(pattern,data)
# print(result)
# print(result.group())                                             #372


"""# findall()"""
# Return a list of all non-overlapping matches in the string.

# data='my 248783 phonr number is 9037279877'
# # pattern= r'\d\d'
# pattern= r'\d'
# result2=re.findall(pattern,data)
# print(result2)




"""# findall()"""
#Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found. 

# data='my 248783 phonr number is 9037279877'                     #none
# data='83784 my 248783 phonr number is 9037279877'               #none
# # pattern= r'\d\d'
# pattern= r'\d\d'
# result3=re.match(pattern,data)
# print(result3.group())                                           #83




"""\d"""
# any single digit(0-9)


"""/D""" 
#any charecter that is not a digit

# data='my 248783 phonr number \n @ is ✅9037279877  879'
# pattern= r'\D\d'

# result2=re.findall(pattern,data)
# # result2=re.findall(r"\D",data)

# print(result2)



"""/w""" 
#any alphanumeric charecter + underscore

# data='my 248783 phonr number \n @ is ✅9037279877  879 ___-'
# pattern= r'\w'

# result2=re.findall(pattern,data)

# print(result2)




"""/W""" 
#any charecter not alphanumeric charecter + underscore

# data='my 248783 phonr number \n @ is ✅9037279877  879 ___-'
# pattern= r'\W'
# result2=re.findall(pattern,data)
# print(result2)



"""/s""" 
#any white space(space,tab.newline(\n))

# data='my 248        783 phonr number \n @ is ✅9037279877  879 ___-'
# pattern= r'\s'
# result2=re.findall(pattern,data)
# print(result2)




"""/S""" 
#any charecter that is not white space(space,tab.newline(\n))

# data='my 248        783 phonr number \n @ is ✅9037279877  879 ___-'
# pattern= r'\S'
# result2=re.findall(pattern,data)
# print(result2)



""".""" 
#any charecter except a newline(\n)

# data='my 248        783 phonr number \n @ is ✅9037279877  879 ___- yasee'
# pattern= r'y....'                                                           #['y 248', 'yasee']
# pattern= r'........'                                                           
# result2=re.findall(pattern,data)
# print(result2)






# work-out

# data='9894859 ojglf 485 +91 90372 79877 or moe +91 48587 45755'
# # pattern=r"\+91 \d\d\d\d\d \d\d\d\d\d"
# pattern=r"\+91 \d{5} \d{5}"
# res=(re.findall(pattern,data))
# print(res)