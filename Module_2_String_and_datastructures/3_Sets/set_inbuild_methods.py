"""1-issubset()"""

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}

# set3={1,2}                      #true
# set3={1,2,3}                    #true
# set3={1,2,5}                    #true
# set3={1,2,6}                    #false
# set3={6}                        #false
# print(set3.issubset(set1))                   #child




"""2-issuperset()"""

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}

# set3={1,2}                      #true
# set3={1,2,3}                    #true
# set3={1,2,5}                    #true
# set3={1,2,6}                    #false
# set3={6}                        #false
# print(set1.issuperset(set3))                #parent



"""3-isdisjoint()"""

# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}
# set2={6,7,8,9}                              #true

# print(set1.isdisjoint(set2))                #false







