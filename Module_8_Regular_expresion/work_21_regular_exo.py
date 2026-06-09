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
    
    
    #PAN card no
    result3=re.findall(r"[A-Z]{5}\d{4}[A-Z]",data)
    print("PAN No :")
    cont=0
    for i in result3:
        cont+=1
        print(cont," :",i)
    print()
    
    
    #Email id
    # result4= re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', data)
    result4= re.findall(r'[a-zA-Z0-9]+@gmail\.com', data)
    print("Email id's :")
    cont=0
    for i in result4:
        cont+=1
        print(cont," :",i)
    print()
    
    
    #Product Codes
    result5= re.findall(r'[A-z]{4}\-\d{,5}', data)
    print("Product Codes:")
    cont=0
    for i in result5:
        cont+=1
        print(cont," :",i)
    print()
    
    
    
    
    #Dates 
    # result6= re.findall(r'\d{,4}[/-]\d{2}[/-]\d{,4}', data)
    result6= re.findall(r'(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2})', data)
    
    print("Dates :")
    cont=0
    for i in result6:
        cont+=1
        print(cont," :",i)
    print()
    
    
    #Amounts 
    result7= re.findall(r'(?:[₹$€]\d+\.\d+)|[₹$€]\d+', data)
    
    print("Amounts :")
    cont=0
    for i in result7:
        cont+=1
        print(cont," :",i)
    print()
    
    
    
    
    #Pass words 
    result8= re.findall(r'\b\w+[@#$_]\w+\b', data)
    # result8 = re.findall(r"Passwords\s*(\S+)", data)
    
    print("Passwords :")
    cont=0
    for i in result8:
        cont+=1
        print(cont," :",i)
    print()
    
    
    
    