#NEDOSTAJUCE VREDNOSTI

"""
import pandas as pd
from preprocessing import prepare_data    #Ne zaboravi da koristis ovu skriptu
 
data = pd.read_csv('books.csv')
 
df = prepare_data(data)
 
print(df.isnull().sum())                               #PRIKAZ NEDOSTAJUCIH VREDNOSTI "PO KOLONAMA"
"""

#UKLANJANJE KOLONA

"""
import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv('books.csv')                                 #BRISANJE NEPOTREBNIH REDOVA

df = prepare_data(data)

df.dropna(axis=1, thresh=1500, inplace = True)

print(df.isnull().sum())
"""

"""
import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv('books.csv')                                 

df = prepare_data(data)
 
rows_count = df.shape[0]                                                   #BRISANJE KOLONA NA OSNOVU PROCENTA NEDOSTAJUCIH PODATAKA
df.dropna(axis=1, thresh=(rows_count*0.75), inplace = True) 

print(df.isnull().sum())
"""

"""
import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv('books.csv')

df = prepare_data(data)

#df.drop([212,75,698,152], axis = 0, inplace = True)          #BRISANJE NEPOTREBNIH "REDOVA" UZ POMOC "DROP" METODE
#df.dropna(axis = 0, thresh = df.shape[1] - 18,inplace = True)    #BRISANJE NEPOTREBNIH "REDOVA" UZ POMOC "DROPNA" METODE
missing_per_row = df.isna().sum(axis=1)
missing_per_row_sorted = missing_per_row.sort_values(ascending=False)

#print(missing_per_row_sorted.head(30))

df.dropna(subset = ['catalog_position', 'title', 'author'], how = 'all', inplace = True)      #BRISANJE KOLONA UZ POMOC "SUBSET" METODE

missing_rows = df[df[['catalog_position', 'title', 'author']].isna().all(axis = 1)] 

print(missing_rows)
"""

#IMPUTACIJA NEDOSTAJUCIH VREDNOSTI

"""
import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv('books.csv')

df = prepare_data(data)

df['title'] = df['title'].fillna("Unknown Title")                            #IMPUTACIJA NEDOSTAJUCIH VREDNOSTI

missing_count = df['title'].isna().sum()
print("Missing values count in the column 'title':", missing_count)
"""

#DEDUPLIKACIJE

#POPTUNI DUPLIKATI

"""
import pandas as pd

df = pd.read_csv('books.csv')                                           #PREBROJAVANJE UKUPNOG BROJA DUPLIKATA

print(df.duplicated().sum())
"""

"""
import pandas as pd

df = pd.read_csv('books.csv')                                            #PRIKAZIVANJE POPTPUNIH DUPLIKATA

print(df[df.duplicated(keep=False)])
"""

"""
import pandas as pd

df = pd.read_csv('books.csv')                                            #UKLANJANJE POTPUNIH DUPLIKATA

df.drop_duplicates(keep='first', inplace=True, ignore_index=False)
"""

"""
import pandas as pd
df = pd.read_csv('online_shop_with_duplicates.csv')
total_duplicates = df.duplicated().sum()
print(f"Total duplicates: {total_duplicates}")
print("Full duplicates: ")
print(df[df.duplicated()])                                                 #PRIMER UKLANJANJA DUPLIAKTA
#remove full duplicates 
df.drop_duplicates(keep='first', inplace=True, ignore_index=False)
#check duplicates again...
total_duplicates = df.duplicated().sum()
print(f"Total duplicates after deduplication: {total_duplicates}")
"""

#DELIMICNI DUPLIKATI

"""
import pandas as pd

df = pd.read_csv('books.csv')                                               #PRIKAZ BROJA DUPLIKATA

print(df.duplicated(subset=['catalog_position']).sum())          
"""

"""
import pandas as pd

df = pd.read_csv('books.csv')                                                            #PRIKAZ DUPLIKATA

duplicate_rows= df[df.duplicated(subset=['catalog_position'],keep=False)]
print(duplicate_rows.filter(items=['catalog_position','title', 'author']).sort_values(by='title'))
"""

"""
import pandas as pd

df = pd.read_csv('books.csv')

row1 = df.loc[546]
row2 = df.loc[1021]
differences = row1.compare(row2)                                       #PREGLED RAZLIKA IZMEDJU REDOVA
print(differences)


df.drop_duplicates(subset=["catalog_position"],keep='first', inplace=True, ignore_index=False)  #NE ZNAM ZA OVO STA TREBA
"""

"""
import pandas as pd

df = pd.read_csv('books.csv')


print(df.duplicated(subset=['title', 'author']).sum())
duplicate_rows = df[df.duplicated(subset=['title', 'author'], keep=False)]                                #SRECNO SA OVIM DELOM LEKCIJE
print(duplicate_rows.filter(items=['catalog_position', 'title', 'author']).sort_values(by='title'))
"""

#VALIDACIJA PODATAKA

"""
import pandas as pd
import numpy as np
from preprocessing import prepare_data

data = pd.read_csv('books.csv')                                                                       #PRIMER VALIDACIJE PODATAKA
df = prepare_data(data)

suspicious_values = df[(df['year_published'] < 1450) | (df['year_published'] > 2025)]
print(suspicious_values.filter(items=['catalog_position', 'title', 'author', 'year_published'])) 

suspicious_values = df[(df['total_copies'] < 0)]
print(suspicious_values.filter(items=['title', 'author', 'total_copies']))                            #JOS PRIMERA PROVERE VALIDNOSTI

suspicious_values = df[(df['times_borrowed'] < 0)]
print(suspicious_values.filter(items=['title', 'author', 'times_borrowed']))
"""

"""
def find_negative_values(df, column_name):
    negative_values = df[(df[column_name] < 0)]
    return negative_values
ratings_count_negative = find_negative_values(df, "ratings_count")
print(ratings_count_negative.filter(items=['title', 'author', 'ratings_count']))
ratings_count_negative = find_negative_values(df, "price")
print(ratings_count_negative.filter(items=['title', 'author', 'price']))
ratings_count_negative = find_negative_values(df, "page_count")
print(ratings_count_negative.filter(items=['title', 'author', 'page_count']))                             #KOMPLEKSINIJI PRIMER PROVERE VALIDACIJE
ratings_count_negative = find_negative_values(df, "dimensions_width")
print(ratings_count_negative.filter(items=['title', 'author', 'dimensions_width']))
ratings_count_negative = find_negative_values(df, "dimensions_thickness")
print(ratings_count_negative.filter(items=['title', 'author', 'dimensions_thickness']))
ratings_count_negative = find_negative_values(df, "dimensions_height")
print(ratings_count_negative.filter(items=['title', 'author', 'dimensions_height']))
"""

"""
import pandas as pd
import numpy as np
from preprocessing import prepare_data                                 #VALIDACIJA LOGICKIH VEZA IZMEDJU PODATAKA
 
data = pd.read_csv('books.csv')                                        
df = prepare_data(data)

mask = (df['times_borrowed'] == 0) & (df['last_borrowed_date'].notna() | df['rating'].notna() | df['ratings_count'].notna())
df.loc[mask, 'last_borrowed_date'] = pd.NaT
df.loc[mask, 'rating'] = np.nan                                 #NAKON PROVERE RADIMO OVA TRI ILI KO IH VEC IMA
df.loc[mask, 'ratings_count'] = np.nan

mask = (df['times_borrowed'] == 0) & (df['last_borrowed_date'].notna() | df['rating'].notna() | df['ratings_count'].notna())
suspicious_values  = df[mask]
print(suspicious_values.filter(items=['catalog_position', 'title', 'times_borrowed', 'last_borrowed_date', 'rating', 'ratings_count']))     
"""

"""
import pandas as pd
import numpy as np
from preprocessing import prepare_data

data = pd.read_csv('books.csv')                                                      #JOS JEDAN PRIMER
df = prepare_data(data)

mask = (df['ratings_count'].isna()) & (df['rating'].notna())               #PA ONDA OVO
df.loc[mask, 'rating'] = np.nan

mask = (df['ratings_count'].isna()) & (df['rating'].notna())               #PRVO PROVERAVAMO PA ONDA MENJAMO PODATKE
suspicious_data = df[mask]

print(suspicious_data.filter(items= ['catalog_number', 'title', 'author', 'ratings_count', 'rating']))
"""

#STANDARDIZACIJA

"""
import pandas as pd
import numpy as np
from preprocessing import prepare_data

data = pd.read_csv('books.csv')                                        
df = prepare_data(data)                                          #DETEKCIJA KANDIDATA ZA STANDARDIZACIJU
 
print(df['language'].unique())
print(df['language'].value_counts())
print(df['language'].cat.categories)
"""

"""
import difflib
 
products = [
    "Apple iPhone 12",
    "Apple iPhone 12 Pro",
    "Samsung Galaxy S21",
    "Samsung Galaxy S21 Ultra",                                                #PRIMER UPROSCENOG KORISCENJA DIFFLIBA (FUZZY METODA TEHNIKE)
    "Google Pixel 5",
    "Gooogle Pixel 5", #input error
    "Google Pixl 5", #input error
    "OnePlus 9",
    "OnePlus 9 Pro"
]
 
query = "Google Pixel 5"
matches = difflib.get_close_matches(query, products, n=3, cutoff=0.8)
 
print(matches)
"""

"""
import pandas as pd
import difflib
from preprocessing import prepare_data

data = pd.read_csv('books.csv')

df = prepare_data(data)

mapping = {
    'Lev Tolstoy': 'Leo Tolstoy',
    'Winston S. Churchill': 'Winston Churchill',                            #MAPIRANJE 
    'Plato': 'Platon',
    'Will Shakespeare': 'William Shakespeare'
 
}
 
df['author'] = df['author'].replace(mapping)


unique_authors = df['author'].dropna().unique()                                 #PRIMER STANDARDIZACIJE 
 
cutoff_threshold = 0.9                                                          #PRVO STANDARDIZACIJA PA ONDA IDE MAPIRANJE
potential_duplicates = {}
 
for author in unique_authors:
 
    matches = difflib.get_close_matches(author, unique_authors, cutoff=cutoff_threshold)
 
    if len(matches) > 1:
        potential_duplicates[author] = sorted(matches)
 
for key, value in potential_duplicates.items():
    print(f"'{key}' : {value}")
"""

#ANALIZA SVEGA

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
 
df = prepare_data(data)
 
df = df[df['section'] != 'Rare Books']                                                    #POMOC MARKETINGU
 
df['borrowings_per_copy'] = df['times_borrowed'] / df['total_copies']
sorted_df = df.sort_values(by='borrowings_per_copy')
top_50 = sorted_df.head(50)
 
print(top_50[['title', 'times_borrowed', 'total_copies', 'borrowings_per_copy']])
"""




