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








# test_str='a ab abc abbc abbcc abbbccc abbbcccc'
# # result=re.findall(r'a\w*',test_str)                 #['a', 'ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'abbbcccc']
# # result=re.findall(r'a\w+',test_str)                 #['ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'abbbcccc']
# result=re.findall(r'a\w?',test_str)                 #['a', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']
# print(result)










# data ='My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎'

# pattern=r'[a-z]'                              #small leters onlt
# pattern=r'[A-Z]'                              #Capital leters onlt
# pattern=r'[A-z]'                              #small and capital
# pattern=r'[A-Za-z]'                           #small and Capital
# pattern=r'[0-9]{2}'                           #Numbers                              ['23', '35', '03', '72', '77']
# pattern=r'[0-9A-z]{3}'                        #Numbers And carectes of paired 3     ['nam', 'yas', 'een', '23v', 'e3e', '353', 'fro', 'Mal', 'app', 'ura', 'pho', 'num', 'ber', '903', '727', '987']


"""not [^]"""
# pattern=r'[^0-9A-Z]'                          #Not digits and Capital letters     
# pattern=r'[^0-9A-z]'                          #Not digits , Capital and small letters   ,get white spaces and  imojes


"""start(  r'^.....' ))  end( r'....$')"""
# pattern= r"^M"                                #startingil M indoo ennn chak chayyan ,non charecter annenkil empty set [] 
# pattern= r"😎$"                               #to check the given character is apperar at the end of the data


# result=re.findall(pattern,data)
# print(result)





"""Inbuild Functions"""

"""compile()"""


# data ='My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎'
# pattern=r'\d+'

# num=re.compile(pattern)

# result=num.findall(data)
# print(result)





# data ='My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎'
# name=r'yaseen'

# name_pattern=re.compile(name)

# result=name_pattern.findall(data)
# print(result)










"""sub()"""

# data ='My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎'

# # new_data= re.sub(r" ","💕",data)                                 #replace the space into imoji    My💕💕name💕is💕yaseen.Ia💕23💕💕e3e353💕m💕from💕Malappuram,💕My💕phonr💕number3💕is💕9037279877💕✅😎
# # new_data= re.sub(r" ","_",data)   
                                                       
# new_data= re.sub(r" ","✅",data,count=5)                          #replace the first 5 spaces     My✅✅name✅is✅yaseen.Ia✅23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎                                 

# print(new_data)






"""subn()"""
# its in a tuple format 

# data ='My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎' 
                                                       
# new_data= re.subn(r" ","✅",data)                                  #replace the first 5 spaces    ('My✅✅name✅is✅yaseen.Ia✅23✅✅e3e353✅m✅from✅Malappuram,✅My✅phonr✅number3✅is✅9037279877✅✅😎', 16)

# new_data= re.subn(r" ","✅",data,count=5)                          #replace the first 5 spaces    ('My✅✅name✅is✅yaseen.Ia✅23✅✅e3e353✅m✅from✅Malappuram,✅My✅phonr✅number3✅is✅9037279877✅✅😎', 5)

# print(new_data)





"""split()"""

data ='My  name is yaseen.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎' 
                                                       
# splited_data= re.split(r"e",data)                                  #['My  nam', ' is yas', '', 'n.Ia 23  ', '3', '353 m from Malappuram, My phonr numb', 'r3 is 9037279877 ✅😎']
# splited_data= re.split(r"e",data,maxsplit=3)                       #['My  nam', ' is yas', '', 'n.Ia 23  e3e353 m from Malappuram, My phonr number3 is 9037279877 ✅😎']

# print(splited_data)





