#EXCEL

"""
import pandas as pd
 
df = pd.read_excel('users_rentals.xlsx')                                          #ISPISIVANJE PODATAKA IZ EXCEL TABELE
print(df)            #KADA DODAMO TO_STRING(ILI KAKO DA SE PISE) ISPISUJE CELU TABELU U TERMINALU
"""

"""
import pandas as pd
 
users = pd.read_excel("users_rentals.xlsx")
 
tenth_user_data = users.iloc[9]
print(tenth_user_data)
  
user_56_last_name = users.loc[55, "lastname"]                                     #PRIMER ISPISIVANJA VREDNOSTI IZ TABELE  
print(user_56_last_name) 
 
user_1_phone = users.loc[0, "phone"]
print(user_1_phone)
 
all_phones = users["phone"]
print(all_phones)
"""

"""
import pandas as pd
from pandas import DataFrame
 
books = [
    [101, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"],
    [102, "1984", "George Orwell", 1949, "Dystopian"],
    [103, "Moby Dick", "Herman Melville", 1851, "Adventure"],
    [104, "War and Peace", "Leo Tolstoy", 1869, "Historical"],
    [105, "The Catcher in the Rye", "J.D. Salinger", 1951, "Coming-of-Age"]                               #KREIRANJE EXCEL FAJLA
]
 
df = DataFrame(data=books, columns=["id", "title", "author", "published", "genre"])
 
df.to_excel("my_excel_data.xlsx", index = False)
"""

"""
import pandas as pd
 
songs = pd.read_csv("songs.csv")                                                   #KONVERTOVANJE CSV FAJLA U EXCEL FAJL
songs.to_excel("songs.xlsx")
"""

"""
import pandas as pd

df = pd.read_excel('users_rentals.xlsx')                                           #PROVERA VREDNOSTI 

print(df.dtypes)
"""

"""
import pandas as pd
 
df = pd.read_excel('users_rentals.xlsx')                                           #AKO NAKON PROVERE NEMAMO NI JEDNU GRESKU PRETVARAMO OVAKO U DRUGI TIP VREDNOSTI
 
df["total_rentals"] = df['total_rentals'].astype('float')
print(df.dtypes)
"""

"""
import pandas as pd

df = pd.read_excel('users_rentals.xlsx')

df['total_rentals'] = pd.to_numeric(df['total_rentals'], errors='coerce')             #ISPRAVLJANJE GRESKE I ISPISIVANJE SUME

print(df['total_rentals'].sum())
"""

"""
import pandas as pd
 
df = pd.read_excel('users_rentals.xlsx')                                              #PRIMER KONVERTOVANJA
 
df["id"] = df['id'].astype('int16')
 
print(df.dtypes)
"""

"""
import pandas as pd
 
df = pd.read_excel('users_rentals.xlsx')                                              #IZOLACIJA JEDNE KOMPONENTE DATUMA
 
month = df.loc[1, 'rental_date'].month
print(month)
"""

"""
import pandas as pd
 
df = pd.read_excel('users_rentals.xlsx')
 
today = pd.Timestamp.today()                                                         #PRIMER MANIPULACIJE VREMENOM
interval = today - df.loc[1, 'rental_date']                                          #RACUNANJE DA LI JE ISTEKAO ROK ILI NE 
 
print(interval > pd.Timedelta(days = 31))
"""

"""
import pandas as pd
 
df = pd.read_excel('users_rentals.xlsx')
rows = []
 
today = pd.Timestamp.today()                                                         #ITERACIJA KROZ CELU LISTU

for index, row in df.iterrows():                                                     #PROVERA DATUMA
    interval = today - row['rental_date']
    if(interval > pd.Timedelta(days=31)):
        rows.append(row)
 
new_df = pd.DataFrame(data=rows, columns=df.columns)
print(new_df)
"""

"""
import pandas as pd
 
#extract data
df = pd.read_excel('users_rentals.xlsx')                                              #MASKIRANJE
 
#filter data
mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]
 
print(new_df)
"""

"""
import pandas as pd
 
#extract data
df = pd.read_excel('users_rentals.xlsx')
 
#filter data                                                                           #MASKIRANJE PRIMER
mask = (df['active'] == 'Y') & (df['gender'] == 'female')
new_df = df[mask]
 
print(new_df.to_string())
"""

"""
import pandas as pd
 
#extract data
df = pd.read_excel('users_rentals.xlsx')
 
#filter data
mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)              
new_df = df[mask].copy()
 
#sort data
new_df2 = new_df.sort_values(by='rental_date', ascending=True)                         #SORTIRANJE PODATAKA
 
print(new_df2)
"""

#DODAVANJE

"""
import pandas as pd
 
#extract data
df = pd.read_excel('users_rentals.xlsx')
 
#filter data
mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]
 
#sort data
new_df2 = new_df.sort_values(by='rental_date', ascending=True)
 
#add new column
new_df2["overdue_days"] = (pd.Timestamp.today() - new_df2['rental_date']).dt.days - 31                                #DODAVANJE NOVE KOLONE
 
print(new_df2)
"""

"""
import pandas as pd
 
data = pd.Series([10, 20, 30, 40, 50], name="values")                                                #ARITMETICKE FUNKCIJE POMOCU PANDASA
 
result = data * 2
print(result)
"""

"""
import pandas as pd
 
data_a = pd.Series([10, 20, 30, 40, 50], name="values")                                             #PRIMER
data_b = pd.Series([5, 4, 3, 2, 1], name="values")                                                  #VRSE SE OPERACIJE PODATAKA KOJE SE NALAZE NA ISTIM POZICIJAMA
 
result = data_a * data_b
print(result)
"""

#UKLANJANJE

"""
import pandas as pd
 
#extract data
df = pd.read_excel('users_rentals.xlsx')
 
#filter data
mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]
 
#sort data
new_df2 = new_df.sort_values(by='rental_date', ascending=True)
 
#add new column
new_df2["overdue_days"] = (pd.Timestamp.today() - new_df2['rental_date']).dt.days - 31
 
#remove columns
new_df2.drop(['address', 'gender', 'city', 'active'], axis=1, inplace=True)                            #PRIMER UKLANJANJA
print(new_df2)
"""

#PRAVLJENJE NOVOG FAJLA

"""
import pandas as pd
 
#extract data
df = pd.read_excel('users_rentals.xlsx')
 
#filter data
mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]
 
#sort data
new_df2 = new_df.sort_values(by='rental_date', ascending=True)
 
#add new column
new_df2["overdue_days"] = (pd.Timestamp.today() - new_df2['rental_date']).dt.days - 31
 
#remove columns
new_df2.drop(['address', 'gender', 'city', 'active'], axis=1, inplace=True)
 
#load data
new_df2.to_excel("overdue_users.xlsx", index=False)                                           #PRAVLJENJE NOVOG FAJLA NAKON IZVRSENIH IZMENA
"""

#PREPRAVLJANJE KODA ODOZGOR

"""
import pandas as pd
 
# extract data
def extract_user_data(file_name):
    return pd.read_excel(file_name)
 
# filter data
def filter_users(data):
    mask = (pd.Timestamp.today() - data['rental_date']) > pd.Timedelta(days=31)
    return data[mask]
 
# sort data
def sort_data(data):
    return data.sort_values(by='rental_date', ascending=True)
 
# add new column
def add_new_column(data):
    data["overdue_days"] = (pd.Timestamp.today() - data['rental_date']).dt.days - 31
    return data
 
# remove columns
def remove_columns(data):
    data = data.drop(['address', 'gender', 'city', 'active'], axis=1)
    return data
 
# load data
def load_data(data):
    data.to_excel("overdue_users_2.xlsx", index=False)

df = extract_user_data('users_rentals.xlsx').pipe(filter_users).pipe(sort_data).pipe(add_new_column).pipe(remove_columns)

load_data(df)
"""


