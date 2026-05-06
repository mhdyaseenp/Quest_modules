#in this file we import the file in another folder into this file
#it acssess the file inside first_folder 


# from first_folder.module_in_python import greet,pi

# print(pi)
# print(greet("yaseen"))


# from first_folder.module_in_python import *

# print(pi)
# print(greet("yaseen"))



import first_folder.module_in_python as ts
ts.pi
print(ts.pi)

print(ts.greet("jasil"))





from  first_folder.module_in_python import greet as ss

print(ss("shakir"))




