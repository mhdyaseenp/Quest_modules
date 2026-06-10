
# OOPs Lab Practical Questions (Python)

"""# BEGINNER LEVEL QUESTIONS"""

# 1. Create a Student class with attributes:
#    - name
#    - age
#    - course
#    Create 3 objects and display their details.

# 2. Create an Employee class and calculate yearly salary from monthly salary.

# 3. Create a Car class with methods:
#    - start()
#    - stop()
#    - display_details()
# Create a Car class with methods:
# - start()
# - stop()
# - display_details()

# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
        
#     def start(self):
#         print(self.brand, "car started")

#     def stop(self):
#         print(self.brand, "car stopped")

#     def display_details(self):
#         print("Brand :", self.brand)
#         print("Model :", self.model)
#         print("Price :", self.price)

# c1 = Car("Toyota", "Innova", 2500000)
# c1.start()
# c1.display_details()
# c1.stop()

# 4. Create a Mobile class and store:
#    - brand
#    - model
#    - price

# 5. Create a Book class and display book details using objects.
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display(self):
#         print("Book Title :",self.title)
#         print("Author     :",self.author)
#         print("Price.     :",self.price)
# b1=Book(title="Python",price="220",author="Sreeraj")
# b2=Book(title="Java",price="120",author="sneha")
# b1.display()
# print()
# b2.display()

# 6. Create a BankAccount class with:
#    - deposit()
#    - withdraw()
#    - check_balance()

# 7. Create a Laptop class and count how many objects are created.
# class Laptop:
#     count=0
#     def __init__(self,brand):
#         self.brand=brand
#         Laptop.count+=1
# lp1=Laptop('hp')
# lp2=Laptop('apple')
# lp3=Laptop('pavlion')
# lp4=Laptop('hp')
# lp5=Laptop('lenovo')
# print("total count :",Laptop.count)


# 8. Create a class for HospitalPatient with:
#    - patient_id
#    - disease
#    - doctor_name
# class HospitalPatient:
#     def __init__(self,patient_id,disease,doctor_name):
#         self.pat_id=patient_id
#         self.des=disease
#         self.doc=doctor_name
#     def patient_details(self):
#         print(f"Patient id :{self.pat_id}\niDsease :{self.des}\nDoctor :{self.doc}")        
# patient1=HospitalPatient(102,"Feaver",'Dr.Arun')
# patient1.patient_details()

# 9. Create a MovieTicket class to calculate total ticket price.class MovieTicket:
# class MovieTicket:
#     def __init__(self, movie_name, ticket_price, number_of_tickets):
#         self.movie_name = movie_name
#         self.ticket_price = ticket_price
#         self.number_of_tickets = number_of_tickets
#     def cal(self):
#         print("Movie name :",self.movie_name)
#         print("Ticket Price :",self.ticket_price)
#         print("Number of ticket :",self.number_of_tickets)
#         print("Total Amount:",self.ticket_price*self.number_of_tickets)
# movie=MovieTicket(movie_name="Drishyam 3",number_of_tickets=22,ticket_price=120)
# movie.cal()


# 10. Create a Rectangle class and calculate:
#    - area
# #  - perimeter
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def aarea(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)
# r1=Rectangle(10,5)
# print("Area      :",r1.aarea())
# print("perimeter :",r1.perimeter())
    

"""# CONSTRUCTOR-BASED QUESTIONS"""

# 11. Create a class using a default constructor.
# class Student:
#     def __init__(self):
#         print("defult constructor....")
#     def disp(self):
#         print("Welcome to python...")
# s1=Student() 
# s1.disp()       


# 12. Create a class using a parameterized constructor.
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"My namr is {self.name} and iam {self.age} year old")
    
# s1=Student("yaseen",34)

# 13. Create a User class where password should not be empty.
# class User:
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
#         if password=="":
#             print("pass should not be empty")

#         else:
#             print("Login success full")
# # s1=User("yasee",'')
# s2=User("yasee",'djfl')


# 14. Create a constructor that validates email format.
# class Email:
#     def __init__(self,email):
#         self.email=email
#         if '@' in email and '.' in email:
#             print("Email validated")
#         else:
#             print("Email not valdable")
            
# s=input("Enter email :")
# s1=Email(s)


# 15. Create a constructor that automatically generates employee IDs.

# from random import*
# class Employee:
#     count=randint(101,202)
#     def __init__(self,name):
#         self.name=name
#         Employee.count+=1
#         self.empid=Employee.count
#         print(f"Employee name :{self.name}\nEmployee id :{self.empid}\n")
        
# c1=Employee('yaseen;')
# c1=Employee('jasi;')
# c1=Employee('shakir')
        






# 16. Create a Product class that applies GST during object creation.
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
        
#         gst=price*18/100
#         total=price+gst
        
#         print(f"Product name :{self.name}\nProduct Price :{self.price}\nGst amount :{gst}\nTotal Bill :{total}\n")        

# pd1=Product("Iphone",49000)
# pd2=Product("lapto",149000)
# pd2=Product("chai",12)


# 17. Create a Vehicle class that stores:
#    - owner name
#    - vehicle number
#    - insurance expiry

# class Vehicle:
#     def __init__(self, owner_name,vehicle_number,insurance_expiry):
#         self.owner_namea=owner_name
#         self.vehcle_number=vehicle_number
#         self.insurance=insurance_expiry
    
#     def display(self):
#         print(f"Owner name :{self.owner_namea}\nVehicle Number :{self.vehcle_number}\nInsurance Expiry date :{self.insurance}\n")

# s1=Vehicle("yaseen",'KL 32 H 8372','June 12 2027')
# s1.display()


# 18. Create a LibraryBook class with constructor-based initialization.
# class LibreryBook:
#     def __init__(self,title,author,price):
#         self.author=author
#         self.title=title
#         self.price=price

#         print(f"Title       :{self.title}\nAuthor name :{self.author}\nPrice       :{self.price}\n")
        
# c1=LibreryBook("jungle book",'kunjappu',599)
# c1=LibreryBook("Harry Potter",'Henry',2399)
# c1=LibreryBook("Mango tree",'Babuu',359)



# 19. Create a Course class and enroll students using constructors.
# class Course:
#     def __init__(self,course,name):
#         self.name=name
#         self.course=course
#         print(f"{self.name} enrolled in {self.course}")

# s1=Course("Python","Sreeraj")
# s1=Course("Java","Sneha")

# 20. Create a FoodOrder class that calculates total bill automatically.
# class FooodOrder:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
        
#         self.gst=self.price*0.18
#         self.total=self.price+self.gst
        
#         print("Food item :",self.item)
#         print("Food Price :",self.total)
#         print("Food Price on Delivery:",self.total+50)

# f1=FooodOrder("pasta",349)

'# SELF AND ATTRIBUTE QUESTIONS'

# 21. Demonstrate the use of self.

# 22. Differentiate:
#    - class attribute
#    - instance attribute

# 23. Create a company management system using class attributes.
# class Company:
#     company_name="Quest"
#     employee=[]
#     def __init__(self,e_name,e_pos):
#         self.position=e_pos
#         self.name=e_name
#         Company.employee.append(self)
#     def display(self):
#         print("Employe Name :",self.name)
#         print("Position     :",self.position)
#         print("Company Name :",Company.company_name)
#         print()
        
#     def display_all_emp(self):
#         print("All Employe in ",Company.company_name)
#         print()
#         for emp in Company.employee:
#             print(emp.name,"-",emp.position)
            
# e1 = Company("Rahul", "Manager")
# e2 = Company("Aisha", "Developer")
# e3 = Company("Arun", "Designer")

# e1.display()
# e2.display()
# e3.display()

# e1.display_all_emp()
    
    
    
    
# 24. Create instance-specific attributes for users.

# 25. Demonstrate local variables inside methods.
# class Student:
#     def show(self):
#         name="Rahul"
#         mark="101"
#         print("Name of the student :",name)
#         print("Mark of the student :",mark)
# ob=Student()
# ob.show()


# 26. Create a class attribute that tracks total online users.
# class User:
#     us_tot=0
#     def __init__(self,name):
#         self.name=name
#         User.us_tot+=1
#     def displa(self):
#         print("User Name :",self.name)

#     def total_users(self):
#         print("Total Online Users :",User.us_tot)
        
# u1=User("Jasil")
# u2=User("Yaseen")
# u3=User("Shakir")
# u4=User("Fadil")

# u1.displa()
# u2.displa()
# u3.displa()
# u4.displa()
# print()
# u1.total_users()
        

# 27. Build a login system where each object stores unique user data.


# class Login:
#     def __init__(self,user,passw):
#         self.user_name=user
#         self.password=passw
        
#     def login(self,user,pwd):
#         if self.user_name ==user and self.password==pwd:
#             print("Login success full")
#         else:
#             print("Invalid User name or password")

# u1=Login("user123",99877)
# u2=Login('ud23',6655)

# u2.login('ud23',6655)
# u2.login('ud23',746655)


# 28. Create a shopping cart where products are instance attributes.
# class Shoping:
#     def __init__(self,product_name,price,quantity):
#         self.product=product_name
#         self.price=price
#         self.quanatity=quantity
        
#     def displat(self):
#         total=self.quanatity * self.price
        
#         print("Product Name     :",self.product)
#         print("Product Price    :",self.price)
#         print("Product Quantity :",self.quanatity)
#         print("Total Bill       :",total,'\n')
# item1=Shoping("Laptop",45000,1)
# item2=Shoping("Mouse",450,3)

# item1.displat()
# item1.displat()


# 29. Create a school system using:
#    - class attribute for school name
#    - instance attribute for student details

# class School:
#     school_name="JDT"
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
        
#     def details(self):
#         print("School Name    :",School.school_name)
#         print("--------------------------")
#         print("Student Name   :",self.name)
#         print("Student Age    :",self.age)
#         print("Student Course :",self.course,'\n\n')
        
# s1=School("yaseen",21,"Python")
# s2=School("Jasil",22,"Java")
# s3=School("Sree",25,"Dotnet")

# s1.details()
# s2.details()
# s3.details()
        

# 30. Create a weather app object storing city-wise temperature data.
# class Wether:
#     def __init__(self,city,temprature):
#         self.city=city
#         self.tem=temprature
#     def disp(self):
#         print("City       :",self.city)
#         print("Temprature :",self.tem,'°C\n')

# city1 = Wether("Calicut", 32)
# city2 = Wether("Kochi", 30)
# city3 = Wether("Delhi", 40)

# city1.disp()
# city2.disp()
# city3.disp()


# ATTRIBUTE HANDLING FUNCTIONS

# 31. Use getattr() to access object properties dynamically.
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# s1=Student("yaseen",21)
# # attribute = input("Enter attribute name: ")
# # value = getattr(s1, attribute, "Attribute not found")

# value = setattr(s1, 'year', "8758")
# print("Value:",s1.year)


# 33. Use hasattr() to validate whether an object contains a field.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# emp1 = Employee("Yaseen", 50000)

# # Check if attributes exist
# if hasattr(emp1, "name"):
#     print("Name field exists")

# if hasattr(emp1, "salary"):
#     print("Salary field exists")

# if hasattr(emp1, "department"):
#     print("Department field exists")
# else:
#     print("Department field does not exist")

# 34. Use delattr() to remove an object attribute.

# 35. Build a dynamic student record manager using attribute functions.

# 36. Create an API response object and dynamically add attributes.

# 37. Create a configuration class where attributes are added at runtime.

# 38. Build a chatbot profile manager using setattr().

# 39. Create a form builder using dynamic attributes.

# 40. Create a dynamic inventory management system.

# INHERITANCE QUESTIONS

# SINGLE INHERITANCE

# 41. Create:
#    - Parent → Person
#    - Child → Student

# 42. Create:
#    - Parent → Vehicle
#    - Child → Bike

# 43. Create an Employee class inherited by Developer.

# 44. Create a hospital management system using inheritance.

# 45. Create a payment gateway system using inheritance.

"""# MULTILEVEL INHERITANCE"""

# 46. Create:
#    - Animal → Mammal → Dog

# 47. Create:
#    - Company → Department → Employee

# 48. Create:
#    - User → Seller → PremiumSeller

# 49. Create:
#    - Account → SavingsAccount → SalaryAccount

# 50. Create:
#    - Device → Laptop → GamingLaptop

# MULTIPLE INHERITANCE

# 51. Create a class inheriting from:
#    - Camera
#    - Phone

# 52. Create:
#    - Teacher
#    - Researcher
#    - Professor

# 53. Create:
#    - GPS
#    - MusicPlayer
#    - SmartCar

# 54. Build a food delivery app using multiple inheritance.

# 55. Create a drone system combining:
#    - Camera
#    - FlightController

# HIERARCHICAL INHERITANCE

# 56. Create:
#    - Parent → Shape
#    - Children → Circle, Rectangle, Triangle

# 57. Create:
#    - Employee
#    - Manager
#    - Developer
#    - Tester

# 58. Create:
#    - Payment
#    - UPI
#    - Card
#    - Wallet

# 59. Build a school system using hierarchical inheritance.

# 60. Create an OTT subscription system.

# SUPER() AND MRO QUESTIONS

# 61. Demonstrate usage of super().

# 62. Create parent and child constructors using super().

# 63. Demonstrate Method Resolution Order (MRO).

# 64. Create a diamond inheritance structure and explain MRO.

# 65. Create an e-commerce order system using super().

# 66. Create a notification system:
#    - EmailNotification
#    - SMSNotification
#    - PushNotification

# 67. Create multiple inheritance and print MRO using:
#    ClassName.mro()

# 68. Build a payroll system using parent constructor reuse.

# 69. Create a ride-booking system using inheritance and super().

# 70. Create a cloud storage system demonstrating MRO.

# POLYMORPHISM QUESTIONS

# 71. Create different classes with same method:
#    pay_bill()

# 72. Create:
#    - Dog
#    - Cat
#    with same sound() method.

# 73. Create payment methods:
#    - UPI
#    - Card
#    - NetBanking

# 74. Create a shipping system using polymorphism.

# 75. Create different file handlers:
#    - PDF
#    - DOCX
#    - TXT

# 76. Build an online meeting system:
#    - Zoom
#    - GoogleMeet
#    - Teams

# 77. Create an AI assistant with multiple response styles.

# 78. Build a notification service using polymorphism.

# 79. Create a report generator supporting:
#    - CSV
#    - JSON
#    - XML

# 80. Create a chatbot with different language responses.

# OPERATOR OVERLOADING QUESTIONS

# 81. Overload + operator for complex numbers.

# 82. Overload + operator for adding bank balances.

# 83. Overload * operator for matrix multiplication.

# 84. Overload comparison operators for students based on marks.

# 85. Create a shopping cart object supporting +.

# 86. Create a vector class with operator overloading.

# 87. Create a salary object supporting arithmetic operations.

# 88. Create a custom string formatter using operator overloading.

# 89. Create a distance calculator using operator overloading.

# 90. Build a cryptocurrency wallet supporting operations.

# METHOD OVERRIDING QUESTIONS

# 91. Override display() method in child class.

# 92. Create a payment system overriding process_payment().

# 93. Create a social media notification system.

# 94. Create:
#    - Admin
#    - User
#    - Guest
#    overriding permissions.

# 95. Build a food delivery app overriding delivery charges.

# 96. Create a ride fare calculator using overriding.

# 97. Create a streaming app with different subscription plans.

# 98. Build an employee attendance system.

# 99. Create a cloud storage pricing system.

# 100. Create a fraud detection system using overriding.

# ENCAPSULATION QUESTIONS

# 101. Create private attributes using __.

# 102. Create getter and setter methods.

# 103. Create a secure banking system.

# 104. Hide salary details using encapsulation.

# 105. Create a login system protecting passwords.

# 106. Create an ATM system with PIN validation.

# 107. Create a student grading system.

# 108. Create a hospital patient record system.

# 109. Create an online wallet with balance protection.

# 110. Create a secure inventory management system.

# ABSTRACTION QUESTIONS

# 111. Create an abstract class for payment systems.

# 112. Create abstract methods:
#    - login()
#    - logout()

# 113. Create:
#    - Abstract Vehicle
#    - Bike
#    - Car

# 114. Create:
#    - Abstract Shape
#    - Circle
#    - Rectangle

# 115. Build an online food ordering abstraction system.

# 116. Create a cloud service provider abstraction.

# 117. Create a machine learning model abstraction.

# 118. Create an online exam system using abstraction.

# 119. Create an e-commerce delivery abstraction.

# 120. Build a hospital appointment abstraction system.

# ADVANCED INDUSTRY-ORIENTED QUESTIONS

# 121. Build a mini banking application using OOP.

# 122. Build a student management system.

# 123. Build a library management system.

# 124. Build an e-commerce cart system.

# 125. Build a food delivery system.

# 126. Build a hotel room booking system.

# 127. Build a movie ticket booking system.

# 128. Build an employee payroll management system.

# 129. Build an online shopping checkout system.

# 130. Build a cab booking application.

# 131. Build a hospital management system.

# 132. Build a parking management system.

# 133. Build an inventory management application.

# 134. Build a digital wallet application.

# 135. Build a simple CRM system.

# 136. Build a customer support ticket system.

# 137. Build a warehouse management system.

# 138. Build a school ERP mini-module.

# 139. Build a real-time order tracking system.

# 140. Build a smart home automation system.

# INTERVIEW-ORIENTED SCENARIO QUESTIONS

# 141. Why is encapsulation important in banking applications?

# 142. Why do companies prefer abstraction in large projects?

# 143. Explain real-world examples of polymorphism.

# 144. Where is inheritance overused in real projects?

# 145. Explain MRO with a real interview example.

# 146. Why is multiple inheritance risky?

# 147. Explain composition vs inheritance.

# 148. Why are constructors important in frameworks?

# 149. Why does Python not support true method overloading?

# 150. Design an OOP architecture for an online shopping platform.
