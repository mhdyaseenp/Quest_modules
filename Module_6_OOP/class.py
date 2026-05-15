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


# class Student:
#     school_name="Quest innovative Solution "                   #class Attribute"""
    
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




class Student:
    school_name="Quest innovative Solution "                 
    
richu=Student()
yaseen=Student()

# print(Student.school_name)                                  
# print(yaseen.school_name)                                     
# print(richu.school_name)                                      

'reasign'
Student.school_name="Qis"                                     
# print(yaseen.school_name)

yaseen.school_name="JDT"                  
                    
# print(yaseen.school_name)
# print(richu.school_name)


# del Student.school_name

# print(richu.school_name)                                 #error
# print(yaseen.school_name)                                #JDT

del yaseen.school_name

print(richu.school_name)                                 #Qis
print(yaseen.school_name)                                #Qis