# Basic Level
#  1.⁠ ⁠Student Class

# Create a class named Student.
# Add a class attribute school_name = "ABC School"
# Create two objects.
# Display the school name using both objects.

# class Student:
#     school_name = "ABC School"
    
# x=Student()
# y=Student()
# print(x.school_name)
# print(y.school_name)


#  2.⁠ ⁠Mobile Class

# Create a class named Mobile.

# Add class attributes:
# brand = "Samsung"
# country = "Korea"
# Create an object and print both attributes.
# class Mobile:
#     brand = "Samsung"
#     country = "Korea"
# x=Mobile()
# print(x.brand," ",x.country)


#  3.⁠ ⁠Employee Class

# Create a class named Employee.

# Add a method show_company() that prints:
# "Company Name: TechSoft"
# Create an object and call the method.

# class Employee:
#     def show_company(self):
#         print("Company Name: TechSoft")
# emp=Employee
# emp.show_company()

    
    
#  4.⁠ ⁠Car Class

# Create a class named Car.

# Add class attribute wheels = 4
# Create two objects.
# Print the number of wheels using both objects.
# class Car:
#     wheels=4
# car1=Car()
# car2=Car()
# print("Wheels :",car1.wheels)
# print("Wheels :",car2.wheels)


#  5.⁠ ⁠College Class

# Create a class named College.

# Add a class attribute college_name = "Green Valley College"
# Add a method display() to print the college name.
# Create an object and call the method.
# Intermediate Level

# class College:
#     college_name = "Green Valley College"
#     def display(self):
#         print("College name :",College.college_name)
# obj=College()
# obj.display()
    


#  6.⁠ ⁠Laptop Class Attribute Updation

# Create a class named Laptop.

# Add class attribute brand = "Dell"
# Print the brand.
# Update the class attribute to "HP"
# Print the updated value.
# class Laptop:
#     brand="Dell"
# lap=Laptop()
# Laptop.brand="Hp"
# print(Laptop.brand)



#  7.⁠ ⁠Hospital Class""""

# Create a class named Hospital.

# Add class attribute hospital_name = "City Hospital"
# Add method show() to display the hospital name.
# Create two objects and call the method using both objects.
# class Hosppital:
#     hospital_name = "City Hospital"
    
#     def show(self):
#         print(Hosppital.hospital_name)
# obj=Hosppital()
# obj.show()

#  8.⁠ ⁠Bus Class

# Create a class named Bus.

# Add class attribute seats = 40
# Update the number of seats to 50
# Print the updated value.
# class Buss:
#     seats=40
# seat=Buss()
# Buss.seats=50
# print(Buss.seat)
    

#  9.⁠ ⁠Bank Class

# Create a class named Bank.

# Add class attribute bank_name = "Federal Bank"
# Add method display_bank() to print the bank name.
# Create an object and call the method.

# class Bank:
#     bank_name='Fedaral Bank'
    
#     def display(self):
#         print("bank name :",Bank.bank_name)
# s=Bank()
# s.display()

# 10.⁠ ⁠Movie Class
# # Create a class named Movie.

# Add class attribute industry = "Mollywood"
# Delete the class attribute.
# Try printing the attribute after deletion.

# class Movie:
#     industry = "Mollywood"
# print("before Deletion :",Movie.industry)
# del Movie.industry
# print("After Deletion :",Movie.industry)


# Advanced Level
# 11.⁠ ⁠Book Class

# Create a class named Book.

# Add class attribute library = "Central Library"
# Add methods:
# show_library()
# update_library()
# Update the library name using the method and display the updated value.
# class Book:
#     library = "Central Library"
    
#     def show_library(self):
#         print("Librery name is ",Book.library)
        
#     def update_library(self,new):
#         Book.library=new
        
# b1=Book()
# b1.show_library()

# b1.update_library("city librery")

# b1.show_library()



# 12.⁠ ⁠School Class Attribute Deletion

# Create a class named School.

# Add class attribute principal = "Ramesh"
# Print the attribute.
# Delete the attribute.
# Handle the error if the attribute is accessed after deletion.

# class School:
#     principal = "Ramesh"
# print("Principle :",School.principal)

# del School.principal

# try:
#     print("Principle :",School.principal)
# except AttributeError:
#     print("Error Principle transfered")





# 13.⁠ ⁠TV Class

# Create a class named TV.

# Add class attribute company = "Sony"
# Create three objects.
# Update the class attribute to "LG"
# Show that the updated value is reflected in all objects.
# class TV:
#      company = "Sony"

# tv1=TV()
# tv2=TV()
# tv3=TV()

# print(f"Before\n{tv1.company} {tv2.company} {tv3.company}\n")
# TV.company='LG'
# print(f"After\n{tv1.company} {tv2.company} {tv3.company}")


# 14.⁠ ⁠University Class

# Create a class named University.

# Add class attribute country = "India"
# Add method show_country()
# Create multiple objects and call the method.

# class University:
#     country = "India"
#     def show(self):
#          print("My country is ",University.country)
         
# ob1=University()
# ob1.show()

# ob2=University()
# ob2.show()

# ob3=University()
# ob3.show()




# 15.⁠ ⁠Restaurant Class

# Create a class named Restaurant.

# Add class attribute type = "Veg"
# Update the attribute to "Multi Cuisine"
# Delete the attribute.
# Print suitable messages after each operation.
# Challenge Questions

# class Resturant:
#     type = "Veg"

# print("Orginal :",Resturant.type)

# Resturant.type="Multi Cuisine"
# print("Updated  :",Resturant.type)

# del Resturant.type
# try:
#     print(Resturant.type)
# except AttributeError:
#     print("this one was deleted")

# 16.⁠ ⁠Company Management

# Create a class named Company.

# Add class attribute company_name = "Infosys"
# Add methods to:
# Display company name
# Update company name
# Delete company name

# 17.⁠ ⁠Cricket Team

# Create a class named CricketTeam.

# Add class attribute team_name = "India"
# Create multiple objects.
# Change the team name to "Kerala"
# Display the updated value using all objects.

# 18.⁠ ⁠ATM Machine

# Create a class named ATM.

# Add class attribute bank = "SBI"
# Add method show_bank()
# Delete the class attribute and check the output.
# class ATM:
#     bank = "SBI"

#     def show(self):
#         print("your bank is ",ATM.bank)

# bn=ATM()
# bn.show()
# del ATM.show
# try:
#     bn.show()
# except AttributeError:
#     print("this one was deleted")



# 19.⁠ ⁠Airline Class

# Create a class named Airline.

# Add class attribute airline_name = "Air India"
# Add methods to display and update the airline name.
# Create two objects and test the methods.








# 20.⁠ ⁠Shopping Mall

# Create a class named Mall.

# Add class attribute mall_name = "Lulu Mall"
# Create objects.
# Update and delete the class attribute.
# Display outputs before and after each operation.
