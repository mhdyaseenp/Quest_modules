# sample_list = []
# print(type(sample_list))

# sample_list = list()
# print(type(sample_list))

# sample_list = [1,2,3,'Quest',10,25,[7,8,9], True,None]
# print(sample_list)
# print(type(sample_list))

# sample_list = list(1,2,3)
# print(type(sample_list))
# print(sample_list)

# sample_list = ([1,2,3,'Quest',10,25,[7,8,9], True,None])
# print(type(sample_list))
# print(sample_list)
# print(len(sample_list)) 

# print(sample_list[3])
# print(sample_list[-2])



# s = [1,2,3,'Quest', 10.25 ,[7,5,6],True,None]
# print(s[5][1])
# print(s[5[1]])

"""Operatoes"""

""""+= add an element"""
# numbers=[1,2,3,4,5,6,7,8,9]
# numbers+=[10]                               #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)

# numbers+='10'                              #1, 2, 3, 4, 5, 6, 7, 8, 9,'1', '0']
# print(numbers)

# numbers+='yaseen'                          #[1, 2, 3, 4, 5, 6, 7, 8, 9, 'y', 'a', 's', 'e', 'e', 'n']
# print(numbers)



"""+ operator used to merg 2 lists"""

# numbers=[1,2,3,4,5,6,7,8,9]
# sample=[10,20,30,40,50]
# updated_list=numbers+sample
# print(updated_list)                         #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]

# numbers=[1,2,3,4,5,6,7,8,9]
# test_list= numbers*10
# print(test_list)


# list1=[0]
# list1*=10
# print(list1)                                #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(len(list1))


# numbers=[1,2,3,4,5,6,7,8,9]
# numbers[3]=400  
# print(numbers)                              #[1, 2, 3, 400, 5, 6, 7, 8, 9]

# numbers=[1,2,3,4,5,6,7,8,9]
# numbers[3]=numbers[1] +89
# print(numbers)                              #[1, 2, 3, 91, 5, 6, 7, 8, 9]             //it means 2+89. =91

"""membership """

# numbers=[1,2,3,4,5,6,7,8,9]
# print(20 in numbers)                         #false
# print(3 in numbers)                          #true

# numbers=[1,2,3,4,5,6,7,8,9,[20,10,30]]              
# print(30 in numbers[-1])


""""Indexing"""
# numbers=[1,2,3,4,5,6,7,8,9,[20,10,30]]              
# print(numbers[8])
# print(numbers[9])
# # print(numbers[10])            #Error
# print(numbers[-5])
# print(numbers[-1][-1])

# numbers=[1,2,3,4,5,6,7,8,9,[20,10,30],[100,200,300,[400,500,600],700,800,900]]              
# acsses 500
# print(numbers[-1][3][1])
# print(numbers[10][3][1])
# print(numbers[-1][-4][-2])

# numbers=[1,2,3,4,5,'quest','yaseen',6,7,8,9,[20,10,30],[100,200,300,[400,500,600],700,800,900]]              
# accsess s
# print(numbers[6][2])



""""Slicing"""

# numbers=[1,2,3,4,5,'quest','yaseen','najad',6,7,8,9,[20,10,30]]              
# print(numbers[5:8])                                                 #['quest', 'yaseen', 'najad']
# print(numbers[::2])                                                 #[1, 3, 5, 'yaseen', 6, 8, [20, 10, 30]]
# print(numbers[::-1])                                                #reversw the list

# print(numbers[7][1:4])            

# matirxes=[[0,1,2],[3,4,5],[6,7,8]]
# for matrix in matirxes:
#     print(matrix)

# matirxes=[[0,1,2],[3,4,5],[6,7,8]]

# for matrix in matirxes:
#     for m in matrix:
#         print(m)

# for matrix in matirxes:
#     for m in matrix:
#         print(m,end=" ")
#     print()

# for i in range(len(matirxes)):
#     for j in range(len(matirxes[i])):
#         print(matirxes[i][j],end=" ")
#     print()