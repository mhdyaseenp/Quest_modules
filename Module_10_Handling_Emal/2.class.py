# class Student:
#     pass

# yaseen = Student()

# print(type(yaseen))
# print(id(yaseen))

# richu=Student()
# print(id(richu))


# class Student:
#     def exam(self):
#         print("Exam contucted on 10/5/2026")
#                                                             #self is a parameter it refers to the current obnject(instance) of the class
#     def study(self):
#         pass                                                #pass statement is a do-nothing statement
        
# richu=Student()
# yasee=Student()

# richu.exam()
# yasee.exam()

"""class Attribute"""

# class Student:
#     school_name="Quest innovative Solution "                  #class Attribute"""
    
# richu=Student()
# yaseen=Student()

# print(Student.school_name)                                    #call with calss
# print(yaseen.school_name)                                     #call with object
# print(richu.school_name)                                      #call with object

# 'reasign'
# Student.school_name="Qis"                                     #it will efect all objects. //class level update
# print(yaseen.school_name)

# yaseen.school_name="JDT"                                      #it only affect the renamed object      //object level update
# print(yaseen.school_name)
# print(richu.school_name)




# class Human:
#     no_fo_hands=2
#     no_fo_legs=2
# x=Human()
# y=Human()

# y.no_fo_legs=1
# print(x.no_fo_legs)
# print(y.no_fo_legs)




# class Student:
#     school_name="Quest innovative Solution "                 
    
# richu=Student()
# yaseen=Student()

# print(Student.school_name)                                  
# print(yaseen.school_name)                                     
# print(richu.school_name)                                      

# 'reasign'
# Student.school_name="Qis"                                     
# print(yaseen.school_name)

# yaseen.school_name="JDT"                  
                    
# print(yaseen.school_name)
# print(richu.school_name)


# del Student.school_name

# print(richu.school_name)                                 #error
# print(yaseen.school_name)                                #JDT

# del yaseen.school_name

# print(richu.school_name)                                 #Qis
# print(yaseen.school_name)                                #Qis



"""instance """

# class Student:
#     school_name="QIS"
#     course="Python Full Stack"
    
#     def __init__(self):                                      #constructor method      
#         print("Constructor created ......")
        
# shal=Student()
# jasil=Student()


# class Student:
#     school_name="QIS"
#     course="Python Full Stack"
    
#     def __init__(self,s_id,name,age,email):     
#         self.Student_id=s_id
#         self.S_name=name
#         self.age=age
#         self.email=email
        
         
#     def get_deatails(self):
#         print(f"Student id :{self.Student_id}\nStudent Name :{self.S_name} \nStudent age :{self.age}\nStudent Email :{self.email} ")
        
        
        
# shal=Student(s_id=122,name="yaseen",age=22,email="hello@gmail.com")
# shal.get_deatails()

# print()

# niyas=Student(256,"niyas",43,"hai@gmail.com")
# niyas.get_deatails()



# class Emploee:
#     cpmpany_name="Quest Prtd"
#     Branch_name="Calicut"
    
#     def __init__(self,emp_id,emp_name,emp_salary,emp_mail):
#         self.e_id=emp_id
#         self.e_name=emp_name
#         self.e_salery=emp_salary
#         self.e_mail=emp_mail
    
#     def emp_deatails(self):
#         print(f"Employee id:{self.e_id} \nEmployee name :{self.e_name} \nEmployee Salery :{self.e_salery} \nEmployee Mail :{self.e_mail}")
    
#     def update_sal(self):
#         """Print if the salery grater than 30000"""
#         if self.e_salery >30000:
#             increment=self.e_salery*0.15
#             self.e_salery+=increment
#             print(f"Updated Salery :{self.e_salery}")
            
        
# yasee=Emploee(122,"yaseen",39000,"jajf@gamil.com")

# yasee.emp_deatails()
# yasee.update_sal()






# class Emploee:
#     copmany="Quest Prtd"
#     Branch_name="Calicut"
    
#     def __init__(self,emp_id,emp_name,emp_salary,emp_mail):
#         self.e_id=emp_id
#         self.e_name=emp_name
#         self.e_salery=emp_salary
#         self.e_mail=emp_mail
    
#     def emp_deatails(self):
#         print(f"Employee id:{self.e_id} \nEmployee name :{self.e_name} \nEmployee Salery :{self.e_salery} \nEmployee Mail :{self.e_mail}")
        
#     def update_sal(self):
#         if self.e_salery >30000:
#             increment=self.e_salery*0.15
#             self.e_salery+=increment
#             print(f"Updated Salery :{self.e_salery}")
    
#     def update_company(self):
#         self.copmany="google"
#         print(self.copmany)
        
#     def resign(self):
#         print(f"Employee id:{self.e_id} \nEmployee name :{self.e_name} \nEmployee Salery :{self.e_salery} \nEmployee Mail :{self.e_mail}")
    
#     '__del__()'
    
#     def __del__(self):
#         print("Constructed deleted.....")
        
# yasee=Emploee(122,"yaseen",39000,"jajf@gamil.com")
# jaisl=Emploee(122,"yaseen",39000,"jajf@gamil.com") 

# # yasee.emp_deatails()
# # yasee.update_sal()

# # yasee.update_company()
# yasee.resign()


'Inbuild Atributes of an obj'

# class Emploee:
#     copmany="Quest Prtd"
#     Branch_name="Calicut"
#     # phone=2424524
    
#     def __init__(self,emp_id,emp_name,emp_salary,emp_mail):
#         self.e_id=emp_id
#         self.e_name=emp_name
#         self.e_salery=emp_salary
#         self.e_mail=emp_mail
        
# yaseen=Emploee(102,'yaseen',32000,'yase.co.in')
# jasil=Emploee(133,'jasil',322300,'jasile.co.in')

# print(yaseen.e_name)

'getattr'

# print(getattr(yaseen,'e_name'))
# print(getattr(yaseen,'e_id',923))
# print(getattr(yaseen,'e_place'))                          #Errro
# print(getattr(yaseen,'phone',76454444))

'setattr()'

# setattr(yaseen,'phone',923746972)
# print(yaseen.phone)

# setattr(yaseen,'e_mail','sachu.co.in')
# print(yaseen.e_mail)

'hasattr()'

# print(hasattr(yaseen,'e_name'))                             #True
# print(hasattr(yaseen,'phone'))                              #false

'delattr()'

# delattr(yaseen,'e_name')
# print(yaseen.e_name)






# bank name class

# instance=accno,name,ifsc,balence

# methods getdetails(),getbalence(),eithdraw(),deposit()

# class Bank:
#     bank_name="SBI"
    
#     def __init__(self,acc_no,b_name,ifsc_co,balence):
#         self.acc=acc_no
#         self.name=b_name
#         self.ifsc=ifsc_co
#         self.balence=balence
        
#     def get_details(self):
#         print(f" Account No : {self.acc}\n Name :{self.name}\n IFSC code :{self.ifsc}\n Balence :{self.balence}\n")
        
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





'---------------------------------------------------------------------------------------------------------------'


'class inside another class'

# class Electronics:
#     def collections(self):
#         print("collection of electronics ")
    
#     class Laptop:
#         def brand(self):
#             print('Hp')
            
            
# e=Electronics()
# e.collections()

# lap=Electronics.Laptop()
# lap.brand()

