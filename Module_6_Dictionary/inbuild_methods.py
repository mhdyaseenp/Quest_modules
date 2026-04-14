'inbuild methods'

# fromkeys
# jasil = [ 'a', 'b' , 'c']
# d = dict.fromkeys(jasil)
# print(d)                                    # {'a': None, 'b': None, 'c': None}


'fromkeys'
# jasil = [ 'name', 'age' , 'place']
# d = dict.fromkeys(jasil, 'Not Available')
# print(d)                                   # {'name': 'Not Available', 'age': 'Not Available', 'place': 'Not Available'}


'setdefault'

# details = { 'name' : 'jasil' , 'age' : 22}

# result = details.setdefault('name')
# result1 = details.setdefault('place' , 'Adivaram')

# print(result)                                               # jasil
# print(result1)                                              # Adivaram
# print(details)                                              # {'name': 'jasil', 'age': 22, 'place': 'Adivaram'}


'zip'
# 2 list vech dictionary ndaakan

# a = [ 1, 2, 3 ,8,9]
# b = [ 10, 20, 30,50]

# c = zip(a,b)
# c1 = dict(zip(a,b))

# print(c)                        # <zip object at 0x0000028B4F929A80>

# print(dict(c))                      
# print(c1)                       # {1: 10, 2: 20, 3: 30}





# a = [ 'name' , 'age' , 'place']
# b = [ 'jasil' , 22 , 'Adivaram']

# c = dict(zip(a,b))
# print(c)                          # {'name': 'jasil', 'age': 22, 'place': 'Adivaram'}