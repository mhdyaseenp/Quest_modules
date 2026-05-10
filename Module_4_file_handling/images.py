with open("sagittarius-a-black-3840x2160-25401.jpg",'a+b')as f:
    f.seek(0)
    a=f.read()
    # print(a)
    
with open("1.jpg",'a+b')as file:
    file.write(a)