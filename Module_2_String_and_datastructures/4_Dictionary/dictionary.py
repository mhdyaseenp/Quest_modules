# details ={}
# print(type(details))

# details={'name':'yaseen','age':22,'place':'Clt'}
# print(details)


# details={'name':'yaseen','age':22,'place':'Clt','name':'niyas','name':'shakir'}             # its allow duplucate values does not allow duplicate key
# print(details)                                                                              #{'name': 'shakir', 'age': 22, 'place': 'Clt'}

# Data types in key

# sample_dit={1:'a',2:'b',3:'a',4.11:'d',}
# print(sample_dit)

# sample_dit={1:'a',2:'b',3:'a',4.11:'d',[1,2,4]:'e'}                     #set cant give as key value
# print(sample_dit)


# sample_dit={1:'a',2:'b',3:'a',4.11:'d',(1,2,4):'e'}                     #{1: 'a', 2: 'b', 3: 'a', 4.11: 'd', (1, 2, 4): 'e'}
# print(sample_dit)


# sample_dit={1:'a',2:'b',3:'a',4.11:'d',{1:'yase'}:'e'}                   #dict cant give as key value
# print(sample_dit)




# Data types in values // allow all type 
# sample_dit={'a':(1,23,4),'b':{1,23,4,5},'c':{1:'yaseen'},'d':[1,2,3,4]}
# print(sample_dit)



# student={'name':'yaseen','age':21,'batch':'python'}
# print(len(student))

# to add new key value pair
# student['place']='Clt'

# to add new key value pair
# student['name']='shakir'
# print(student)

# student.update({'rollno':66,'domain':['react']})
# print(student)

# student['domain'].append('MERN')
# print(student)

  
# student={'name': 'yaseen', 'age': 21, 'batch': 'python', 'rollno': 66, 'domain': ['react', 'MERN']}
# print(student['teacher'])h
# print(student.get('teacher'))                                     #none
# print(student.get('teacher','key dosen\'t exist'))
# print(student.get('name','key dosen\'t exist'))

# del
# del student
# print(student)


# del student['rollno']
# print(student)


# student={'name': 'yaseen', 'age': 21, 'batch': 'python','place':'Clt' ,'rollno': 66, 'domain': ['react', 'MERN']}
# student.pop('place')
# print(student)

# pop()
# p=student.pop('place')
# print(p)
# print(student)

# popitem()
# student={'name': 'yaseen', 'age': 21, 'batch': 'python','place':'Clt' ,'rollno': 66, 'domain': ['react', 'MERN']}
# student.popitem()
# print(student)                                                    #remove last item


# student={'name': 'yaseen', 'age': 21, 'batch': 'python','place':'Clt' ,'rollno': 66, 'domain': ['react', 'MERN']}
# student.clear()
# print(student)                                          #empty dict


student={'name': 'yaseen', 'age': 21, 'batch': 'python','place':'Clt' ,'rollno': 66, 'domain': ['react', 'MERN']}
 
# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)

# for k,v in student.items():
#     print(k,":",v)


print(student.keys())
print(student.values())
print(student.items())