# Binding data (variables) and methods (functions) together inside a class and restricting direct access to some data.









# bank name class
# instance=accno,name,ifsc,balence
# methods getdetails(),getbalence(),eithdraw(),deposit()

class Bank:
    bank_name="SBI"
    
    def __init__(self,acc_no,b_name,ifsc_co,balence):
        self.acc=acc_no
        self.name=b_name
        self.__ifsc=ifsc_co
        self.balence=balence
        
    def get_details(self):
        print(f" Account No : {self.acc}\n Name :{self.name}\n IFSC code :{self.__ifsc}\n Balence :{self.balence}\n")
        
        # return __
        
    def get_balence(self):
        print(f" Current balence :{self.balence}")
    
    def deposit(self,amount):
        self.balence +=amount
        print(f" deposit is succsessful ,current balence is {self.balence}")
        
    def withdraw(self,amount):
        if amount >self.balence:
            print("insufficent balence..")
        else:
            self.balence -=amount
            print(f"Transaction compleated, yor current balence is {self.balence}")
        
        
yaseen=Bank(28737459,'yaseen','SBI03838',45000)
yaseen.get_details()


# yaseen.get_balence()

# am=int(input("Enter the amount to deposit :"))
# yaseen.deposit(am)

# wit=int(input("Enter the amount to withdraw :"))
# yaseen.withdraw(wit)



