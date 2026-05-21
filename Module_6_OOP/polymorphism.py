# class Animal:
#     def speak(self):
#         pass
    
# class Dog(Animal):
#     def speak(self):
#         print("Bowww Boww")
        
        
'operator overloading'

# class Operator:
#     def add(self,a,b):
#         return a+b
#     def mult(selb,f,d):
#         return f*d
    
# o1=Operator()
# print(o1.add(5,4))

# print(o1.add('5','4'))

# print(o1.add('Mhd',' Yaseen'))

# print(o1.mult(3,'Yaseen '))

'-----------------------------------------------------------'

# class Operation:
#     def __init__(self,a=10,b=39):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
    
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
    
# # ob=Operation()
# ob=Operation(2,4)


# 'Method Ovrriding'
# '-----------------------------------------------------------'
# class Vehicle :
#     def start(self):
#         print("Vrhicle is starting")
        
# class Bike(Vehicle):
#     def start(self):
#         super().start()
#         print("Bike Starting with self Button")
        
# b=Bike()
# b.start()