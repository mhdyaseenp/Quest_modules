# PYTHON FULL STACK TRAINING: DICTIONARY LOGIC &
# INTERVIEW PREP
# Topic: Key-Value Pairs, JSON-like Structures, and Data Mapping
# --- PART 1: DICTIONARY BASICS & CREATION ---
# 1. Create a dictionary representing a 'Laptop' with keys: brand, model, and price.
# laptop ={
#     'Brand':'Hp',
#     'Model':'Victus',
#     'Price':'56k'
# }
# print(laptop)


# 2. Access the value of the 'model' key using square brackets.
# laptop ={
#     'Brand':'Hp',
#     'Model':'Victus',
#     'Price':'56k'
# }
# print(laptop['Model'])


# 3. Access the value of a key that doesn't exist using .get() and explain why it's safer than [].
# 4. Create an empty dictionary using both {} and the dict() constructor.

# 5. Add a new key-value pair 'processor': 'i7' to an existing dictionary.
# laptop ={
#     'Brand':'Hp',
#     'Model':'Victus',
#     'Price':'56k'
# }
# laptop['processor']='i7'

# print(laptop)


# 6. Update the 'price' of the laptop to a new value.
# laptop ={
#     'Brand':'Hp',
#     'Model':'Victus',
#     'Price':'56k'
# }
# laptop['processor']='i7'
# laptop['Price']='45k'

# print(laptop)


# 7. Use the len() function to find how many key-value pairs are in a dictionary.

# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# print(len(laptop))


# 8. Create a dictionary where the keys are numbers 1 to 5 and the values are their squares.
# num={ c:c**2 for c in range(1,6)}
# print(num)


# 9. Check if a specific key exists in a dictionary using the 'in' operator.
# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# if "Brand" in laptop:
#     print("exist")
# else:
#     ("nort")


# 10. Delete a key-value pair using the  'del' keyword and handle the case if the key is missing. 
# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# del laptop['Model']
# print(laptop)

# --- PART 2: METHODS & MANIPULATION ---
# 11. Use the pop() method to remove a key and store its value in a variable.
# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# value=laptop.pop('Price')
# print(value)
# print(laptop)

# 12. Use popitem() to remove the last inserted item and explain its behavior in Python 3.7+.
# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# item=laptop.popitem()
# print(item)
# print(laptop)


# 13. Use the keys() method to print all the keys in a dictionary.
# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# for k in laptop.keys():
#     print(k)


# 14. Use the values() method to print all the values in a dictionary.
# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# for v in laptop.values():
#     print(v)


# 15. Use the items() method to iterate through a dictionary and print "Key: Value" for each
# pair.
# laptop={
#     'Brand': 'Hp', 
#     'Model': 'Victus', 
#     'Price': '45k', 
#     'processor': 'i7'
# }
# for k,v in laptop.items():
#     print(k,":",v)


# 16. Merge two dictionaries: {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using the update() method.
# dict1={'a': 1, 'b': 2}
# dict2={'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)


# 17. Clear all items from a dictionary using the clear() method.
# dict1={'a': 1, 'b': 2}
# dict1.clear()
# print(dict1)


# 18. Use the setdefault() method to add a key 'country' with value 'India' only if it doesn't exist.
# person = {
#     'name': 'Yaseen',
#     'age': 22
# }
# person.setdefault('Contry','India')
# print(person)


# 19. Create a shallow copy of a dictionary and show that modifying the copy doesn't change
# the original.
# person = {
#     'name': 'Yaseen',
#     'age': 22
# }
# copy_person=person.copy()
# copy_person['age']=33
# copy_person.setdefault('Place','Mlp')
# print(copy_person)
# print(person)


# 20. Create a dictionary from two lists: one for keys and one for values using the zip()
# function.
# key=['name','age','place']
# value=['yaseen',23,'Mlp']
# tot=zip(key,value)
# print(dict(tot))


# --- PART 3: NESTED DICTIONARIES (API STYLE) ---
# 21. Create a nested dictionary called 'Employees' containing data for three different people.
# employy={
#     'empl1':{
#         'name':'yaseen',
#         'age':23,
#         'place':'Mlp'
#     },
#     'empl2':{
#         'name':'shakir',
#         'age':26,
#         'place':'Knr'
#     },
#     'empl3':{
#         'name':'niyas',
#         'age':25,
#         'place':'Wnd'
#     },
# }
# print(employy)


# 22. Access a value inside a nested dictionary (e.g., Employees['emp1']['salary']).
# employy={
#     'empl1':{
#         'name':'yaseen',
#         'age':23,
#         'place':'Mlp'
#     },
#     'empl2':{
#         'name':'shakir',
#         'age':26,
#         'place':'Knr'
#     },
#     'empl3':{
#         'name':'niyas',
#         'age':25,
#         'place':'Wnd'
#     },
# }
# print(employy['empl1']['name'])

# 23. Update a value inside a nested dictionary.
# employy={
#     'empl1':{
#         'name':'yaseen',
#         'age':23,
#         'place':'Mlp'
#     },
#     'empl2':{
#         'name':'shakir',
#         'age':26,
#         'place':'Knr'
#     },
#     'empl3':{
#         'name':'niyas',
#         'age':25,
#         'place':'Wnd'
#     },
# }
# employy['empl2']['name']='jasil'
# print(employy['empl2']['name'])
# print(employy)


# 24. Add a new nested dictionary (a new employee) to the existing 'Employees' structure.
# employy={
#     'empl1':{
#         'name':'yaseen',
#         'age':23,
#         'place':'Mlp'
#     },
#     'empl2':{
#         'name':'shakir',
#         'age':26,
#         'place':'Knr'
#     },
#     'empl3':{
#         'name':'niyas',
#         'age':25,
#         'place':'Wnd'
#     },
# }

# employy['empl4']={
#     'name':'jasil',
#     'age':25,
#     'place':'clt'
# }
# print(employy)


# 25. Write a loop to print only the names of all employees from the nested 'Employees'
# dictionary.
# employy={
#     'empl1':{
#         'name':'yaseen',
#         'age':23,
#         'place':'Mlp'
#     },
#     'empl2':{
#         'name':'shakir',
#         'age':26,
#         'place':'Knr'
#     },
#     'empl3':{
#         'name':'niyas',
#         'age':25,
#         'place':'Wnd'
#     },
# }
# for vl in employy.values():
#     print(vl['name'])
    # print(vl)


# 26. Create a dictionary where a key points to a list of values (e.g., 'hobbies': ['coding',
# 'reading']).
# person = {
#     'name': 'Yaseen',
#     'age': 22,
#     'hobbies': ['coding', 'reading', 'riding']
# }
# print(person)

# 27. Append a new hobby to the list inside that dictionary.
# person['hobbies'].append('gaming')
# print(person)


# 28. Given a dictionary of students and their marks (a list), calculate the average marks for one
# student.
# students = {
#     'Yaseen': [80, 85, 90],
#     'jail': [70, 75, 78],
#     'niyas': [88, 92, 84]
# }
# marks=students['Yaseen']
# avg=sum(marks)/len(marks)
# print(avg)

# total=0
# for m in marks:
#     total+=m
# avg=total/len(marks)
# print(avg)


# 29. Flatten a simple nested dictionary (convert {'a': {'b': 1}} to {('a', 'b'): 1}).
# data = {
#     'a': {'b': 1}
# }
# flat={}
# for oute_k,inner_d in data.items():
#     for inner_k,value in data.items():
#         flat[(oute_k, inner_k)] = value
# print(flat)


# 30. Represent a JSON response from a weather API as a nested dictionary and extract the
# 'temperature'.
# data={
#     'location':{
#         'city':'calicut',
#         'country' : 'India'
#     },
#     'current':{
#         'tempreture':32,
#         'humdity':90,
#         'weather':'sunny'
#     }
# }
# print(data['current']['tempreture'])

# --- PART 4: COMPREHENSIONS & LOGIC ---

# 31. [Comprehension] Create a dictionary of even numbers between 1-10 as keys and their
# cubes as values.
# valu={k:k**3 for k in range(1,11) if k%2==0}
# print(valu)


# 32. [Comprehension] Given a dictionary, create a new one with only items where the value is > 100.
val={'a':10,'b':300,'c':23,'d':110}
# filter={k:v for k,v in val.items() if v>100}
# print(filter)
# print({k:v for k,v in val.items() if v>100})


# 33. [Comprehension] Swap keys and values in a dictionary (Reverse Mapping).
# val={'a':10,'b':300,'c':23,'d':110}
# swp={v:k for k,v in val.items()}
# print(swp)


# 34. Sort a dictionary by its keys in alphabetical order.
# data = {'banana': 3, 'apple': 5, 'cherry': 42}
# itm=list(data.items())
# itm.sort()
# sort_dict=dict(itm)
# print(sort_dict)


# 35. Sort a dictionary by its values in ascending order.
# data = {'banana': 3, 'apple': 5, 'cherry': 42,'grape':2}
# sorted_dict={}
# values=list(data.values())
# values.sort()
# for value in values:
#     for key in data.keys():
#         if data[key]== value and key not in sorted_dict:
#             sorted_dict[key]=value
# print(sorted_dict)


# 36. Find the key with the maximum value in a dictionary of product prices.
# products = {'banana': 30, 'iphone': 50000, 'laptop': 90000,'bag':1200}
# keys=list(products.keys())

# max_k=keys[0]
# max_v=products[max_k]

# for key in products.keys():
#     if products[key] > max_v:
#         max_v=products[key]
#         max_k=key

# print(f"{max_k}:{max_v}")



# 37. Count the frequency of each character in a string "Python Trainer" using a dictionary.
# text = "yaseen"
# # text = "Python Trainer"
# freq={}
# for chr in text:
#     if chr in freq:
#         freq[chr]=freq[chr] + 1
#     else:
#         freq[chr]=1
# print(freq)


# 38. Combine two dictionaries by adding values for common keys.
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 5, 'c': 15, 'd': 40}
# result = {}
# for key in d1:
#     result[key] = d1[key]
# for key in d2:
#     if key in result:
#         result[key]=result[key] + d2[key]
#     else:
#         result[key] = d2[key]
# print(result)



# 39. Convert a dictionary into a list of tuples.
# data = {'a': 10, 'b': 20, 'c': 30}
# result=[]

# for k in data.keys():
#     result.append((k,data[k]))
# print(result)


# 40. Check if all values in a dictionary are the same.
# data = {'a': 10, 'b': 10, 'c': 10}
# values=list(data.values())
# first=values[0]
# same="yes"

# for v in values:
#     if v !=first:
#         same=False
#         break
# print(same)


# --- PART 5: INDUSTRIAL & INTERVIEW SCENARIOS ---

# 41. [JSON] Use the 'json' module to convert a dictionary into a JSON string.
# 42. [Data Cleaning] Remove all keys from a dictionary that have None or empty string
# values.
# 43. [Security] Explain why a list cannot be used as a dictionary key, but a tuple can.
# 44. [Logic] Write a program to find the sum of all values in a numeric dictionary.
# 45. [Simulation] Use a dictionary to simulate a simple "Switch-Case" statement logic.
# 46. [Efficiency] Compare the time it takes to find a value in a list of 10,000 items vs. a
# dictionary.
# 47. [Functionality] Use **kwargs in a function to accept arbitrary keyword arguments as a
# dictionary.
# 48. [Mapping] Create a dictionary to map Roman numerals to Integers (e.g., 'I': 1, 'V': 5).
# 49. [Logic] Given a list of words, group them by their starting letter using a dictionary.
# 50. [Interview Question] Explain the difference between '==' and 'is' when comparing two
# identical dictionaries.


a=[10,20,20,30,40,50,50,60,60]
res=[]
dup=[]
for n in a:
    if n not in res:
        res.append(n)


for i in a:
    if i in a:
        dup.append(n)

print(f"duplicate removes {dup}")

# print(f"Orginal {a}")
# print(f"duplicate removes {res}")



