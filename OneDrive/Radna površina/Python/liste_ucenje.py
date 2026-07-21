#LISTE

"""
voce = ["banana","jabuka", "lubenica"]

if "banana" in voce:
    print("Nalazi se u listi")                                                           #PRONALAZENJE U LISTI
else:
    print("NE nalazi se u listi")
"""

"""
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
products[-1] = "Smart Watch"                                                             #MENJANJE NEKOG PROIZVODA U LISTI
print("Nova lista: ")
print(products)
"""

"""
products =[]

for i in range(5):
    p = input("unesite ime proizvoda: ")         
    products.append(p)


pozicija = int(input("Unesite poziciju na kojoj zelite da umetnete proizvod:"))           #UBACIVANJE I PRODUZAVANJE = KORISCENJE APPEND i INSERT
p = input("Unesite ime proizvoda:")

products.insert(pozicija,p)
print(products)

"""

"""
products = ["Phone", "Laptop", "Phone", "TV", "Headphones", "Camera", "Phone"]
while "Phone" in products:
    products.remove("Phone")                                                    #IZBACIVANJE IZ LISTE UZ POMOC WHILE i REMOVE    
print(products)
"""

"""
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
removed_item = products.pop(3)                                                  #IZBACIVANJE IZ LISTE UZ POMOC POP 
print(products)
print("The product at position 3 was:", removed_item)
"""

"""
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
del products[3]                                                                 #IZBACIVANJE IZ LISTE UZ POMOC DEL
print(products)
"""

"""
list1 = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
list2 = ["Laptop Stand", "Mouse", "Keyboard"]                                   #SPAJANJE LISTE UZ POMOC +
                                                      
combined_list = list1 + list2
print("Combined List:", combined_list)
"""

"""
list1 = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
list2 = ["Laptop Stand", "Mouse", "Keyboard"]                                   #SPAJANJE LISTE UZ POMOC .EXTEND()

list1.extend(list2)
print("Extended List1:", list1)
"""

"""
all_products = ("Laptop", "Phone", "TV", "Phone", "Camera")                     #BROJANJE ELEMENATA U LISTI
print(all_products.count("Phone")) 
"""

"""
all_products = ("Laptop", "Phone", "TV", "Phone", "Camera")                     #PRONALAZENJE KOJI ELEMENT JE KOJI INDEX
print(all_products.index("TV"))                                                 
"""

"""
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
products.sort()                                                                 #SORTIRANJE LISTE
print(products)
"""

"""
products = ["Laptop", "TV", "Camera", "Phone", "Printer"]
products.sort(reverse=True)                                                     #SORTIRANJE LISTE UNAZAD
print(products)
"""

"""
products = ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]
for i in range(len(products)):                                                                    #PRIMER ZA BROJANJE LISTE
    print(f"Element: {i + 1}: {products[i]}")      #Ovo znaci da ce umesto brojeva ispisati ono sto je u promenljivoj po redoledu brojeva
"""

"""
# List of products
products = ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]
# Prompt the user to enter a keyword
keyword = input("Enter the keyword to search for in product names: ")                             #TRAZENJE NECEGA U LISTI
# Loop through the products and print those containing the keyword
for product in products:
    if keyword in product:
        print(product)
"""

"""
prices = [100, 250, 150, 300, 50, 200, 175, 80, 120, 275]
max_price = int(input("Enter the maximum price you consider affordable: "))
affordable_count = 0

for price in prices:                                                               #Zadatak mozda bude koristan nekada u zivotu
    if price <= max_price:
        affordable_count += 1
print(f"The number of products with a price less than or equal to {max_price} is: {affordable_count}")
"""

"""
products = [['bread', 'egss', 'potato'],
            ['cofffe', 'tea', 'water'],
            ['pizza', 'fish', 'ice cream']]

for category in products:                                                         #PRIMER 2D LISTE
    for p in category:
        print(f"Group: {products.index(category), {p}}")
    print('')

"""

#TUPLE

"""
suma = 0
orders = [
    (101, "John Doe", 299.99, "Pending"),
    (102, "Jane Smith", 149.50, "Shipped"),
    (103, "Mike Johnson", 89.75, "Deliverd"),
    (104, "Emily Davis", 249.99, "Pending"),
]
        
for order in orders:
    id, name, price, status = order
    if status == "Pending":                                                           #DODELJIVANJE PROMENILJIVE U LISTI
        print(order)

for order in orders:
    id, name, price, status = order
    #if status == "Deliverd" or status == "Shipped":
    if status in ['Shipped', 'Deliverd']:                       #Dva nacina kako da manipulisemo #Ovaj drugi nacin koristimo za vise stvari koje imamo da trazimo
        suma += price
print(suma)
"""

#SETOVI

"""
products_in_stock = {"Laptop", "Phone", "TV", "Laptop"}

print(products_in_stock)

products_in_stock.add("Tablet")                                                   #DODAVANJE U SETOVE UZ POMOC .add() 
print(products_in_stock)

products_in_stock.remove('TV')                                                    #UKLANJANJE UZ POMOC .remove()  
print(products_in_stock)
"""

"""
A = {1, 2, 3}
B = {3, 4, 5} 

print(A | B)   # unija      .union()                                              #UNIJE
print(A & B)   # presek     .intersection()   
print(A - B)   # razlik     .differnce()    
"""

#RECNIK

"""
order = {
    "customer": "John Smith",
    "product": "Laptop",
    "price": 75000,
    "date": "2024-10-15",
    "status": "deliverd",
    "delivery_service": "DHL"
}

print(order["customer"])                                              #Printovanje necega iz recnika 
order["price"] = 70000                                                #Ovako se menja nesto u recniku
order["phone"] = "+3819832497"                                        #Dodavanje necega
del order["status"]                                                   #Brisanje necega
for key, value in order.items():                                      #Printovanje uz pomoc ITEMS()  
    print(f"{key} : {value}")                                                                         #} DVA NACINA PRINTOVANJA
for key in order.keys():                                               #Printovanje uz pomoc KEYS()
    print(f"{key} - {order[key]}")
"""

"""
sales_data  = [
    {'product': 'Smartphone', 'month': 'January', 'quantity': 150},
    {'product': 'Laptop', 'month': 'January', 'quantity': 80},
    {'product': 'Tablet', 'month': 'January', 'quantity': 50},
    {'product': 'Smartphone', 'month': 'February', 'quantity': 200},
    {'product': 'Laptop', 'month': 'February', 'quantity': 90},
    {'product': 'Tablet', 'month': 'February', 'quantity': 60},
    {'product': 'Smartphone', 'month': 'March', 'quantity': 250},
    {'product': 'Laptop', 'month': 'March', 'quantity': 100},
    {'product': 'Tablet', 'month': 'March', 'quantity': 70},
 
]
total_sales = {}
total_sales_by_month = {}                                                        #ZADATAK SA IZVALECENJEM IZ LISTE UZ POMOC RECNIKA

for i in sales_data:
    product = i['product']
    quantity = i['quantity']
    total_sales[product] = total_sales.get(product, 0) + quantity

print("Total sales per product:")
for product, total in total_sales.items():
    print(f"{product}: {total}")

for entry in sales_data:
    month = entry['month']
    quantity = entry['quantity']
    total_sales_by_month[month] = total_sales_by_month.get(month, 0) + quantity

print("Total sales per month:")
for month, total in total_sales_by_month.items():
    print(f"{month}: {total}")
"""

"""
customers = [
    {   "first_name": "Emma", 
        "last_name": "Smith", 
        "purchases": 
    [ 
        ("Laptop", 1200.0),             
        ("Mouse", 50.0) 
        ] 
    }, 
    { 
        "first_name": "Jamie", 
        "last_name": "Lee", 
        "purchases": [ 
            ("Smartphone", 800.0), 
            ("Headphones", 100.0) 
        ] 
    }, 
    { 
        "first_name": "Alex", 
        "last_name": "Taylor", 
        "purchases": [ 
            ("Tablet", 400.0), 
            ("Keyboard", 60.0), 
            ("Monitor", 300.0) 
        ] 
    } 
]                                                                                               #PRIMER ZA RECNIK
 

def ukupno_potroseno(customers):
    for customer in customers:
        total_spent = sum(item[1] for item in customer["purchases"])
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
        print(f"Total spent: {total_spent:.2f} euros\n")
        
def total_items_purchased(customers):
    for customer in customers: 
        total_items = len(customer["purchases"])
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
        print(f"Total items purchased: {total_items}\n")
        
def most_expensive_purchase(customers): 
    for customer in customers: 
        most_expensive = max(customer["purchases"], key=lambda x: x[1]) 
        print(f"Customer: {customer['first_name']} {customer['last_name']}") 
        print(f"Most expensive item: {most_expensive[0]} - {most_expensive[1]:.2f} euros\n")

def generate_report(customers): 
    print("Calculating total spent by each customer:") 
    ukupno_potroseno(customers)    
    print("Calculating total items purchased by each customer:") 
    total_items_purchased(customers)    
    print("Finding the most expensive purchase for each customer:") 
    most_expensive_purchase(customers)       
 
generate_report(customers)

"""

#REDOVI

"""
customers = []

customers.append("Alice")
customers.append("Bob")
customers.append("Charlie")
print(f"Queue: {customers}")                                               #PRIMER REDOVA

while len(customers) > 0:
    next_customer = customers.pop(0)
    print(f"Next customer is: {next_customer}")
    print(f"Queue: {customers}")
"""