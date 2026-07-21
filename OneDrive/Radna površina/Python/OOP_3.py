##ENKAPSULACIJA##

#PROTECTED VREDNOSTI

"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price  # Protected member
        self.quantity = quantity
        
    def update_price(self, new_price):
        if new_price > 0:
            self._price = new_price                                                         #PRIMER
            print(f"Price updated to: {self._price}")                                       #FUNKCIJA ZA AZURIRANJE NECEGA
        else:
            print("Invalid price. Must be greater than zero.")
                   
p = Product("TV", 1000, 10)
p.update_price(1200) # Updates the price
p.update_price(-500) # Reports an error
"""

#PRIVATE VREDNOSTI

"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price  # Private member
        self.quantity = quantity                                                             #PRIMER SA PRIVATE VREDNOSTIMA
              
# Creating an instance of the class
p = Product("TV", 500, 5)
 
# Attempt to access the private member
print(p.__price)  # Error!
"""

"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price  
        self.quantity = quantity
 
 
    # Setter for price with validation
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price                                                     #MENJANJE PRIVATNE VREDNOSTI UZ POMOC GETTER-A I SETTER-A
        else:
            print("Price must be a positive value!")   
   
    def get_price(self):
        return self.__price       
         
p = Product("tv", 500, 5)
p.set_price(330) 
print(p.get_price())
"""

"""
class User:
    def __init__(self, name, age, balance):
        self.__name = name
        self.__age = age
        self.__balance = balance
        
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Godine ne mogu da budu negativne")
            
    def get_age(self):
        return self.__age
        
    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount                                                    #KOMPLEKSNIJI PRIMER SA PRIVATNIM VREDNOSTIMA
        else:
            print("Amount must be positive!")
            
    def withdraw_balance(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount!")
    
    def display_user_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Balance: {self.__balance}")
        
# Testing
user = User("Alex", 25, 1000)
user.display_user_info()
user.add_balance(500)
user.withdraw_balance(300)
user.withdraw_balance(1500)  #Error
user.display_user_info()
"""

#NASLEDJIVANJE

#user.py

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def display_info(self):
        return f"User {self.username}. email; {self.email}"
"""

#standarduser

"""
import User

class StandardUser(User.User):
    def __init__(self, username, email, storage_limit):
        super().__init__(username, email)
        self.storage_limit = storage_limit
"""        

#vipuser                                                                                   #PRIMER                  

"""
import User

class VIPUser(User.User):
    def __init__(self, username, email, vip_level):
        super().__init__(username, email)
        self,vip_level = vip_level
"""

#usertest

"""
import User
import StandardUser
import VIPUser

user1 = User.User("Nick", "nick@gmail.com")

print(user1.display_info())                                   

user2 = StandardUser.StandardUser("Ana", "ana@gmail.com", 10)

print(user2.display_info())

user3 = VIPUser.VIPUser("Peter", "peter@gmail.com", 4)
print(user3.display_info())
"""

#PLOMORFIZAM

"""
# Superclass
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
 
    def display_info(self):
        print(f"Employee: {self.name}, Email: {self.email}")
 
# Subclass that overrides the method
class SalesManager(Employee):                                                                    #PRIMER
    def display_info(self):
        print(f"Sales Manager: {self.name}, Contact: {self.email}")
 
# Creating instances
employee = Employee("Alex Johnson", "alex.johnson@example.com")
manager = SalesManager("Emily Smith", "emily.smith@company.com")
 
# Calling methods
employee.display_info()  # Uses the method from Employee class
manager.display_info()   # Uses the overridden method from SalesManager class
"""

#APSTRAKTNE KLASE

"""
import abc
class Product(abc.ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price
 
    @abc.abstractmethod
    def tax(self):                                                                          #PRIMER - KORISCENJE ABSTRACTMETHOD-E
        pass
 
    def buy(self):
        print("You bought a product",self.name,"with a price",self.tax(),"dollars")

class Shoes(Product):
    def tax(self):
        return self.price * 1.2
    
p = Shoes("Nike Airmax",100)
p.buy()
"""

"""
from abc import ABC, abstractmethod
 
class OnlineProduct(ABC): 
    @abstractmethod
    def calculate_discount(self):
        pass
    @abstractmethod
    def display_details(self):
        pass
    
class DigitalProduct(OnlineProduct):
 
    def __init__(self, name, price, file_size):
        self.name = name
        self.price = price
        self.file_size = file_size
     
    def calculate_discount(self):
        return self.price * 0.10  # 10% popusta na digitalne proizvode                                  #PRIMER MALO KOMPLEKSINJI
     
    def display_details(self):
        print(f"Digital Product: {self.name}, Price: ${self.price}, File Size: {self.file_size}MB")
 
class PhysicalProduct(OnlineProduct):
     
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
     
    def calculate_discount(self):
        return self.price * 0.05  # 5% popusta na fizičke proizvode
     
    def display_details(self):
        print(f"Physical Product: {self.name}, Price: ${self.price}, Weight: {self.weight}kg")
        
ebook = DigitalProduct("E-book on Python", 20, 15)
laptop = PhysicalProduct("Gaming Laptop", 1500, 2.5)
 
ebook.display_details()
laptop.display_details()
 
print(f"Discount for {ebook.name}: ${ebook.calculate_discount()}")
print(f"Discount for {laptop.name}: ${laptop.calculate_discount()}")
"""