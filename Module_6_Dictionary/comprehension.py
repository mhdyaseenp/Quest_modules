'Dictionary Comprehension'


# squared_dict = {x : x**2 for x in range(1,11)}
# print(squared_dict)                               # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# even_squared_dict = {x : x**2 for x in range(1,11) if x%2==0}
# print(even_squared_dict)                                                # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}



# alphanum_dict = { 'a' : 1 , 'b' : 2 , 'c' : 3 , 'd' : 4}
# new_dict = { k : v for k,v in alphanum_dict.items() if v%2 == 0}
# print(new_dict)                                                          # {'b': 2, 'd': 4}




# alphanum_dict = { 'a' : 1 , 'b' : 2 , 'c' : 3 , 'd' : 4}
# new_dict = { v : k for k,v in alphanum_dict.items()}
# print(new_dict)                                                             # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}



alphabets = ['a','b' ,'c' ,'d' ]
new_dict = { x : ord(x) for x in alphabets}
print(new_dict)                                       # {'a': 97, 'b': 98, 'c': 99, 'd': 100}


'odd aneel Qube'
'even aneel Square'



sample = [1, 2, 3, 4, 5, 6, 7, 8, 10]
new_dict = {i : i**2 if i %2 ==0 else i ** 3 for i in range(1,11)}
print(new_dict)