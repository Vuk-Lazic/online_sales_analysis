"""
import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv('books.csv')                               #ISPISIVANJE SVIH DESKRIPTIVNIH VREDNOSTI
df = prepare_data(data)

print(df.describe(include = 'all')) 
"""

#PROSEK(ARITMETICKA SREDINA)

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)                                             #PRIMER ARITMETICKE SREDINE
 
average_price = df["price"].mean()
print(f"Average book price: ${average_price:.2f}")

average_page_count = df["page_count"].mean()
print(f"Average amount of pages per book: {average_page_count:.2f}")
"""

#MEDIANA

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)                                               #PRIMER RACUANANJA MEDIANE    
  
median_price = df["price"].median()
print(f"Median book price: ${median_price:.2f}")

median_page_count = df["page_count"].median()
print(f"Median page count: {median_page_count:.2f}")
"""

#MOD

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
genre_mode = df["genre"].mode()
print(f"Genre mode: {", ".join(genre_mode.astype(str))}")

most_common_authors = df["author"].mode()
print(f"Most common author: {", ".join(most_common_authors.astype(str))}")
"""

#AGREGACIJA PODATAKA

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
data = {
    'mean': df['ratings_count'].mean(),
    'median':df['ratings_count'].median(),
    'mode':df['ratings_count'].mode().tolist(),
    'sum':df['ratings_count'].sum(),                                    #AGREGATNE FUNKCIJE
    'count':df['ratings_count'].count(),
    'min':df['ratings_count'].min(),
    'max':df['ratings_count'].max()
}
 
for key, value in data.items():
    print(f"{key}: {value}")
"""

"""
import pandas as pd
 
df = pd.read_csv('products_dataset.csv')
 
aggregated_data = {
    'Mean Price': df['price'].mean(),
    'Median Rating': df['rating'].median(),
    'Mode Ratings_Count': df['rating'].mode().tolist(),              #PRIMER AGREGATNIH FUNKCIJA
    'Total Stock': df['stock'].sum(), 
    'Total Products': df['product_id'].count(),        
    'Min Price': df['price'].min(),
    'Max Price': df['price'].max()
}
 
for key, value in aggregated_data.items():
    print(f"{key}: {value}")
"""

#GRUPISANJE

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
grouped_data = df.groupby("genre")                                     #GRUPISANJE
  
for genre, group in grouped_data:
    print(f"Genre: {genre}")
    print(group)
    print("-" * 60)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')                             
df = prepare_data(data) 
  
grouped_data = df.groupby("section")                                   #PRIMER GRUPISANJA
 
for section, group in grouped_data:
    print(f"Section: {section}")
    print(group)
    print("-" * 60)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')                                            #KOMBINACIJA GRUPISANJA I AGREGATNIH FUNCKIJA
df = prepare_data(data) 
 
avg_price_per_genre = df.groupby("genre")["price"].mean().sort_values(ascending=False)
 
print(avg_price_per_genre)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)                                                   #PRIMER KOMBINACIJE GRUPISANJA I AGREGATNIH FUNKCIJA
 
rentals_per_author = df.groupby("author")["times_borrowed"].sum().sort_values(ascending=False)
 
print(rentals_per_author)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
price_stats = df.groupby('genre').agg(                                  #KORISCENJE VECEG BROJA AGREGATNIOH FUNCKIJA POMOCU .agg()
    avg_price=('price', 'mean'),
    median_price=('price', 'median')
)
 
print(price_stats)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')                                     #KORISCENJE .agg() PRILEDJIVANJEM RECNIKA
df = prepare_data(data)
 
price_stats = df.groupby('genre').agg({
    "price": ['mean', 'median']
})
 
print(price_stats)
"""

"""
import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)
 
author_stats = df.groupby("author").agg({
    "times_borrowed": ["sum", "mean", "max"],                                       #KORISCENJE .agg() PRILEDJIVANJEM RECNIKA
    "rating": ["max"],
    "ratings_count": ["sum"],
    "price": ["mean"]
})
 
author_stats_sorted = author_stats.sort_values(("times_borrowed", "sum"), ascending=False)
 
print(author_stats_sorted)
"""

#PROJEKAT

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
inventory_gap = df.groupby('section').agg({                                                   #SUMA SUMARUM LEKCIJE
    'title': 'count',
    'times_borrowed': 'sum'
})
 
inventory_gap['titles_to_borrow_ratio'] = inventory_gap['times_borrowed'] / inventory_gap['title'] 
 
print(inventory_gap.sort_values(by=['titles_to_borrow_ratio'], ascending=False))
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
inventory_gap  = (
    df.groupby('author')
      .agg(
          total_times_borrowed=('times_borrowed', 'sum'),
          available_titles=('title', 'count')
      )
      .sort_values(by='total_times_borrowed', ascending=False)
      .head(20)
)
 
inventory_gap['copies_to_borrow_ratio'] = inventory_gap['total_times_borrowed'] / inventory_gap['available_titles']
 
print(inventory_gap.sort_values(by=['copies_to_borrow_ratio'], ascending=False))
"""