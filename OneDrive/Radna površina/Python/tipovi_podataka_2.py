"""
import pandas as pd
df = pd.read_csv('books.csv')                             #PROVERA KOJI TYPE JE PODATAKA U SVAKOJ KOLONI "DTYPES"
print(df.dtypes)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')                              #PROVERA KOJI TYPE JE PODATAKA U SVAKOJ KOLONI "INFO"
print(df.info())
"""

#KONVERTOVANJE PODATAKA

"""
import pandas as pd
df = pd.read_csv('books.csv')

df['times_borrowed'] = df['times_borrowed'].astype('Int32')            #KONVERTOVANJE IZ FLOAT U INT
print(df.dtypes)
"""

"""
import pandas as pd
data = {
    'id': [1, 2, 3, 4], 
    'value': ['10', '20', '30', '40']                                  #KONVERTOVANJE IZ STR U INT
}
df = pd.DataFrame(data)
df['value'] = df['value'].astype(int)
print(df.dtypes)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')

df['page_count'] = df['page_count'].astype('Int32')                    #PRIMER KONVERTOVANJA IZ FLOAT U INT
print(df.dtypes)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df['total_copies'] = pd.to_numeric(df['total_copies'], errors='coerce')
mask = (df['genre'] == 'Science') & (df['total_copies'] < 4)                #PRIMER KONVERTOVANJA IZ STR U NUMERIC I FILTRIRANJE PODATAKA NA OSNOVU TE KONVERZIJE
filtered_books = df[mask]
print(filtered_books.filter(items=['title', 'total_copies']))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df['year_published'] = pd.to_numeric(df['year_published'], errors='coerce')
df['year_published'] = df['year_published'].astype('Int32')                          #PRIMER
mask = (df['year_published'] > 1960) & (df['year_published'] < 1970)                 #DODATI MOYDA DA SE GODINE POREDJAJU PO OPADUJCEM REDOSLEDU
filtered_books = df[mask]
print(filtered_books.filter(items=['catalog_number', 'title', 'author', 'year_published']))
"""

#DATUM I VREME

"""
import pandas as pd
df = pd.read_csv('books.csv')
df['last_borrowed_date'] = pd.to_datetime(df['last_borrowed_date'], format='%d_%b_%y', errors='coerce')        #KONVERTOVANJE STR U DATETIME, DODATI MOYDA DA SE SORTIRA PO DATUMU POSLEDNJEG POSUDJIVANJA
df.sort_values(by=["last_borrowed_date"], inplace=True)
print(df.filter(items=['title','author', 'last_borrowed_date']).head(30))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df['last_borrowed_date'] = pd.to_datetime(df['last_borrowed_date'], format='%d_%b_%y', errors='coerce')
data = {
    'years': df['last_borrowed_date'].dt.year,
    'months': df['last_borrowed_date'].dt.month,               #ISPIAIVANJE GODINA, MESECI I DANI IZ DATUMA POSLEDNJEG POSUDJIVANJA
    'days': df['last_borrowed_date'].dt.day
}
new_df = pd.DataFrame(data=data, dtype='Int32')
print(new_df)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df['last_borrowed_date'] = pd.to_datetime(df['last_borrowed_date'], format='%d_%b_%y', errors='coerce') 
filtered_df = df[(df['last_borrowed_date'].dt.year == 2024) & (df['last_borrowed_date'].dt.month == 12)]      #FILTRIRANJE PODATAKA NA OSNOVU GODINE I MESECA POSLEDNJEG POSUDJIVANJA
print(filtered_df.filter(items=['title', 'author', 'last_borrowed_date']))
"""

#KATEGORIJSKI PODACI

"""
import pandas as pd
df = pd.read_csv('books.csv')                    #PROVERA KOLIKO RAZLICITIH VREDNOSTI IMA U SVAKOJ KOLONI
print(df.nunique())
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')                    #DUBLJA PROVERA KOLIKO RAZLICITIH VREDNOSTI IMA U SVAKOJ KOLONI
print(df['section'].value_counts())
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
print(df.memory_usage(deep=True))
df['genre'] = df['genre'].astype('category')                 #KONVERTOVANJE STR U CATEGORY
df['section'] = df['section'].astype('category')      
df['language'] = df['language'].astype('category')
print(df.memory_usage(deep=True))
"""

"""
import pandas as pd
df = pd.read_csv('online_orders.csv')
initial_state = df.memory_usage(deep=True)
df['product_category'] = df['product_category'].astype('category')
df['order_status'] = df['order_status'].astype('category')
df['payment_method'] = df['payment_method'].astype('category')                                      #PRIMER KONVERTOVANJA STR U CATEGORY NA DRUGOM DATASETU I PROVERA KOLIKO SE MEMORIJE UŠTEDILO TIME
final_state = df.memory_usage(deep=True)
memory_comparation = pd.DataFrame(data={"before": initial_state, "after": final_state, "gain": (
    initial_state - final_state)/initial_state*100, "types": df.dtypes})
print(memory_comparation)
"""

#ETL

##koristiti funkcije iz preprocessing.py

"""
import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')                                        #PPRIMER KORISCENJA ETL PROCESA
df = prepare_data(data)
print(df)
"""

#PARSIRANJE I ESTRAHOVANJE PODATAKA

"""
import pandas as pd
df = pd.read_csv('books.csv')
print(df['rating'].unique())
print(df['rating'].value_counts())                                          #ISPISIVANJE RAZLICITIH VREDNOSTI U KOLONI "RATING" I NJIHOVOG BROJA POJAVLJIVANJA
values = df[~df['rating'].str.contains('5 stars', case=False, na=False)]
print(values['rating'].unique())
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
print(df['ratings_count'].unique())
print(df['ratings_count'].value_counts())                                           #ISTO KO I OVO GORE
values = df[~df['ratings_count'].str.contains('rating', case=False, na=False)]
print(values['ratings_count'].unique())
"""

"""
import pandas as pd
import numpy as np
df = pd.read_csv('books.csv')
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no rating available":
        return np.nan
     
    parts = str(text).split()                                                   #ESKTRAHOVANJE NUMERICKIH VREDNOSTI
     
    try:
        return float(parts[0])     
    except (ValueError, IndexError):
        return np.nan
df['rating'] = df['rating'].apply(parse_rating)
print(df.filter(items=['title', 'author', 'rating']).head(30))
"""

"""
import pandas as pd
import numpy as np
df = pd.read_csv('books.csv')
def parse_ratings_count(text):
    if pd.isna(text) or str(text).strip().lower() == "no reviews":
        return np.nan
    parts = str(text).replace(',', '').split()                                      #ISTO SAMO ZA DRUGACIJU KOLONU
    try:
        return int(parts[0])
    except (ValueError, IndexError):
        return np.nan
df['ratings_count'] = df['ratings_count'].apply(parse_ratings_count)
print(df.filter(items=['title', 'ratings_count']).head(30))
"""

"""
import pandas as pd
import numpy as np
df = pd.read_csv('books.csv')
def parse_price(text):
    if pd.isna(text) or str(text).strip().lower() == "price not available":
        return np.nan 
    try:
        price_str = str(text).replace('$', '').strip()                                  #ISTO SVE SAMO DRUGACIJA KOLONA
        return float(price_str)
    except ValueError:
        return np.nan
df['price'] = df['price'].apply(parse_price)
print(df.filter(items=['title', 'price']).head(30))
"""
category
"""
import pandas as pd
import numpy as np
from preprocessing import prepare_data

data = pd.read_csv('books.csv')                                        #PRIMER KORISCENJA ETL PROCESA SA PARSIRANJEM I ESTRAHOVANJEM PODATAKA
df = prepare_data(data)

print(df.dtypes)
"""

#INZENJERING KARAKTERISTIKE

"""
import pandas as pd

df = pd.read_csv('books.csv')

df[['dimensions_width', 'dimensions_thickness', 'dimensions_height']] = df['dimensions'].str.replace(
    "inches", "").str.replace(" ", "").str.split('x', expand=True).astype(float)

df.drop('dimensions', axis=1, inplace=True)                                                   #PRIMER INZENJERINGA KARAKTERISTIKE

print(df.head(30))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df[['catalog_shelf', 'catalog_row', 'catalog_row_number']] = df['catalog_position'].str.split('-', expand=True)         #PRIMER INZENJERINGA KARAKTERISTIKE SAMO DRUGA KOLONA
print(df.filter(items=['title', 'catalog_shelf', 'catalog_row', 'catalog_row_number']).head(30))
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
sorted_books = df.sort_values(by='times_borrowed', ascending=False)
 
shelf_width = 118
selected_books = []
current_width = 0.0                                                         #PRIMER INZENJERINGA KARAKTERISTIKE - NAPREDNIJI PRIMER
 
for idx, row in sorted_books.iterrows():
    thickness = row['dimensions_thickness']
    if current_width + thickness <= shelf_width:
        selected_books.append(row)
        current_width += thickness
    if current_width >= shelf_width:
        break
 
selected_df = pd.DataFrame(selected_books).reset_index()
 
print("Width used:", current_width, "inches")
print(selected_df[['title', 'author', 'times_borrowed', 'dimensions_thickness']].to_string())
"""