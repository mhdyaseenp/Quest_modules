# t1=(15,0.5,'saple text',[1,4,53,5])
# print(t1)
# print(type(t1))


# sapmle=tuple()
# print(type(sapmle))

# t2=(2)
# t22=(2,)
# print(type(t2))             #int
# print(type(t22))            #tuple

#indexing
# t1=(15,0.5,'saple text',[1,4,53,5])
# print(t1[0])
# print(t1[-1])

""""Add&Updat"""

#using += 
# t1 = (15,0.5,'saple text',[1,4,53,5])
# t1 += (60,)
# print(t1)



#convert into list and update vallues
# t1=(15,0.5,'saple text',[1,4,53,5])
# sample_list=list(t1)

# sample_list.append(50)
# t1=tuple(sample_list)
# print(t1)


"""#Unpaking"""
# person=('richu','shabin','shahal','yaseen')
# *p1,p2,p3=person                
# print(p1)                       #['richu', 'shabin']
# print(p2)                       #shahal
# print(p3)                       #yaseen

#add using unpaking
# person=('richu','shabin','shahal','yaseen')
# person=(*person,'niyas','jasil')
# print(person)

#Delete a tuple
# person=('richu','shabin','shahal','yaseen')
# del person
# print(person)               #output will be error


"""slice"""
# person=('richu','shabin','shahal','yaseen')
# print(person[1::])
# print(person[-1])
# print(person[::-1])


# person=('richu','shabin','shahal','yaseen')
# for p in range(len(person)):
#     print(p," : ",person[p])


# person=('richu','shabin','shahal','yaseen')
# i=0
# while i < len(person):
#     print(person[i])
#     i+=1




#inbuild functions
# person=('richu','shabin','shahal','yaseen')
# print(dir(person))

"""colunt()"""
# print(person.count('jasil'))                #0
# print(person.count('yaseen'))               #1

"""index()"""
# print(person.index('jasil'))                #error
# print(person.index('yaseen'))               #3



 

# person=('richu','shabin','shahal','yaseen')
# print(person * 3)



# person=('richu','shabin','shahal','yaseen')
# print('sree' not in person)
# print('yaseen' not in person)