import re
with open("regex_practice_dataset.txt", "r+") as f:
    data=f.read()
    
    #for Vehcle no
    result=re.findall(r"\w{2}-\d{2}-\w{2}-\d{4}",data)
    print("Vehcle Number :")
    cont=0
    for i in result:
        cont+=1
        print(cont," :",i)
    print()   
    
    
    #ip address
    result2=re.findall(r"\d{,3}\.\d{,3}\.\d{,3}\.\d{,2}",data)
    print("IP adresses :")
    cont=0
    for i in result2:
        cont+=1
        print(cont," :",i)
    print()
    
    
    
    