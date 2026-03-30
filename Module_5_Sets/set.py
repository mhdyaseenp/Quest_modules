# sample_set={}
# print(type(sample_set))                        #it will be show as dict

# sample_set=set()
# print(type(sample_set))                       #it will be show as set


# s={1,4,2,3,1.4,'yaseen','jasil'}
# print(type(s))
# print(s)

# s={1,4,2,3,1.4,'yaseen','jasil','yaseen'}                 #does not allow duplicate elements
# print(type(s))
# print(s)

 
# s={1,4,2,3,1.4,'yaseen','jasil','yaseen',[1,2,3,4]}       #we cannot give list and set  in a set
# print(type(s))
# print(s)

 
# s={1,4,2,3,1.4,'yaseen','jasil','yaseen',(1,2,3)}         #we give tuple in a set
# print(type(s))
# print(s)

 
# numbers=set({100,200,300,400,500})
# print(numbers)


# sample_list=[10,20,30,40,10,20,50,60,30]
# updated_list=set(sample_list)
# print(updated_list)


# string=set("yaseen")
# print(string)

# s={1,4,2,3,1.4,'yaseen','jasil','yaseen',(1,2,3)}         
# print(s[5])                                                 #//error bcs set doesnot support indexing


# s={1,4,2,3,1.4,'yaseen','jasil','yaseen',(1,2,3)}         
# # for index,value in enumerate(s):                            #syntax
# for i,j in enumerate(s):
#     print(i,j)



# s={1,4,2,3,1.4,'yaseen','jasil','yaseen',(1,2,3)}         
# print(list(enumerate(s)))                                   #[(0, 1), (1, 2), (2, 3), (3, 4), (4, 1.4), (5, (1, 2, 3)), (6, 'jasil'), (7, 'yaseen')]

# print(enumerate(s))                                         #<enumerate object at 0x1003fc4a0>

