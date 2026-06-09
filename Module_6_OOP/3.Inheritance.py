# class Animal:

#     def eat(self):
#         print("Eating.....")
        
#     def sleep(self):
#         print("sleeping.....")
        
# class Dog(Animal):
#     def run(self):
#         print("Runnig.....")

# class Cat (Animal):
#     pass

# arjun=Dog()
# arjun.eat()
# arjun.run()

# kittu=Cat()
# kittu.sleep()




# class Person:
#     def __init__(self,name,age):
#         print("Calling Parent constructor..........")
#         self.name=name
#         self.age=age
        
#     def get_details(self):
#         print(f"Name :{self.name}\nAge :{self.age}")
        
#     def test(self):
#         print("Tsting Parent method....")
        
        
# class Student(Person):
#     # def __init__(self,s_is,name, age,):
#     #     super().__init__(name,age)
        
#     #     print("Calling child constructor.....")
#         # self.s_id=id
#         # self.course=course
        
#     def test(self):
#         super().test()
#         print("Tsting Child method....")
        
# # yaseen=Student('yaseen',34)
# # yaseen.get_details()

# # jasil=Student(2332,'jasil',33)
# # jasil.test()

# shahal=Student('jh',76)
# shahal.test()





# class Person:
#     def __init__(self,name,age,address):
#         print("Calling Parent constructor..........")
#         self.name=name
#         self.age=age
        
#     def get_details(self):
#         print(f"Name :{self.name}\nAge :{self.age}")
        
#     def test(self):
#         print("Tsting Parent method....")
        
        
# class Student(Person):
#     def __init__(self,name, age,address,course):
#         super().__init__(name,age,address)
        
#         print("Calling child constructor.....")
#         self.s_id=id
#         self.course=course
        
#     def test(self):
#         super().test()
#         print("Tsting Child method....")
        
# # yaseen=Student('yaseen',34)
# # yaseen.get_details()

# # jasil=Student(2332,'jasil',33)
# # jasil.test()

# shahal=Student('jh',76,'sdjfhjsh','python')
# # shahal.test()





'single INheritance'

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# class Devoleper(Person):
#     def __init__(self, name, age,salery,language):
#         super().__init__(name, age)
#         self.salery=salery
#         self.language=language
        
#     def get_details(self):
#         print(f"Name :{self.name}\nAge :{self.age}\nSalery :{self.salery}\nLanguage :{self.language}")

# niyas=Devoleper(name="niyas",salery=34342,age=23,language="Python")
# niyas.get_details()


'multilevel inheritance'

# class Vehicle:                                      #class 1 grand parent
    
#     def start(self):
#         print("Vehicle can start..")
        
#     def test(self):
#         print("Testing Vehicle method....")

# class Car(Vehicle):                                 #class 2 parent
#     def horn(self):
#         print("Horn......")
#     def test(self):
#         super().test()
#         print("Testing Car method....")
        
# class Ev(Car):                                      #class 3 child
#     def test(self):
#         super().test()
#         # Vehicle.test(self)
#         print("Testing Ev method....")


# # nexon=Ev()
# # nexon.horn()
# # nexon.start()

# # bmw=Vehicle()
# # bmw.start()

# nexa=Ev()
# nexa.test()




'Multiple inheritance' 
#one childen one or more  parent


# class Father:
#     def fath(self):
#         print("iam father ")
        
# class Mother:
#     def moth(self):
#         print("iam mother ")
        
# class Child(Father,Mother):
#     def chi(self):
#         print("iam the son")
        
# richu=Child()



# class SportsPerson:
#     team='barcelona'
#     def action(self):
#         print("Plays Footbal")
        
# class Mucican:
#     band='thaikudam'
#     def action(self):
#         print("Plays Guitar")

# # class Student(Mucican,SportsPerson):                 #method resolution order (MRO) which one on left it will call if a same method called for both parents   // c3 linerarazation algorithamis used
# class Student(SportsPerson,Mucican):                   #method resolution order (MRO) which one on left it will call if a same method called for both parents
#     def study(self):
#         print("Studies in college")
        
# yaseen=Student()
# print(yaseen.band)
# print(yaseen.team)

# yaseen.action()                                         #class Student(Mucican,SportsPerson):   output :-Plays Guitar
# yaseen.action()                                         #class Student(SportsPerson,Mucican):   output :-Plays Footbal

# print(Student.mro())


    
    
    
'Hierarchical inheritance' 
#one parent one or more childen

# class Shape:
#     def color(self):
#         print("All shapes have an color")
    
# class Circle(Shape):
#     def area(self,r):
#         print("area of a circle is :",3.14*r)
        
# class Rectangle(Shape):
#     def area(self,l,b):
#         print("area of a rectangle is :",l*b)
#     def test(self):
#         pass
    
#
# c2=Circle()
# c2.area(3)
# c2.color()

# r3=Rectangle()
# r3.area(4,23)
# r3.test()


'Hybrid Inheritance'


class Vehicle:
    def fuel(self):
        print("Vehcle use some fuel tuype")
        
class Car (Vehicle):
    def wheels(self):
        print("Car has 4 wheels.")
        
class Motorcycle(Vehicle):
    def wheels(self):
        print("Motorcycle has 2 wheels")
        
class ElectricCar(Car):
    def battery(self):
        print("Electric car uses lithium battery")
        
class ElectricMotorecycle(Motorcycle):
    def battery(self):
        print("Electric Motorcycle use litium battery")
    
# ac=ElectricCar()
# ac.battery()
# ac.fuel()
# ac.wheels()
# print()
# bk=ElectricMotorecycle()
# bk.battery()
# bk.fuel()
# bk.wheels()



print()
print()


# apps chid class ,fooddelivery 

# questin

class User:
    def login(self):
        print("login succsesful...")
          
    def order(self):
        print("Order Your foood...")
    
    def order_copleat(self):
        print("Order completed ☑️")
          
class Shop:
    def food(self):
        print("Selct an food \n1. Biriyani\n2. Mandi")
            
class Delvery_partner:
    def location(self):
        print("Order out of delivery")
        
    def deliverd(self):
        print("Order delivered succesfully ✅")

class Swiggy(Shop,Delvery_partner,User):
    def paymet(self):
        print("please compleate your payment")
        
    def paymet_compleated(self):
        print("payment compleated Successfully✅")
        
# cp=Swiggy()

# cp.login()
# cp.order()
# cp.food()
# cp.order_copleat()
# cp.paymet()
# cp.paymet_compleated()
# cp.location()
# cp.deliverd()

#                                         # login succsesful...
#                                         # Order Your foood...
#                                         # Selct an food 
#                                         # 1. Biriyani
#                                         # 2. Mandi
#                                         # Order completed ☑️
#                                         # please compleate your payment
#                                         # payment compleated Successfully✅
#                                         # Order out of delivery
#                                         # Order delivered succesfully ✅



