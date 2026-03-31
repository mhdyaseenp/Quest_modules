# 1 to 10
# a = []
# for i in range(1,11):
#     a.append(i)
# print(a)



# print 1 to 10 
# number = [i for i in range(1,11)]  
# print(number)                                                               #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# print even 
# num = [1,2,3,4,5,6,7,8,9]
# new_list = [n for n in num if n %2==0]
# print(new_list)                                                             # [2, 4, 6, 8]



# Square of 1 to 10 
# square = [i ** 2 for i in range(1,11)]
# print(square)                                                              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]








# print 1 to 10 . even number aneel square um odd num aneel cube um 

# sq_cube = [ i*2 if i %2 ==0 else i * 3 for i in range(1,11)]
# print(sq_cube)                                                              # [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]





# List upper case il aaakaan

# list = ['apple','banana','orange']
# upper_list = [i.upper() for i in list]
# print(upper_list)                                                             # ['APPLE', 'BANANA', 'ORANGE']




# Length check cheyyan 

# list = ['apple','banana','orange']
# count = [len(i) for i in list]
# print(count)                                                                   # [5, 6, 6]




# Vowels aneel capital letter . allengil Title 

# list = ['apple','iron','jasil','Yaseen']
# check = [i.upper() if i[0] in 'AEIOUaeiou' else i.title() for i in list]
# print(check)




# Positive number mathram print cheyyan 
# list = [1,2,3,4,-4,-8,9,-3]
# positive = [i for i in list if i > 0]
# print(positive)







# Print vowels only
# list1 = 'programming'
# vowels = [ i for i in list1 if i in 'AEIOUaeiou']
# print(vowels).





# 2 List um common number undeeel print cheyyan 
# L1 = [1,2,3,4,5]
# L2 = [10,2,30,45,5]

# check = [i for i in L1 if i in L2 ]
# print(check)



# number = ['1','2','3','4','5','6']
# convert = [int (i) for i in number if i.isdigit() ]
# print(convert)