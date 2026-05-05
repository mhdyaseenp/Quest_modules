# f=open("sample.txt",'r+')
# print(f.read())
# f.write("\nwelcome to our home ground campnow")
# f.close()

# files=open('test.py','r+')
# print(files.read())
# files.write("\nprint(add(8,6))")
# files.close()

# with open("sample.txt",'r') as f:
#     print(f.read())                           #read the file
    

# with open("sample.txt",'w') as f:
#     f.write("Hello World")                      #rewrite the file
#     f.write("\nPython Programers")
    
    
# with open("sample.txt",'w') as f:
#     print(f.write("Calicut"))
#     f.write("Calicut")                      
    
    
# with open("sample.txt",'w') as f:
#     pass
    
    
    
# with open("input.txt",'w') as f:             #when we use an file that not exixst in the folder then it will add new file with the given name it only work in w ,w+ 
#     pass
    
    
# "r+"
# with open("sample.txt",'r+') as f2:
#     data=f2.read()
#     print(data)
#     f2.write(" Programers")
#     f2.seek(10)
#     print(f2.read())


# with open("sample.txt",'r+') as f1:
    # f1.seek(11)
    # f1.write(", Calicut")
    # f1.write(", kottayam")
    # f1.write(", Malapuram")
    # f1.write("456")
    # f1.write("22")
    # f1.seek(10)
    # f1.write("101010")
    # f1.write("39330")
    
    
#when we use f.read() before write the coursor go to the last 
#when we dont use the f.read() the cooursor go to the start 
    
    
    
    
# with open("sample.txt","a+") as f:
#     print(f.tell())
#     f.seek(0)
#     data=f.readlines()
#     print(data)

# data[0]="sree"
# print(data)

# data=tuple(data)

# data=set(data)

# with open("write_example.txt",'w+') as file:
#     file.writelines(data)






# with open("sample_1.txt")as f:
#     data=f.read()
#     print(data)

# with open("yasee.txt",'x')as r:
#     r.write(data)




# with open("sample_1.txt",'r') as f:
#     line=int(input("enter the lines :"))
#     for i in range(line):
#         print(f.readline())


with open("zenitsu-agatsuma-3840x2160-24472.png",'a+b')as f:
    f.seek(0)
    print(f.read())
    # print(a)