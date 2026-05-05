with open("sagittarius-a-black-3840x2160-25401.jpg",'a+b')as f:
    f.seek(0)
    a=f.read()
    
with open("1.jpg",'w')as file:
    file.write(a)