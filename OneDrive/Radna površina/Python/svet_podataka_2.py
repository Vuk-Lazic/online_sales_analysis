#CSV

"""
import csv

with open('books.csv', 'r') as file:
    reader = csv.reader(file)                                                      #CITANJE FAJLA
     
    for row in reader:
        print(row[0])                #CITANJE ODRADJENOG DELA FAJLA
"""

"""
import csv
 
with open('books.csv', 'a', newline='') as file:
    writer = csv.writer(file)                                                                      #UPISIVANJE NOVE LISTE U FAJL
    writer.writerow(["Thinking, Fast and Slow", "Daniel Kahneman", 2011, "Psychology"])
"""

"""
import csv
 
with open("books.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)                                             #CITANJE PODATAK POMOCU NAZIVA
    
    for row in csv_reader:
        print(row["published"])
"""

"""
import csv
 
with open("books.csv", mode="r") as file:
    fieldnames = ["title", "author", "published", "genre"]                   #U SLUCAJU DA NEMAMO OBELEZENE KOLONE
    csv_reader = csv.DictReader(file, fieldnames=fieldnames)                 #DODAVANJE I ISPISIVANJE ZADATAOG
    for row in csv_reader:
        print(row["title"])
"""

"""
import csv
 
with open('my_book.csv', 'w', newline='') as csvfile:
    fieldnames = ["title", "author", "published", "genre"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)                             #KREIRANJE CSV FAJLAI UPISIVANJE PODATAKA U NJEGA (DICT)
 
    writer.writeheader()
    writer.writerow({'title': 'The Alchemist', 'author': 'Paulo Coelho', 'published': 1988, 'genre': 'Adventure'})
"""

"""
import csv
 
with open('my_book.csv', 'a', newline='') as csvfile:
    fieldnames = ["title", "author", "published", "genre"]                                   #DODAVANJE PODATAKA U VEC POSTOJECI CSV FAJL
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writerow({'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'published': 1813, 'genre': 'Romance'})
"""

#PANDAS

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                                 #CITANJE POMOCU PANDAS
print(df.to_string())
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                               #KOLIKO REDOVA I KOLONA IMA
print(df.shape)
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                               
print(df.shape[0])            #ILI UMESTO INDEKSA NAPISEMO IME KOLONE      #BROJ REDOVA
print(df.shape[1])                                                         #BROJ KOLONA
"""  

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                              #ITERACIJA KROZ REDOVE
 
for index, row in df.iterrows():
    print(row.to_string())
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                            #ISPISIVANJE SAMO ODREDJENOG 
 
for index, row in df.iterrows():
    print(row["title"])                   #ILI NAPISATI INDEKS                     
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                           #POKAZIVANJE KOJI TIP JE PODATAK U DATAFRAME-U
 
for index, row in df.iterrows():
    print(type(row)) 
"""

""" 
import pandas as pd                                                     #UPISIVANJE PODATAKA U FAJL POMOCU PANDAS BIBLIOTEKE
 
df = pd.DataFrame(data=[[101, "The Alchemist", "Paulo Coelho", 1988, "Adventure"]],columns=[ 'id', 'title', 'author', 'published', 'genre'])
 
df.to_csv('my_book.csv', index=False)
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')
print(df.title.to_string())


import pandas as pd                                                  #DVA NACINA ISPISIVANJA NECEGA IZ DOKUMENTA

df = pd.read_csv('books_csv')
print(df['title'].to_string())
"""

"""
import pandas as pd
  
df = pd.read_csv('books.csv')                                                     #CITANJE PODATAKA POMOCU ILOC FUNKCIJE
print(df.iloc[2].to_string())
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                                     #CITANJE VISE REDOVA 
 
print(df.iloc[2:4].to_string())
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                                     #CITANJE VREDNOSTI POJEDINACNIH CELIJA
 
print(df.iloc[2, 1])
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv')                                                     #CITANJE VREDNOSTI POJEDINACNIH CELIJA POMOCU NAZIVA
 
print(df.loc[2, "title"])
"""

"""
import pandas as pd
  
df = pd.read_csv('books.csv', index_col="id")                                     #ISPISIVANJE VREDNOSTI POMOCU LOC FUNKCIJE
 
print(df.loc[103, "title"])
"""