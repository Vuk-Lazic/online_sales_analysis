"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
mean_val = df['rating'].mean()
median_val = df['rating'].median()                             #UPOREDJIVANJE PROSEKA, MEDIANE I MODA
mode_val = df['rating'].mode() 
 
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {", ".join(mode_val.astype(str))}")
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
mean_val = df['times_borrowed'].mean()
median_val = df['times_borrowed'].median()                                    #PRIMER UPOREDJIVANJE PROSEKA, MEDIANE I MODA
mode_val = df['times_borrowed'].mode()
 
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {", ".join(mode_val.astype(str))}")
"""

#OPSEG

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
mean_val = df['rating'].mean()
median_val = df['rating'].median()
mode_val = df['rating'].mode()                                         #PRIMER PROVERE OPSEGA 
max_val = df['rating'].max()
min_val = df['rating'].min()
 
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {", ".join(mode_val.astype(str))}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
mean_val = df['times_borrowed'].mean()
median_val = df['times_borrowed'].median()
mode_val = df['times_borrowed'].mode()                              #PRIMER PROVERE OPSEGA 
max_val = df['times_borrowed'].max()
min_val = df['times_borrowed'].min()
 
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {", ".join(mode_val.astype(str))}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")
"""

#KVANTILI

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
p01 = df['rating'].quantile(0.01)                                      #PRONALAZAK JEDNOG PROCENTA NAJLOSIJIH KNJIGA
 
bottom_1_percent_books = df[df['rating'] <= p01]
 
print(bottom_1_percent_books.filter(items=['title', 'rating']).sort_values(by=['rating'], ascending=False).to_string())
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
p95 = df['rating'].quantile(0.95)                                      #PRONALAZAK PET PROCENATA NAJBOLJE OCENJENIH KNJIGA
 
top_5_percent_books = df[df['rating'] >= p95]
 
print(top_5_percent_books.filter(items=['title', 'rating']).sort_values(by=['rating'], ascending=False).to_string())
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
p99 = df['page_count'].quantile(0.99)                                   #PRONALAZAK JEDNOG PROCENTA NAJDUZIH KNJIGA    
 
longest_1_percent = df[df['page_count'] >= p99]
 
print(longest_1_percent.filter(items=['title', 'page_count']).sort_values(by=['page_count'], ascending=False).to_string())
"""

#STANDARDNA DEVIJACIJA

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)                                                 #PRIKAZ STANDARDNE DEVIJACIJE
 
std_year = df['year_published'].std()
 
print(std_year)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)                                                #KOMBINOVANJE STANDARDNE DEVIJACIJE I PROSEKA
 
std_year = df['year_published'].std()
mean_year = df['year_published'].mean()
 
print(std_year)
print(mean_year)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv') 
df = prepare_data(data)                                                #PRIMER KOMBINOVANJE STANDARDNE DEVIJACIJE I PROSEKA
 
std_year = df['times_borrowed'].std()
mean_year = df['times_borrowed'].mean()
 
print(std_year)
print(mean_year)
"""

#INTERKVARTIOLNI RASPON

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv') 
df = prepare_data(data)                                           #DOBIJANJE INTERKVARTILNOG RASPONA

q1 = df['times_borrowed'].quantile(0.25)
q3 = df['times_borrowed'].quantile(0.75)
 
iqr = q3 - q1
print(iqr)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
sd = df['times_borrowed'].std()                                   #ODNOS STANDARDNE DEVIJACIJE I INTERKVARTILNOG RASPONA
q1 = df['times_borrowed'].quantile(0.25)
q3 = df['times_borrowed'].quantile(0.75)

iqr = q3 - q1
 
print(f"Standard deviation: {sd:.2f}")
print(f"IQR (Q3 - Q1): {iqr:.2f}")
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
sd = df['rating'].std()
q1 = df['rating'].quantile(0.25)                                  #PRIMER ODNOSA STANDARDNE DEVIJACIJE I INTERKVARTILNOG RASPONA
q3 = df['rating'].quantile(0.75) 
iqr = q3 - q1
 
print(f"Standard deviation: {sd:.2f}")
print(f"IQR (Q3 - Q1): {iqr:.2f}")
"""

#PROJEKAT

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
genre_stats = df.groupby('genre', observed=True).agg(                                #NAJUJEDNACENIJE IZDAVANJE KNJIGA
    times_borrowed_std=('times_borrowed', 'std'),
    titles_count=('title', 'count')
)
 
genre_stats_filtered = genre_stats[genre_stats['titles_count'] >= 20]
genre_sorted = genre_stats_filtered.sort_values(by=["times_borrowed_std"])
print(genre_sorted)
""" 

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
section_stats = df.groupby('section', observed=True).agg(                                #SEKCIJE KOJE BELEZE NAJUJEDNACENIJE REZULTATE IZDAVANJA
    times_borrowed_std=('times_borrowed', 'std'),
    titles_count=('title', 'count')
)
 
section_stats_filtered = section_stats[section_stats['titles_count'] >= 20]
section_sorted = section_stats_filtered.sort_values(by=["times_borrowed_std"])
print(section_sorted)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
Q1 = df['price'].quantile(0.25) 
Q3 = df['price'].quantile(0.75)                                                             #TIPICNI CENOVNI RANG KNJIGA
IQR = Q3 - Q1
 
iqr_books = df[(df['price'] >= Q1) & (df['price'] <= Q3)]
 
print(f"Price range of the middle 50% of books:")
print(f"{Q1:.2f} € - {Q3:.2f} € (IQR = {IQR:.2f} €)")
print(f"Total number of books: {len(iqr_books)}")
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
section_stats = df.groupby('section', observed=True).agg(                             #TIPICAN BROJ IZNAJMLJIVANJA KNJIGA U BIBLIOTECI
    times_borrowed_std=('times_borrowed', 'std'),
    titles_count=('title', 'count')
)
 
section_stats_filtered = section_stats[section_stats['titles_count'] >= 20]
section_sorted = section_stats_filtered.sort_values(by=["times_borrowed_std"])
print(section_sorted)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
Q1 = df['page_count'].quantile(0.25)
Q2 = df['page_count'].quantile(0.50)
Q3 = df['page_count'].quantile(0.75)
 
def assign_quartile(pages): 
    if pages <= Q1:
        return '1st quartile'                                          #BROJ IZNAJMLJIOVANJA KNJIGA U ZAVISNOSTI OD BROJA STRANICA
    elif pages <= Q2:
        return '2nd quartile'
    elif pages <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'
 
df['page_quartile'] = df['page_count'].apply(assign_quartile)
 
total_borrowed_per_quartile = df.groupby('page_quartile')['times_borrowed'].sum().reset_index()
 
print(total_borrowed_per_quartile)
"""

"""
import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
Q1 = df['page_count'].quantile(0.25)
Q2 = df['page_count'].quantile(0.50)
Q3 = df['page_count'].quantile(0.75)
 
def assign_quartile(pages):                                            #OCENA KNJIGE U ZAVISNOSTI OD BROJA STRANICA
    if pages <= Q1:
        return '1st quartile'
    elif pages <= Q2:
        return '2nd quartile'
    elif pages <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'
 
df['page_quartile'] = df['page_count'].apply(assign_quartile)
 
rating_per_quartile = df.groupby('page_quartile')['rating'].mean().reset_index()
 
print(rating_per_quartile)
"""























