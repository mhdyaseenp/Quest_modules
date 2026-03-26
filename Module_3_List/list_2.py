""" Matrix""" 

# matrix = [[0,1,2],[3,4,5],[6,7,8]]
# for s in matrix:
#     for m in s:     
#         print(m)



"""append()"""                          # Last index il value add cheyyaan

# sample = [1,2,3,4,5,6,7,8,9,100]
# # print(dir( sample ))
# sample.append(2004)
# sample.append("Jasil")
# sample.append([200,300,400])

# print(sample)


"""Insert()"""                          # add value in specific place

# num = [1,2,3,4,5,6,7,8,9]
# num.insert(1,'jasil')
# print(num)


"""pop()"""                            # Remove a element

# num = [1,2,3,4,5,6,7,8,9]
# num.pop()
# print(num)


# remove value in index base 

# num = [1,2,3,4,5,6,7,8,9]
# num.pop(0)
# print(num)


# remove value in neg index 

# num = [1,2,3,4,5,6,7,8,9]
# num.pop(-1)
# print(num)


"""remove()"""
# num = [1,200,3,4,5,6,7,8,9]
# num.remove(200)
# print(num)


'''clear()  '''                      # clear a list ,empty list
# num = [1,200,3,4,5,6,7,8,9]
# num.clear()
# print(num)


'''count()'''                       # count cheyyaan . eg :- 200 ethra thavana undennn
# num = [1,200,3,4,200,5,6,7,8,9]
# print(num.count(200))


'''Copy()'''
# num = [1,200,3,4,5,6,7,8,9,[100,200,7]]
# copy_list = num.copy()

# copy_list[-1][-1]=700
# print(copy_list)                                    # [1, 200, 3, 4, 5, 6, 7, 8, 9, [100, 200, 700]]
# print(num)                                          # [1, 200, 3, 4, 5, 6, 7, 8, 9, [100, 200, 700]]


'''sort()'''                                        # accending order ( 1 2 3 4 5 6 )
# Accesing
# list1 = [1, 200, 9, 7, 5, 0, 3]
# list1.sort()
# print(list1)                                        # [0, 1, 3, 5, 7, 9, 200]

# Deccending
# list1.sort(reverse=True)
# print(list1)                                        # [200, 9, 7, 5, 3, 1, 0]


# Sort in alphabetic order 
# name = ['my', 'name', 'is', 'jasil', 'adivaram']
# name.sort()
# print(name)                                             # ['adivaram', 'is', 'jasil', 'my', 'name']


# Length vechh 
# name = ['myyyyyyyyyyyyy', 'name', 'is', 'jasil', 'adivaram']
# name.sort(key=len)
# print(name)


'''Extend()'''              #to add multiple element

# list1 = [1, 200, 9, 7, 5, 0, 3]
# list2 = ['jasil',2004,'adivaram']
# list1.extend(list2)
# print(list1)                               # [1, 200, 9, 7, 5, 0, 3, 'jasil', 2004, 'adivaram']

# list1.extend('Muhammed')
# print(list1)                              # [1, 200, 9, 7, 5, 0, 3, 'jasil', 2004, 'adivaram', 'M', 'u', 'h', 'a', 'm', 'm', 'e', 'd']



'''index()'''                                # (value,start,stop)
# list1 = [1, 200, 9, 7, 5, 0, 3]
# print(list1.index(200))                      # 1
# print(list1.index(9,0,3))                    # 2



'''reverse()'''
# list1 = [1, 200, 9,'jasil', 7, 5, 0, 3]
# list1.reverse()
# print(list1)                                # [3, 0, 5, 7, 'jasil', 9, 200, 1]


# list1 = [3, 0, 5, 7, 9, 200, 1]
# # len
# print(len(list1))                                             # 7

# # min
# print(min(list1))                                             # 0

# # max
# print(max(list1))                                             # 200

# # sum
# print(sum(list1))                                             # 225
 
# # sorted
# print(sorted(list1))                                          # [0, 1, 3, 5, 7, 9, 200]




# nums = [1, 2, 3, 401, 10, 4008, 20]
# large = 0
# s_large = 0

# for i in range(len(nums)):
#     if nums[i] > large:
#         s_large = large
#         large = nums[i]
#     elif large > nums[i] > s_large:
#         s_large = nums[i]

# print("Largest =", large)
# print("Second Largest =", s_large)


"""Unpaking"""
# sample=['apple','banana','mango']
# x,y,z=sample
# print(x)                  #apple
# print(y)                  #banana
# print(z)                  #mango

# sample=['apple','banana','mango','grape']
# x,y,z=sample
# print(x)
# print(y)                  
# print(z)                  #error


# sample=['apple','banana','mango','grape']
# *x,y,z=sample
# print(x)                  #['apple', 'banana']
# print(y)                  #banana
# print(z)                  #mango