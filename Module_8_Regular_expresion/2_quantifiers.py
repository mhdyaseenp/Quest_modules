import re
 
# data ='My name is yaseen.Iam from Malappuram, My phonr number is 9037279877'
# result=re.search(r'yaseen',data)
# print(result.group())

# print(result.start())                  #11
#                                             #the start()  and end() only work with search()
# print(result.end())                    #17

# print(result.span())                   # (11, 17) both staring and ending  



"""quantifiers {}"""
# {n}                  exactly n times
# {n,}                 minimum n
# {n,m}                minimum n, maximum m
# {,m}                 maximum m


# data ='My name is yaseen.Iam from Malappuram, My phonr number is 9037279877'
# result=re.findall(r'\d{10}',data)
# print(result)


# data ='q e My name is yaseen.Iam from Malappuram, My phonr number is 9037279877'
# # result=re.findall(r'\w{2,}',data)                                               #minimum 2,['My', 'name', 'is', 'yaseen', 'Iam', 'from', 'Malappuram', 'My', 'phonr', 'number', 'is', '9037279877']
# result=re.findall(r'\w{2,5}',data)                                                #minimum 2 maximum 5,['My', 'name', 'is', 'yasee', 'Iam', 'from', 'Malap', 'puram', 'My', 'phonr', 'numbe', 'is', '90372', '79877']
# print(result)



# data ='q e My name is yaseen.Iam from Malappuram, My phonr number is 9037279877'
# print(len(data))
# result=re.findall(r'\d{,2}',data)
# print(len(result))
# print(result)

"""+"""
#atleast one 
#apple+    appple False     appplee True       apppleess True

# data ='q e My name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877'
# # result=re.findall(r'\d+',data)                                              #\d+  atleast 1 ['23', '3', '353', '3', '9037279877']

# # result=re.findall(r'\w+3',data)                                               #\w+3   after the alpha numeric  its end in 3   ['23', 'e3e353', 'number3', '903']


# print(result)



"""*"""
#zero or more   
# apple*    appple True     appplee True       apppleess True

# data ='q e My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877'                                          
# result=re.findall(r'\w*',data)                                               
# print(result)


"""?"""
#zero or one
#appple?    appple True     appplee True       apppleess False

# data ='q e My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877'

# result=re.findall(r'\w\w?',data)

# print(result)








test_str='a ab abc abbc abbcc abbbccc abbbcccc'
# result=re.findall(r'a\w*',test_str)                 #['a', 'ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'abbbcccc']
# result=re.findall(r'a\w+',test_str)                 #['ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'abbbcccc']
result=re.findall(r'a\w?',test_str)                 #['a', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']
print(result)