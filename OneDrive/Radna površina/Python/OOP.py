#LAMBDA

"""
mnozenje = lambda x: x * 2
broj = int(input("Unesi broj: "))                             #JEDNOSTAVNE MATEMATICKE OPERACIJE
print(mnozenje(broj))
"""

"""
orders = [
    {'product':'Laptop', 'quantity':2, 'unit_price':850},
    {'product':'Phone', 'quantity':3, 'unit_price':500},
    {'product':'Headphones', 'quantity':5, 'unit_price':150}
]

calculate_total = lambda order : order['quantity'] * order['unit_price']           #PRIMER SA LISTAMA

for order in orders:
    total_price = calculate_total(order)
    print(f"{order['product']} : {total_price}")
"""

"""
numbers = list(range(0,10))
print(list(filter(lambda x: x % 2 != 0, numbers)))                                 #FILTER() FUNKCIJA
"""

"""
customers = [
    {'name': 'Mark', 'spending': 75000},
    {'name': 'Anna', 'spending': 120000},
    {'name': 'John', 'spending': 50000},
    {'name': 'Eve', 'spending': 130000}                                            #PRIMER SA FILTER() FUNKCIJOM
]               

vip_customers = list(filter(lambda x: x['spending'] > 100000, customers))
 
for c in vip_customers:
    print(f"{c['name']} is a VIP customer with a spending of {c['spending']}.")   
"""    

"""
products = [
    {'name': 'Laptop', 'price': 85000, 'discount': True},
    {'name': 'Phone', 'price': 50000, 'discount': False},
    {'name': 'TV', 'price': 60000, 'discount': True},
    {'name': 'Camera', 'price': 25000, 'discount': False}
]

products.sort(key=lambda x: x['price'])                                                 #SORT() FUNKCIJA
 
for x in products:
    print(f"{x['name']}: {x['price']} dinars")
"""

"""
prices_in_euros = [10, 20, 15, 30]
prices_in_dinars = list(map(lambda x: x * 117, prices_in_euros))                        #MAP() FUNKCIJA
  
print(prices_in_dinars)
"""

"""
products = [
    {'name': 'Laptop', 'price': 50000},
    {'name': 'Phone', 'price': 30000},
    {'name': 'Tablet', 'price': 20000}
]                                                                                                    #PRIMER SA MAP()

cena_nakon_poreza = list(map(lambda x: {'name': x['name'], 'price': x['price'] * 1.2}, products))
for c in cena_nakon_poreza:
    print(f"{c['name']}: {c['price']}")
"""

"""
status = lambda x: 'Positive number' if x > 0 else 'Negative number'
print(status(10))  # Output: 'Positive number'                                             #IF ELSE FUNKCIJE SA LAMBDOM
print(status(-5))  # Output: 'Negative number'
"""

"""
complex_condition = lambda x: x**2 if x < 5 else (x**3 if x > 5 else x)
print(complex_condition(3))  # Output: 9
print(complex_condition(6))  # Output: 216                                                 #IF ELSE FUNKCIJE SA LAMBDOM
print(complex_condition(5))  # Output: 5
"""

#TRY / EXCEPT

"""
try:
    x = 100 / 0                                                                            #PRIMER
except:
    print("Ne mozes deliti sa nulom")
"""    

"""
try:
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")                                              #PRIMER
    result = str1 / str2
except:
    print("Divison of strings is not possible")
"""

"""
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2                                                               #PRIMER
        print(f"Addition result: {result}")
        break
    except ValueError:
        print("Invalid input. Please enter numbers.")
"""

"""
try:
    x=100
    y=0
    print(x/y)
except NameError:
    print("You won't see me!")
except ZeroDivisionError:                                                                 #FINALLY FUNKCIJA
    print("Hey, you can't divide by zero!")
except Exception:
    print("I'm here just in case you didn't find anything")
finally:
    print("Value of y is:",y)
"""

"""
def divide(a,b):
    if b == 0:
        return 0
    if a > 10 or b > 10:                                                                    #RAISE FUNKCIJA
        raise ArithmeticError("Number is larger than 10")
    else:
        return a/b
print(divide(14,2))
"""

"""
def validate_email(email):
    if '@' not in email:
        raise ValueError("Invalid email address")

email_list = ['marko@example.com', 'anaexample', 'ivan@example.com']
for email in email_list:                                                                   #RAISE PRIMER
    try:
        validate_email(email)
        print(f"The email address {email} is valid.")
    except ValueError as e:
        print (f"Error: {e} ({email})")
"""

#OPSEG (SCOPE)

"""
import builtins
def type(x):
    print(f"You entered x = {x}")                                                          #UGRADJENI OPSEG (Built-in scope)
 
x = 1
print(builtins.type(x))  # calls the built-in type() function
type(x)  # calls our new type() function
"""

"""
x = 20  # Global variable
 
def function():
    print(x)  # Accesses the global variable                                               #GLOBALNI OPSEG (Global scope)
 
function()
"""

"""
total_sales = 1000
def update_sales(new_sale):
    global total_sales
    total_sales += new_sale                                                                #GLOBALNI OPSEG PRIMER
 
update_sales(500)
print(total_sales)  # Now total_sales is 1500
"""

"""
def function_outer():
    x = 5  # Defined in the enclosing scope (outer function)
    def function_inner():
        nonlocal x  # Accesses the variable from the enclosing scope                      #OBUHVATNI (NELOKALNI) OPSEG (Nonlocal scope)
        x = 9
        print(f"Inside inner function x = {x}")
    function_inner()
    print(f"Inside outer function x = {x}")
 
function_outer()
"""

"""
def create_discount():
    discount = 0.1
    def apply_discount():
        nonlocal discount                                                                #OBUHVATNI OPSEG PRIMER
        discount += 0.05
    apply_discount()
    return discount
print(create_discount())  # The result is 0.15
"""

"""
def function():
    x = 10  # Local variable, accessible only within the function
print(x)                                                                                  #LOKALNI OPSEG (Local scope)
 
function()
# print(x)  # This would raise an error because x is not accessible outside the function
"""

"""
# Global variable for total stock
total_stock = 100  # Initial stock
 
def add_to_stock(quantity):
    global total_stock
    total_stock += quantity
    print(f"Added {quantity} units to stock.")
 
def check_stock():
    print(f"Current stock is: {total_stock} units.")
 
def order(product, quantity):
    global total_stock
    product_prices = {
        'Laptop': 80000,
        'Mouse': 1500,
        'Keyboard': 5000,
        'Monitor': 20000
    }
    if product in product_prices:                                                                                   #PRIMER
        unit_price = product_prices[product]
        if quantity <= total_stock:
            total_stock -= quantity
            total_price = unit_price * quantity  # Local variable
            print(f"Order: {product} x{quantity} units. Total price: {total_price} dinars.")
        else:
            print(f"Not enough stock for {product}. Available: {total_stock} units.")
    else:
        print(f"Product {product} not found.")
 
# Main program
check_stock()
add_to_stock(50)
check_stock()
order('Laptop', 20)
check_stock()
order('Mouse', 150)
check_stock()
""" 

#MODULI

#Ključni saveti za rad s modulima
#Dodajmo putanju ka modulu u sys.path pomoću sys.path.append().
#Koristimo alat kao što je pip za instalaciju modula u globalno dostupne direktorijume.

 