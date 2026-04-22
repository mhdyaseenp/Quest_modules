# def greet():
#     print("Hello world")
# greet()



# def greet(m,n,o):
#     print(f"Hello welcome {m},{n}")

# greet("yaseen",'jasil','shakir')


# def add(n1,n2):
#     return n1+n2
# res=add(12,2)
# print(res)


# def eligible(age):                        #function with return type
#     if age >25:
#         return "eligible"
#     else:
#         return "Not eligible"
# print(eligible(26))



# def to_upper(s:str) -> str:
#     """This function convert string to upper case"""
#     return s.upper()
# print(to_upper("Yaseen"))


# def details(name:str ,age:int,phone:list) -> dict :
#     """this function used to collect details from the user"""
#     return "My namae is",name,"Age is ",age,phone
# a=details("yaseen",22,[24552552,2552552])
# print(a)



# def details(name:str ,age:int, ph:list) -> dict :
#     """this function used to collect details from the user""".           #positional arg
#     print (name)
#     print(age)

# a=details(22,"yaseen",[24552552,2552552])
# print(a)



# def details(name: str, age: int, phon: list):
#     # """this function used to collect details from the user"""            #keyword Arg
#     print (name)
#     print(age)
#     print(phon)
# a=details(age=22,name="yaseen",phon=[24552552,2552552])
# print(a)



# def add(a=1,b=2,c=3):
#     return a+b+c                                                          #default arg

# print(add(4,5,6))
# print(add())

# def add(a=10,b=20):
#     return a+b                                                        #default arg

# print(add(4))
# print(add())



# def add(a,b):
#     return a+b
# print(add(2,3))


"""4 Arbitary arg"""


# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(add(2))                       #2
# print(add(2,23,5,35,53,2,23,1))     #144


# def detals(**kwargs):
#     return kwargs
# print (detals(name='yaseen',aga=22))
# print (detals(name='jasil',aga=32,place='Adv'))
# print (detals(name='shakir',aga=22,place='pay',phone=24958392940))



# def detals(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# detals(name='yaseen',aga=22)
# detals(name='jasil',aga=32,place='Adv')
# detals(name='shakir',aga=22,place='pay',phone=24958392940)




# def even(**args):

#     for i in args:
#         if i%2==0:
#             print(i)
            
# even(2,23,5,35,53,2,23,22,4,6,8,10,1)
# print(2,23,5,35,53,2,23,22,4,6,8,10,1)
