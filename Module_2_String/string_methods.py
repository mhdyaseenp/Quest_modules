"""--------------------------String Methods in Python--------------------------"""

# company="qis"             #dir is used to check the datatypes inbuild mathods
# print(dir(company))

"""----------- 1. Case Conversion Method-----------"""
"""Upper()"""
# name="muhammned Yaseen"
# print(name.upper())

"""Lover()"""
# name="MUHAMMED Yaseen"
# print(name.lower())

"""title()"""
# name="MUHAMMED yaseen p"
# print(name.title())             #Muhammed Yaseen 

"""capitalize()"""
# s="hello iam yasee ,"           #Hello iam yasee ,
# print(s.capitalize())

"""swapcase()"""
# s="yaSEEn p"
# print(s.swapcase())                #YAseeN P


"""----------- 2. Searching And Finding-----------"""

"""find()"""
# ch="Python Django"
# print(ch.find("D"))         #print D index                       // 7
# print(ch.find("thon"))      #print first letters  index          // 2
# print(ch.find("o"))         #print first o (there is 2 o) index  // 4
# print(ch.find("z"))         #if check an undifined charecter     //-1

"""rfind()"""
# print(ch.rfind("o"))         #check right to left (find() willl chek left to right). //12
# print(ch.rfind("thon"))
# print(ch.find("y"))

"""index()"""
# print(ch.index("h"))
# print(ch.index("ang"))
# print(ch.index("o"))
# print(ch.index("z")).       #error in find it will be -1

"""rindex()"""
# print(ch.rindex("o"))

"""count()"""
# ch="my name is ysaeethon ,my fav lang python"
# print(ch.count("my"))       #2
# print(ch.count("is"))       #1
# print(ch.count("on"))       #2
# print(ch.count("e"))        #3


"""----------- 3.Validation or Checking-----------"""

"""isalpha()"""
# s="Python"                          #only alphabets
# print(s.isalpha()) 
#       

"""isdigit()"""
# s="1234"                            #only digits
# print(s.isdigit())     


"""isalnum()"""
# s="1234"                            #only digits and alphabets
# print(s.isalnum())     


"""isalnum()"""
# s=" "                                #only white space
# print(s.isspace())     
   

"""isdecimal()"""
# s="123"                              #only base 10 values 
# print(s.isdecimal())     
   

"""isupper()"""
# s="DIIED1M"                           #only upper case includes digits
# print(s.isupper())     
   

"""islower()"""
# s="and@bn"                            #only lower case includes digits
# print(s.islower())     


"""istitle()"""
# s="Quest@ Solution12@"                #words first letter is Uppercase
# print(s.istitle())     
   
"""istitle()"""
# s="Quest@ Solution12"        #TRUE      #words first letter is Uppercase
# print(s.isascii())     
# s="Quest@ Solution12😩"      #FALSE     #words first letter is Uppercase
# print(s.isascii())     
   

"""startswith()"""
# s="Quest@ Solution12@"                  #Start with substring eg:- "Q"
# print(s.startswith("Quest"))   


"""endswith()"""
# s="Quest@ Solution12@"                  #Ends with substring eg:- "@"
# print(s.endswith("@"))     
   


"""----------- 4.Modification or Replacement-----------"""

"""replace()"""
# s="Python Django"
# s="Python Django Django Django"

# update=s.replace('D','d')                     #Python django
# update=s.replace('Django','Development')      #Python Development

# update=s.replace(' ','_')                      #Python_Django_Django_Django
# update=s.replace('Django','Development',2)     #Python Development Development Django.  //change first 2

# print(update)

"""strip()"""
# string="     hello django        "
# print(string)
# print(string.strip())
# string="--------hello django--------"
# print(string.strip('-'))

# string="0000000hello django00000000"
# print(string.strip('0'))

# string="aaaaaaa hello django aaaaaa"
# print(string)
# print(string.strip('a'))

# string="abcabcabc hello django aaaaaa"
# print(string)
# print(string.strip('abc'))


"""lstrip()"""
# # remove lefts
# string="abcabcabc hello django aaaaaa"
# print(string)
# print(string.lstrip('abc'))


"""rstrip()"""
# remove rights
# string="aaaaaaaa hello django aaaaaa"
# print(string)
# print(string.rstrip('abc'))


"""removeprefix()"""
# left to right
# name='Mr.yaseen'
# print(name.removeprefix('Mr.'))
# print(name.removeprefix('m'))


"""removesuffix()"""
# right to left

# name='Mr.yaseen'
# print(name.removesuffix('Mr.'))
# print(name.removesuffix('een'))

# name='Mr.yaseen Mr.'
# print(name.removesuffix('Mr.'))



"""----------- 5.Formating and Alignment-----------"""

"""center"""
# s="Python"                       
# print(s.center(25,'*'))          #center align


"""ljust"""
# s="Python"  
# print(s.ljust(25,"⬅️"))            #left align


"""rjust"""
# s="Python"  
# print(s.rjust(25,"😁"))           #left align


"""zfill"""
# s="Python"  
# print(s.zfill(10))                 #padd with zeros


"""format"""
# name="Yaseen"                        #format placeholder
# age=24 
# # print("My name is {} and iam {} year old".format(name,age))        #My name is Yaseen and iam 24 year old
# # print("My name is {} and iam {} year old".format(age,name))        #My name is 24 and iam Yaseen year old      
# # print("My name is {1} and iam {0} year old".format(age,name))      #My name is Yaseen and iam 24 year old    

# print("My name is {:<10} and iam {} year old".format(name,age))      #My name is Yaseen     and iam 24 year old    
# print("My name is {:^10} and iam {:05} year old".format(name,age))   #My name is   Yaseen   and iam 00024 year old 


"""f-string"""
# name="Yaseen"                        
# age=24 
# print(f"My name is {name} and iam {age} year old") 

"""row-string"""
# name="Yaseen"                        
# age=24 
# print(f"My name is {name} \t and iam {age} year old")                  #My name is Yaseen        and iam 24 year old
# print(r"My name is {name} and iam {age} year old")                     #My name is {name} and iam {age} year old

#Extraaa
# print("''")
# print("""")            # Error
# print("\"\"")            # ""



"""----------- 6.Splittting and Joinning-----------"""

"""split()"""
# s="welcone to the world of python"                 #split a string      //output is a list   
# print(s.split())                                   #['welcone', 'to', 'the', 'world', 'of', 'python']
# print(s.split(" ",3))                              #['welcone', 'to', 'the', 'world of python']

# s="welcone-to-the-world-of-python"                
# print(s.split("-"))                                #same as above
# print(s.split("-",3))                              #['welcone', 'to', 'the', 'world-of-python']

# print("hello".split("l"))                          #['he', '', 'o']
# print("helllo".split("l"))                         #['he', '', '', 'o']


"""rsplit()"""                                      #split left to righr
# s="welcone to the world of python"                #split a string      //output is a list   
# print(s.rsplit(" ",3))                            #['welcone to the', 'world', 'of', 'python']


"""join()"""                                      #split left to righr
# s="welcone to the world of python"  

# split=s.split()                                   #Split the the words
# print(split)                                      #'welcone', 'to', 'the', 'world', 'of', 'python']


# jointed_string=" ".join(split)                    #join splited list the the words
# print(jointed_string)                             #welcone to the world of python

# print(" ".join(split))


"""partition()"""
# s="job = python"
# print(s.partition("="))                           #('job ', '=', ' python')


# s="job=python"
# print(s.partition("python"))                      #('job ', '=', ' python')

# s="python"
# print(s.partition("python"))                      #('', 'python', '')
# s="python"
# print(s.partition("x"))                           #('python', '', '')


# s="my name is yaseen"
# print(s.partition(" "))                           #('my', ' ', 'name is yaseen')


"""rpartition()"""
# s="my name is yaseen"
# print(s.rpartition(" "))                            #('my name is', ' ', 'yaseen')



"""----------- 7.Encoding and Decoding-----------"""

"""encode()"""      
# s="hello"                                               #convert string to byte code
# print(s.encode())                                       #b'hello'
# print(s.encode(encoding="utf-8",errors="strict"))            


"""encode()"""  
# s="hello"                                               #convert string to byte code
# encode_s=s.encode()
# print(encode_s)                                         #b'hello'
# decode_s=encode_s.decode()                              
# print(decode_s)                                         #hello



"""----------- 8.Miscellaneous -----------"""

"""expandtabs()"""
print("hello \t python")
# print("hello \t python".expandtabs(10)
# print("hello \t python".expandtabs(23))  
            #syntax:-  [spases=tabsize-(current_position / tabsize)]
# print(len("hello \t python".expandtabs(34)))
# print(len("hello \t python".expandtabs(24)))
# print(len("hello \t python".expandtabs(10)))          


"""translate()"""
# s="yaseen"
# print(s.translate({97:'x',101:'z'}))            #we change the a to x a ascii value is 97 we set 97 to x so the givens strings all a change to x 
#                                                 #yxszzn


# y="hello world"
# print(y.translate({111:"0",108:"!"}))                   #hell0 w0rld
# print(y.translate({111:"0"}))                           #he!!0 w0r!d

# print(chr(111))
# print(ord("!"))
# print(ord("1"))

"""maketrans"""
# s="xxxxyyyyyzzzzz"
# table=s.maketrans('x','z',)                         #zzzzyyyyyzzzzz
# print(s.translate(table))

# s="xxxxyyyyyzzzzz"
# table=s.maketrans('x','z','y')                      #zzzzzzzzz
# print(s.translate(table))


# s="yaseen"
# table=s.maketrans('y','m','en')                     #mas
# print(s.translate(table))


# s="sreeraj"
# table=s.maketrans('sr','xy','e')                     #xyyaj         // s=x and  r=y
# print(s.translate(table))


# s="sreersaj"
# table=s.maketrans('sr','xy','e')                     #xyyxaj         // s=x and  r=y
# print(s.translate(table))


# s="cdalgh"
# table=s.maketrans('abcdefghi','ABCDEFGHI')              #CDAlGH         
# print(s.translate(table))




# split and join
# replase and strip 
# prefix and sufix
# upper ,lower and title
# full in validation and cheking
# index and find
# count