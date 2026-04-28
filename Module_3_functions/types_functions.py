
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




