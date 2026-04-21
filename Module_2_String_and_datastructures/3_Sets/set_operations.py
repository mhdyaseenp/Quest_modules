"""union()"""
#to combain 2 sets

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9,}

# print(set1.union(set2))
# print(set1 | set2)                  #{1, 2, 3, 4, 5, 6, 7, 8, 9}


# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9,}
# set3={8,9,10,11,12,13,13,13}

# print(len(set3))                    #6 bcz duplicats 

# print(set1.union(set2,set3))
# print(set1 | set2 | set3)           #{1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13}


# who_know_python={'najad','shabin','yaseen','jasil'}
# who_know_django={'richu','shahal','yaseen','shoney','priyanka'}
# who_know_atleast_one=who_know_django | who_know_python
# print(who_know_atleast_one)


"""intersection()"""
#common elements in both sets

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9,}
# print(set1.intersection(set2))          #{4, 5}

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9,}
# set3={8,9,10,11,12,13}
# print(set1.intersection(set2,set3))          #set().  bcz 4,5 not in set 3

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9,}
# set3={4,5,8,9,10,11,12,13}
# print(set1 & set2 & set3)          #{4, 5}


# who_know_python={'najad','shabin','yaseen','jasil'}
# who_know_django={'richu','shahal','yaseen','shoney','priyanka'}
# who_know_both=who_know_django & who_know_python
# print(who_know_both)


"""3-intersection_update()"""
# update the existing sest

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9,}
# set1.intersection_update(set2)
# print(set1)
# set2.intersection_update(set1)
# set2&=set1
# print(set2)                                 #update set2



"""4-diffrence()"""
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}

# print(set1.difference(set2))                    #{1, 2, 3}
# print(set1-set2)
# print(set2-set1)                               #{8, 9, 6, 7}

# print(set2-set2)                                #set()


"""5-difference_update()"""
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}

# set1.difference_update(set2)
# set1-=set2
# print(set1)


"""6-symmetric_difference()"""
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}

# print(set1.symmetric_difference(set2))                    
# print(set1 ^ set2)                            #{1, 2, 3, 6, 7, 8, 9}


"""6-symmetric_difference()"""
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}

# set1.symmetric_difference_update(set2)                    
# print(set1)                                       #{1, 2, 3, 6, 7, 8, 9}