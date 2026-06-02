"""the raisse key word in pyhton is used to manually trigger an wxception it allows you
    to stop normal exicutions and signal that an error condition has occured 


    it allows developers to control error conditiond,enforce rules and create custom exceptions


    insted of waiting for python to throw an error automatically(like ZeroDivision Error) you can 
    explicitly raise one yourself

"""


# age=-5

# if age <0:
#     raise ValueError ("age can't be negative")



# mark=550
# if mark >200:
#     # raise ValueError("value must be less than or wqual to 200")
#     # raise ZeroDivisionError("value must be less than or wqual to 200")
#     raise ZeroDivisionError("value must be less than or wqual to 200")



# try:
#     mark=550
#     if mark >200:
#         raise ValueError("value must be less than or equal to 200")
# except Exception as e:
#     print(e)
#     # passs
    
# print("kjfd")




# try:
#     mark='550'
#     if int(mark) >200:
#         # raise ValueError("value must be less than or equal to 200")
#         pass
#     elif isinstance(mark,int):
#         raise TypeError("Mark can't be string")
# except Exception as e:
#     print(e)
#     # passs
    
# print("kjfd")






# class AgeError(Exception):
#     pass

# class VoteError(Exception):
#     pass

# # age=-5
# # if age<0:
# #     raise AgeError("Age can't be  negative")

# age=13
# if age>18:
#     raise VoteError("Age must be grater than 18")






num=int(input("Enter a positive number :"))

if num<=0:
    raise ValueError("Number must be positive")

print("square :",num*num)






