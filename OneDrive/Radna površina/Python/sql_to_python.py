#SQL

"""
import mysql.connector  

my_connetion = mysql.connector.connect(
    host="localhost",
    port= 3306,
    user= "root",                                                 #POVEZIVANJE SA SQL I PRAVLJENJE KURSORA
    password= "LazaBosanac1",                                     #OVO STOJI SVUDA KADA KUCAMO ZA SQL NA POCETKU
    database= "library"
)

cursor = my_connetion.cursor()
"""

#CREATE

"""
sql_query = "INSERT INTO Author (firstname, lastname) VALUES ('Desanka', 'Maksimovic')"
cursor.execute(sql_query)  
my_connetion.commit()                                                                    #DIREKTAN NACIN DODAVANJA
print("Author added successfully.")
"""

"""
#User input for author details
firstname = input("Enter the author's first name: ").strip()
lastname = input("Enter the author's last name: ").strip()
 
# SQL query with parameters (safe way to execute queries)
sql_query = "INSERT INTO Author (firstname, lastname) VALUES (%s, %s)"
values = (firstname, lastname)
 
# Executing the SQL query                                                       #SIGURNIJI NACIN DODAVANJA
cursor.execute(sql_query, values)
my_connetion.commit()  # Saves changes to the database
 
print(f"Author {firstname} {lastname} successfully added to the database.")
 
# Closing the database connection
cursor.close()
my_connetion.close()
print("Database connection closed.")
"""

#READ

"""
# Defining the SQL query
sql_query = """#SELECT title, published  
               #FROM Book 
               #WHERE genre_id = (SELECT genre_id FROM Genre WHERE name = 'Fiction')"""
""" #obrisati i ovo
# Executing the query
cursor.execute(sql_query)  
 
# Fetching all results                                                                #ISCITAVANJE PODATAKA IZ BAZE
books = cursor.fetchall()  
 
# Displaying results
for book in books:
    print(book)
"""

"""
cursor.execute("SELECT COUNT(*) FROM Book")
total_books = cursor.fetchone()[0] # Retrieving the first value from the first row 
  
print(f"Total number of books in the library: {total_books}")                         #PRIKAZIVANJE NROJA NECEGA
"""

#UPDATE

"""
import mysql.connector
 
# Connecting to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
)
 
# Creating a cursor to execute queries
cursor = conn.cursor()
 
# SQL query to update the publication year
sql_query = """#UPDATE Book  
               #SET published = 2025 
               #WHERE title = 'To Kill a Mockingbird'"""                         
""" #obrisati ovo                          
# Executing the query                                                            #PRIMER UPDATE-A
cursor.execute(sql_query)
conn.commit()  # Saving changes to the database
 
print("Data successfully updated.")
 
# Closing the connection
cursor.close()
conn.close()
print("Database connection closed.")
"""

"""
sql_query = "UPDATE Book SET published = %s WHERE title = %s"
values = (2025, "To Kill a Mockingbird")
  
cursor.execute(sql_query, values)                                             #BEZBEDNIJI NACIN UPDATE-A
conn.commit()
print("Data has been successfully updated.")
"""

#DELETE

"""
import mysql.connector
 
# Connecting to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
)
 
# Creating a cursor
cursor = conn.cursor()
 
# SQL query to delete books published before 1950 
sql_query = "DELETE FROM Book WHERE published < 1950"                            #PRIMER BRISANJA
 
# Executing the query
cursor.execute(sql_query)
conn.commit()  # Saving changes to the database
 
print("Old books have been deleted from the database.")
 
# Closing the connection
cursor.close()
conn.close()
print("Database connection closed.")
"""

#POVEZIVANJE SQL SA PANDASOM I DRUGIM BILBLIOTEKAMA

"""
import mysql.connector  
import pandas as pd

my_connetion = mysql.connector.connect(
    host="localhost",
    port= 3306,
    user= "root",
    password= "LazaBosanac1",
    database= "library"                                                         #PANDAS
) 

# SQL query to retrieve book data
query = "SELECT book_id, title, published, genre_id FROM Book"
df_books = pd.read_sql(query, my_connetion)
 
# Displaying the first 5 rows of data
print(df_books.head())
 
# Closing the database connection
my_connetion.close()

print(df_books['genre_id'].unique())                                          #PRIKAZIVANJE JEDINSTVENIH VREDNOSTI IZ KOLONE

df_grouped = df_books.groupby("genre_id")["book_id"].count()
print(df_grouped)                                                             #GRUPISANJE PODATAKA PO NEKOJ KOLONI I PRIKAZIVANJE BROJA NECEGA U SVAKOJ GRUPI
"""

#MATPLOTLIB I SEABORN

"""
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
 
# Creating a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LazaBosanac1",
    database="library"
)
 
# SQL query to retrieve book data 
query = "SELECT book_id, title, published, genre_id FROM Book"                           #PRAVLJENJE HISTOGRAMA SA MATPLOTLIBOM
df_books = pd.read_sql(query, conn)      
  
# Display the first 5 rows of data
print(df_books.head())
 
# Closing the database connection
conn.close()
 
# Creating a histogram to visualize the distribution of books by publication year
plt.hist(df_books['published'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Published Year")
plt.ylabel("Number of Books")
plt.title("Distribution of Books by Year")
plt.show()
"""

"""
import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# Creating a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LazaBosanac1",
    database="library"
)
 
# SQL query to retrieve book data
query = "SELECT book_id, title, published, genre_id FROM Book"
df_books = pd.read_sql(query, conn)                                                      #PRAVLJENJE BAR CHARTA SA SEABORNOM I MATPLOTLIBOM
 
# Closing the database connection
conn.close()
 
# Grouping data by genre and counting the number of books
df_grouped = df_books.groupby("genre_id")["book_id"].count()
 
# Data visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=df_grouped.index, y=df_grouped.values, palette="viridis")
 
plt.xlabel("Genre (ID)")
plt.ylabel("Number of Books")
plt.title("Number of Books per Genre")
plt.xticks(rotation=45)  # Rotating labels if there are many
plt.show()
"""






