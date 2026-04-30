
"""1-Build In function"""
# eg:-
#     print()
#     len()
#     input(),etc....


"""2-user_defined Function"""

# def sum(a,b):
#     return a+b
# print(sum(5,10))



"""3-recursive_Function"""

# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# def rev(s):
#     if len(s)==0:
#         return(s)
#     return rev(s[1:])+s[0]
# print(rev('jasil'))


"""4-Lambda functijon"""
# sq=lambda a,b,c : print(a**2)
# sq(10,2,1)


# sq=lambda a: a**2
# print(sq(5))

# to sum a 3 numbers
# total=lambda a,b,c: a+b+c
# print(total(1,2,3))

# if else in lambda
# ev_od=lambda x: x**2 if x%2==0 else x**3
# print(ev_od(3))

# check the len of string
# str=lambda st: len(st)
# print(str("yaseen"))


# largest 2 number

# larag=lambda x,y: f"Largest is {x}" if x>y else f"Largest is{y}"
# print(larag(2,7))

# largest amoung 3
# largest=lambda a,b,c:f"largest is {a}" if a>b and a>c else f"laargest is {b}" if b>a and b>c else f"largesat is {c}"
# # print(largest(2,55,10))

# num1=int(input("1st :"))
# num2=int(input("2nd :"))
# num3=int(input("3rd :"))
# print(largest(num1,num2,num3))


# equal=lambda x,y: f"largest is {x}" if x>y else f"largest is {y}" if y>x else f"both are same"
# num1=int(input("1st :"))
# num2=int(input("2nd :"))
# print(equal(num1,num2))


# mult=lambda x :f"{x} is a multiple of both 3 and 5" if x%3==0 and x%5==0 else f"{x} is a multiple of 5" if x%5==0 else f"{x} is a multiple of 3" if x%3==0 else f"{x}not a multiple of both 3 and 5"
# num1=int(input("1st :"))
# print(mult(num1))




"""5 - Higher order Fuction"""
'map fuction '

# def square(nums : int) -> int:
#     return nums ** 2
# numbers = [1,2,3,4,5]



# result = map(square,numbers)
# print(result)                                   # <map object at 0x0000017CD2549A40>

# result = list(map(square,numbers))
# print(result)                                   # [1, 4, 9, 16, 25]



# Another wayy

# result2 = list(map(lambda x : x **2 ,numbers))
# print(result2)                                    # [1, 4, 9, 16, 25]

# print 5 multiplay only

# element = [1,5,10,14,45,35,16,20]

# result  = list(map(lambda x : x % 5 == 0 , element))
# print(result)                                               # [False, True, True, False, True, True, False, True]



# result2 = list(filter(lambda x : x % 5 == 0 , element))
# print(result2)                                              # [5, 10, 45, 35, 20]


# def vowel(word):
#     for ch in word:
#         if ch in 'aeiou':
#             return True
#     return False
    
# name = ['jasil', 'niyas', 'shakir' , 'yaseen']

# r= list(filter(vowel,name))
# print(r)




# sample_list = [0,{},[],5]
# print(any(sample_list))          # True
# print(all(sample_list))          # False




# names = ['jasil','yaseen','shakir','ssssss' ]
# result = list(filter(lambda x : any( ch in 'AEIOUaeiou' for ch in x), names))
# print(result)                                                                    # ['jasil', 'yaseen', 'shakir']



# print only gmail.com and apple.com

# emails = [
#     'jasilmuhammed25@gmail.com',
#     'yaseen256@yaho.com',
#     'shakir456@gmail.com',
#     'niyas123@yahoo.com',
#     'aflah@apple.com'
#     ]

# result = list(filter(lambda x: any(x.endswith(d) for d in ['gmail.com','apple.com']),emails))

# print(result)          # ['jasilmuhammed25@gmail.com', 'shakir456@gmail.com', 'aflah@apple.com']





# 1 - print multiplay of 3 only
# 2 - 3 multiplay to convert cube

# number = [3,6,5,8,9,12,13,9,15]

# result  = list(filter(lambda x : x % 3 == 0 , number))
# print("Multiple of 3 : " , result)                       # Multiple of 3 :  [3, 6, 9, 12, 9, 15]


# result1 = list(map(lambda y : y**3 , result))
# print("Cube :" , result1)                                                    # Cube : [27, 216, 729, 1728, 729, 3375]





# number = [3, 6, 5, 8, 9, 12, 13, 9, 15]

# result = list(map(lambda x: x ** 3, filter(lambda y: y % 3 == 0, number)))
# print(result)                                                                    # [27, 216, 729, 1728, 729, 3375]