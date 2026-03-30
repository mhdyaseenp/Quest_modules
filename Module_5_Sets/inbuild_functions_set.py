"""Inbuild functions of set"""

# person={'yaseen','jasil','shony','shahal'}
# print(dir(person))


"""Add"""           #to add single value

# person={'yaseen','jasil','shony','shahal'}
# person.add('richu')                                 #we can add only one element
# print(person)


# person={'yaseen','jasil','shony','shahal'}
# person.add(tuple('jasim'))                                


"""update()"""

# person={'yaseen','jasil','shony','shahal'}
# person.update("shakir")
# print(person)

# person.update({10,200,'shakir'})                    #it will add every values in set
# print(person)



"""remove()"""

# person={'yaseen','jasil','shony','shahal'}
# person.remove("yaseen")                     
# print(person)                                       #{'jasil', 'shony', 'shahal'}

# person.remove("shakir")
# print(person)                                       #error


"""pop()"""

# person={'yaseen','jasil','shony','shahal'}
# person.pop()
# print(person)



"""discard()"""

# person={'yaseen','jasil','shony','shahal'}
# person.discard('shony')
# print(person)

# person.discard('shakir')
# print(person)


"""clear()"""

# person={'yaseen','jasil','shony','shahal'}
# person.clear()
# print(person)                                         #set()


