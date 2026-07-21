#PRIKAZIVANJE OSNOVNIH INFORMACIJA O DATASETU

"""
import pandas as pd
df = pd.read_csv('ecommerce_orders_april.csv')
rows, columns = df.shape                                                     #ODREDJIVANJE BROJA REDOVA I KOLONA U DATASETU
print(f"Dataset contains {rows} rows and {columns} columns.")
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
column_names = df.columns.tolist()                                          #PRIKAZIVANJE IMENA SVIH KOLONA U DATASETU
print(column_names)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]           #PROMENA IMENA KOLONA U DATASETU  
df.to_csv('books.csv', index=False, encoding="utf-8-sig") #ZADRZVANJE SVIH SPECIFIČNIH KARAKTERA U IMENIMA KOLONA(encoding)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')                                            #PRIKAZIVANJE PRVIH N REDOVA DATASETA
print(df.head(20))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')                                            #PRIKAZIVANJE POSLEDNJIH N REDOVA DATASETA
print(df.tail())
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
print("First 40:")
print(df.head(40))                                                       #PRIMER PRIKAZIVANJA ODREDJENOG BROJA REDOVA
print("Last 30:")                                                    
print(df.tail(30))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
print(df.sample(n=5, random_state=42, replace=False))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')                                            #PRIKKAZIVANJE UZ POMOC ILOC METODE
print(df.iloc[0])
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')                                            #PRIKKAZIVANJE UZ POMOC LOC METODE
print(df.loc[0, "title"])
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')                                            #PRIKKAZIVANJE UZ POMOC AT METODE
print(df.at[0, "title"]) 
"""

#FORMATIRANJE PRIKAZA ODREDJENIH KOLONA U DATASETU

"""
import pandas as pd
df = pd.read_csv('books.csv')
print(df.head(30).to_string(columns=['title','page_count'], float_format="{:.0f}".format))           #PRIKAZIVANJE ODREDJENIH KOLONA I ULEPSAVANJE PRIKAZA
"""      

"""
import pandas as pd
df = pd.read_csv('books.csv')
print(df.sample(n=30, replace=False).to_string(columns=['title', 'price', 'rating'], float_format="{:.0f}".format))        #PRIMER PRIKAZIVANJA ODREDJENIH KOLONA
"""

#SORTIRANJE PODATAKA U DATASETU

"""
import pandas as pd
df = pd.read_csv('books.csv')
df.sort_values(by="title", inplace=True)                           #SORTIRANJE PODATAKA PO JEDNOJ KOLONI
print(df.head(30).to_string(columns=['title', 'author']))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
sorted_df = df.sort_values(by="year_published")                                               #SORTIRANJE PRIMER PO DATUMU OBJAVLJIVANJA
print(sorted_df.head(20).to_string(columns=['title', 'author', 'year_published']))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df.sort_values(by="title", inplace=True)                                               #SORTIRANJE PODATAKA SORT + ILOC
print(df.iloc[0]) #Nakon sortiranja iloc uzima novu sortiranu listu i po njoj dalje radi, ne po originalnoj. Zato se dobija novi rezultat.
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df.sort_values(by="title", inplace=True)                                               #SORTIRANJE PODATAKA SORT + LOC   
print(df.loc[0]) #Za razliku od iloc, loc i dalje uzima originalnu listu i po njoj radi, ne po sortiranoj. Zato se dobija isti rezultat kao pre sortiranja.
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df.sort_values(by="title", inplace=True)                                               #SORTIRANJE PODATAKA SORT + LOC
df.reset_index(drop=True, inplace=True) #Ali ako se resetuje index nakon sortiranja, onda loc uzima novu sortiranu listu i po njoj dalje radi, ne po originalnoj.
print(df.loc[0])                        # Zato se dobija novi rezultat.
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
sorted_df = df.sort_values(by="times_borrowed", ascending=False)                        #SORTIRANJE OD NAJVECEG KA NAJMANJEM
print(sorted_df.head(20).to_string(columns=['title','author', 'times_borrowed']))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df.sort_values(by="times_borrowed",inplace=True, ascending=False)                        #SORTIRANJE OD NAJVECEG KA NAJMANJEM
print(df.head(20).to_string(columns=['title','author', 'times_borrowed']))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
pages_max = df.sort_values(by="page_count", ascending=False).iloc[0]['page_count']       #PRIMER SORTIRANJA UZ POMOC ILOC-A
pages_min = df.sort_values(by="page_count").iloc[0]['page_count'] 
print(pages_max)
print(pages_min)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df.sort_values(by=["author"], inplace=True, ascending=False)                            #SORTIRANJE PO VISE KOLONA
print(df.head(40).to_string(columns=['title', 'author']))                              
"""

"""
import pandas as pd
 
df = pd.read_csv('books.csv') 
 
df.sort_values(by=["author", "title"], inplace=True, ascending=[False, True])            #SORTIRANJE PO VISE KOLONA, PRVO PO AUTORU OD NAJVECEG KA NAJMANJEM, A ONDA UNUTAR TOGA PO NASLOVU OD NAJMANJEG KA NAJVEĆEM
 
print(df.head(40).to_string(columns=['title', 'author']))
"""

#FILTRIRANJE PODATAKA U DATASETU

"""
import pandas as pd
df = pd.read_csv('books.csv')
filtered_df = df.filter(items=['title', 'author'])                                  #PRIKAZIVANJE ODREDJENIH KOLONA U DATASETU POMOCU FILTER METODE
print(filtered_df.head(50))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
filtered_df = df.filter(items=['catalog_position', 'title', 'year_published'])      #PRIMER FILTRIRANJA
print(filtered_df.tail(30))
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
filtered_df = df.filter(items=[0, 1, 2, 3], axis=0)                                #PRIMER FILTRIRANJA PO REDOVIMA
print(filtered_df)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df = df.set_index('catalog_position')                                             #fILTRIRANJE PO VREDNOSTIMA NEKE KOLONE
filtered_df = df.filter(like="A1-B1", axis=0)
print(filtered_df)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df = df.set_index('catalog_position')
filtered_df = df.filter(like="A1-B1", axis=0).filter(items=['title', 'author'])      #NADOVEZIVANJA FILTER METODE
print(filtered_df.to_string())
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
df = df.set_index('catalog_position')                                                #PRIMER NADOVEZIVANJA FILTER METODE
filtered_df = df.filter(like="A2", axis=0).filter(items=['title', 'page_count'])
print(filtered_df)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
filtered_books = df[df['author'] == 'Mark Twain']                                  #FILTRIRANJE PODATAKA POMOCU USLOVA
print(filtered_books)
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
filtered_books = df[df['genre'] == 'Horror']                                       #PRIMER FILTRIRANJE PODATAKA POMOCU USLOVA
print(f"Total number of \"Horror\" books: {filtered_books.shape[0]}")
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
mask = (df['genre'] == 'Drama') & (df['times_borrowed'] < 5)                       #FILTRIRANJE PODATAKA POMOCU VISE USLOVA
filtered_books = df[mask]
print(filtered_books.filter(items=['title', 'author', 'times_borrowed']).sort_values(by='times_borrowed').head(30))       
"""

"""
import pandas as pd
df = pd.read_csv('books.csv')
mask = (df['genre'] == 'Science') 
science_books_sorted = df[mask].sort_values(by='times_borrowed', ascending=False)              #PRIMER FILTRIRANJA PODATAKA POMOCU VISE USLOVA I SORTIRANJA
print(science_books_sorted.filter(items=['title', 'author', 'times_borrowed']).iloc[0]) 
"""