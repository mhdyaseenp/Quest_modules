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



"""----------- 4.Modification or Replacement-----------"""

"""repalce()"""
# s="Python Django"
# s="Python Django Django Django"

# update=s.replace('D','d')                    #Python django
# update=s.replace('Django','Development')     #Python Development

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


"""estrip()"""
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

name='Mr.yaseen Mr.'
print(name.removesuffix('Mr.'))


