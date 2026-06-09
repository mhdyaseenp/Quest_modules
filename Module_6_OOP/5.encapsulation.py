# data hidding
# Binding data (variables) and methods (functions) together inside a class and restricting direct access to some data.



# private 





# bank name class
# instance=accno,name,ifsc,balence
# methods getdetails(),getbalence(),eithdraw(),deposit()

# class Bank:
#     bank_name="SBI"
    
#     def __init__(self,acc_no,b_name,ifsc_co,balence):
#         self.acc=acc_no
#         self.name=b_name
#         self.__ifsc=ifsc_co
#         self.balence=balence
        
#     def get_details(self):
#         print(f" Account No : {self.acc}\n Name :{self.name}\n IFSC code :{self.__ifsc}\n Balence :{self.balence}\n")
        
#         # return __
        
#     def get_balence(self):
#         print(f" Current balence :{self.balence}")
    
#     def deposit(self,amount):
#         self.balence +=amount
#         print(f" deposit is succsessful ,current balence is {self.balence}")
        
#     def withdraw(self,amount):
#         if amount >self.balence:
#             print("insufficent balence..")
#         else:
#             self.balence -=amount
#             print(f"Transaction compleated, yor current balence is {self.balence}")
        
        
# yaseen=Bank(28737459,'yaseen','SBI03838',45000)
# yaseen.get_details()


# yaseen.get_balence()

# am=int(input("Enter the amount to deposit :"))
# yaseen.deposit(am)

# wit=int(input("Enter the amount to withdraw :"))
# yaseen.withdraw(wit)









# class Bank:
#     bank_name="SBI"
    
#     def __init__(self,acc_no,balence):
#         self.acc=acc_no
#         self.__balence=balence
        
        
#     def get__balence(self):
#         return(f" Current balence :{self.__balence}")
        
#     def set__balence(self,amount):
#         if amount<0:
#             return "invalid"
#         else:
#             self.__balence=amount
#             return f"New balence :{self.__balence}"
    

        
        
# yaseen=Bank(2879,45000)


# print(yaseen.get__balence())
# yaseen.set__balence(3000)
# print(yaseen.get__balence())d





class Bank:
    bank_name="SBI"
    
    def __init__(self,acc_no,balence):
        self.acc=acc_no
        self.__balence=balence
        
    @property  
    def balence(self):
        return(f" Current balence :{self.__balence}")
        
    @balence.setter
    def balence(self,amount):
        if amount<0:
            return "invalid"
        else:
            self.balence=amount
            return f"New balence :{self.__balence}"
    

        
        
yaseen=Bank(2879,45000)


print(yaseen.balence)
yaseen.__balence=3000
print(yaseen.__balence)











# encapsilation
# data hidding

# abstraction
# implimentation hidding