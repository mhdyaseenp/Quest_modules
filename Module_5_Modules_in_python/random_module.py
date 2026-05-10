# import random
# random.random()

from random import*

# print(random())                       #print random floting point numbers Eg:0.937195732382466
 
# print(randint(1,6))                   #andom integer in range [a, b].   Eg:4

# print(randrange(0,8,6))               #andom integer in range [start,stop,step].  Eg:2




# student=['yasee','jasil','shakir','shahal','richu']
# print(choice(student))                                      #Choose a random element from a itrable .
# print(choice("yaseen"))




# student=['yasee','jasil','shakir','shahal','richu']
# print(choices(student,k=3))                                  #Return a k sized list of population elements chosen with replacement.
# print(choices("yaseen",k=3))





# student=['yasee','jasil','shakir','shahal','richu']            #Shuffle list x in place, and return None.
# shuffle(student)
# print(student)

# name="yasen"
# shuffle(name)
# print(name)

# t=(1,3,4,5,4,3)                                                  #only support list
# shuffle(t)
# print(t)





# student=['yasee','jasil','shakir','shahal','richu']
# print(sample(student,k=2))



# Value=uniform(0,5)
# print(Value)

# rounded_value=round(Value,3)
# print(rounded_value)



# value=randint(0,100)
# print(value)
# user=int(input("Enter a random number :"))
# if value < user:
#     print("Too High")
# elif value > user:
#     print("Too loww....")
# else:
#     print("Congrats your the winner")
# print(value)



# "head or tail"
# result=choice(['head','tail'])
# print(result)



'otp'
num=randint(1,999999)
# num=303948384
otp=f"{num:06d}"
print(otp)