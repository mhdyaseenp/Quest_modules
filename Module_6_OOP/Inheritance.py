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

class Vehicle:                                      #class 1 grand parent
    
    def start(self):
        print("Vehicle can start..")
        
    def test(self):
        print("Testing Vehicle method....")

class Car(Vehicle):                                 #class 2 parent
    def horn(self):
        print("Horn......")
    def test(self):
        super().test()
        print("Testing Car method....")
        
class Ev(Car):                                      #class 3 child
    def test(self):
        super().test()
        # Vehicle.test(self)
        print("Testing Ev method....")


# nexon=Ev()
# nexon.horn()
# nexon.start()

# bmw=Vehicle()
# bmw.start()

nexa=Ev()
nexa.test()