#KLASA I OBJEKTI

"""
class Laptop:
    pass                                                          #Prazna klasa radi pokazivanja

item = Laptop()                                                   #Kreiranje objekta koristeci sablon klase

print(f"An object has been created: {item}")
"""

"""
class Product:
    name = ''
    price = 0.0
    quantity = 0
    
item1 = Product()
item1.name = "Laptop"                                                          #PRIMER
item1.price = 1200.99
item1.quantity = 5

item2 = Product()
item2.name = 'Smartphone'
item2.price = 699.50
item2.quantity = 10

print(f"{item1.name}: price = {item1.price}, quantity = {item1.quantity}")
print(f"{item2.name}: price = {item2.price}, quantity = {item2.quantity}")
"""

"""
class Product:  
    name = ""  
    price = 0.0 
    quantity = 0 

    def apply_discount(self):
        self.price *= 0.9                                                   #PRIMER GDE KORISTIMO FUNKCIJU
        
item = Product()
item.price = 150

print(f"Original price: {item.price}")

item.apply_discount()
print(f"Discounted price: {item.price}")
"""

"""
class Calculator:
    number1 = 0
    number2 = 0
    
    def add(self):
        return self.number1 + self.number2
    
    def sub(self):
        return self.number1 - self.number2
    
    def mul(self):                                                            
        return self.number1 * self.number2                                        #PRIMER KALKULATOR
    
    def div(self):
        if self.number2 == 0:
            return "Error: Division by zero!"
        return self.number1 / self.number2

c1 = Calculator()
c1.number1 = 5
c1.number2 = 3
res1 = c1.add()
print(res1)

c2 = Calculator()
c2.number1 = 10
c2.number2 = 4
res2 = c2.mul()
print(res2)
"""

#KONSTRUKTORI

"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quntity = quantity
    
    def display_info(self):
        return(f"Product: {self.name}, Price: {self.price} euros, Quantity: {self.quntity}")                   #KONSTRUKTOR __INIT__
    
product1 = Product("Laptop", 700, 10)
product2 = Product("Phone", 400, 5)

print(product1.display_info())
print(product2.display_info())
"""

"""
class User:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email                                                                           #KONSTRUKTORI PRIMER
        
    def display_user(self):
        return (f"Name: {self.name}, Surname: {self.surname}, Email: {self.email}.")
    
user1 = User("Vuk", "Lazic", "lazicvuk77@gmail.com")

print(user1.display_user())
"""

#ISTANCNI I STATICKI CLANOVI

"""
class Product:
    # Static field (class member)
    tax = 0.2  # 20% tax
 
    def __init__(self, name, price, quantity):
        # Instance fields (specific to each instance)
        self.name = name
        self.price = price
        self.quantity = quantity
 
    def calculate_total_price(self):
        #Calculates the total price of the product including tax.                                     #PRIMER
        return self.price * (1 + Product.tax) * self.quantity
 
    def display_product_info(self):
        #Displays product information.
        print(f"Product: {self.name}")
        print(f"Price per unit (with tax): {self.price * (1 + Product.tax)}")
        print(f"Quantity: {self.quantity}")
        print(f"Total price: {self.calculate_total_price()}")
 
# Testing the class
product1 = Product("Laptop", 700, 2)
product2 = Product("Phone", 400, 3)
 
# Displaying product information
product1.display_product_info()
print()
product2.display_product_info()
"""

"""
class Employee:
    company_name = 'DOO POZAREVAC'
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def display_employee_info(self):                                                #PRIMER 2
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary} dinara")
        print(f"Company: {Employee.company_name}")
        
employee1 = Employee('Vuk Lazic', 'Direktor', 120000)
employee2 = Employee('Luka Zivkovic', 'Tata igre', 110000)

employee1.display_employee_info()
print()
employee2.display_employee_info()
"""

"""
class Product:
    tax = 0.2
 
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
 
    def display_product_info(self):
        print(f"Product: {self.name}")
        print(f"Price per unit (with tax): {self.price * (1 + Product.tax)}")
        print(f"Quantity: {self.quantity}")                                                            #PRIMER SA AZURURANJEM NECEGA
        print(f"Total price: {self.calculate_total_price()}")
 
    def calculate_total_price(self):
        return self.price * (1 + Product.tax) * self.quantity
 
    def update_price(self, new_price):
        #Updates the product price.#
        self.price = new_price
        print(f"Price for {self.name} has been updated to {self.price}")
 
# Testing the method
product1 = Product("Laptop", 700, 2)
product1.display_product_info()
product1.update_price(900)
product1.display_product_info()
"""

#STATICKE METODE

"""
class Product:
    tax = 0.2  # Static field for tax
 
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity                                                     #PRIMER
  
    @staticmethod
    def set_tax(new_tax):
        #Static method to set a new tax rate.
        Product.tax = new_tax
        print(f"New tax rate set to: {Product.tax * 100}%")
        
nova = Product.set_tax(0.25)
print(nova)
"""

"""
class Employee:
    company_name = "TecnCrop"
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary                                                           #PRIMER
        
    @staticmethod
    def set_company_name(new_name):
        Employee.company_name = new_name
        print(f"Company name updated to: {Employee.company_name}")
        
Employee.set_company_name("InnoTech")
"""

#KLASNE METODE

"""
class User:
    def __init__(self, name, userid, number): 
        self.name = name
        self.userid = userid
        self.number = number
 
    @classmethod
    def input_user(cls):
        #Allows direct input of user data through the class.                                     #PRIMER
        name = input('Name: ')
        userid = input('User ID: ')
        number = input('Phone number: ')
        return cls(name, userid, number)
 
# Adding a new user through the class method
new_user = User.input_user()
print(f"Name: {new_user.name}, UserID: {new_user.userid}, Number: {new_user.number}")
"""

"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @classmethod                                                                                        #PRIMER
    def create_from_input(cls):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        return cls(name, price, quantity)
    
product1 = Product.create_from_input()
print(f"Product: {product1.name}, Price: {product1.price}, Quantity: {product1.quantity}")
"""