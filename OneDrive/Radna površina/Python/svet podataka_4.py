#XML

"""
<?xml version="1.0" encoding="utf-8"?>

<recipe>
    <title>Grilled Cheese Sandwich</title>
    <ingredients>
        <ingredient qty="2">bread slice</ingredient>                               #POCETNI PRIMER
        <ingredient>cheese slice</ingredient>
        <ingredient qty="2">margarine pat</ingredient>
        <!-- additional ingredient (as desired) -->
    </ingredients>
</recipe>
"""

"""
<company>
    <employee id = "101">
        <name>John Doe</name>
        <position>Software Engineer</position>
        <department>IT</department>
        <hire_date>2018-05-22</hire_date>
        <salary currency = "USD">75000</salary>
    </employee>
    <employee id = "102">
        <name>Jane Smith</name>
        <position>Project Manager</position>                                      #PRIMER PREDSTAVLJANJA PODATAKA 
        <department>Operations</department>
        <hire_date>2015-03-10</hire_date>
        <salary currency = "USD">90000</salary>
    </employee>
    <employee id = "103">
        <name>Emily Johnson</name>
        <position>Data Analyst</position>
        <department>Marketing</department>
        <hire_date>2020-07-15</hire_date>
        <salary currency = "USD">60000</salary>
    </employee>
</company>
"""

"""
<export>
  <user id="1">
    <name>John Doe</name>
    <email>john@example.com</email>
  </user>
  <user id="2">                                                                    #PRIMER SLANJA PODATAKA U XML FORMATU
    <name>Jane Smith</name>
    <email>jane@example.com</email>
  </user>
</export>
"""

"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
    <sheets>
        <sheet name="Sheet1" sheetId="1" r:id="rId1" />                           #PRIMER PREDSTAVLJANJA PODATAKA U XML FORMATU (EXCEL)- 
        <sheet name="Sheet2" sheetId="2" r:id="rId2" />                           #- PRIKAZ STRUKTURE EXCEL DOKUMENTA U XML FORMATU
    </sheets>
</workbook>
"""

"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
    <sheetData>
        <row r="1">
            <c r="A1" t="s">
                <v>0</v>
            </c>
            <c r="B1" t="s">
                <v>1</v>                                                         #PODACI U POJEDINACNIM EXCEL CELIJAMA PREDSTAVLJENI U XML FORMATU
            </c>
        </row>
        <row r="2">
            <c r="A2">
                <v>10</v>
            </c>
            <c r="B2">
                <v>20</v>
            </c>
        </row>
    </sheetData>
</worksheet>
"""

"""
<configuration>
  <database>
    <name>MyDatabase</name>
    <user>admin</user>
    <password>password123</password>                                             #KONFIGURACIIONI FAJL JEDNE BAZE PODATAKA
  </database>  
  <server>
    <port>8080</port>
    <host>localhost</host>
  </server>
</configuration>
"""

"""
<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
 
  <rect x="10" y="10" width="50" height="50" fill="blue" />                      #PRIMER PREDSTAVLJANJA VEKTORSKE GRAFIKE U XML FORMATU (SVG)
  <circle cx="100" cy="50" r="30" fill="red" /> 
  <line x1="0" y1="100" x2="200" y2="100" stroke="green" stroke-width="2" />
  <text x="10" y="180" font-family="Arial" font-size="20" fill="black">
    SVG document
  </text>
 
</svg>
"""

"""
<COLLADA>
    <library_geometries>
        <geometry id="cube">
            <mesh> <!-- Opis 3D objekta -->                                      #PRIMER PREDSTAVLJANJA 3D MODELA U XML FORMATU (COLLADA) NASTAVAK .DAE
            </mesh>
        </geometry>
    </library_geometries>
</COLLADA>
"""

"""
import pandas as pd

df = pd.read_csv('books.csv')
df.to_xml('books.xml', parser='etree', root_name='library', row_name='book', index=False,  attr_cols=['id'], elem_cols=['title','author','published','genre'])
#PRETVARANJE CSV FAJLA U XML FORMAT KORIŠĆENJEM PANDAS BIBLIOTEKE U PYTHONU
"""

#WEB SERVISI I PODACI U XML I JSON FORMATU

"""
import requests 

response = requests.get('https://openlibrary.org/search?q=1984&mode=everything')           #CITANJE PODATAKA SA WEB SERVISA KOJI VRAĆA PODATKE U XML FORMATU
"""

"""
import requests
 
# define input data
title = 'To Kill a Mockingbird'
author = 'Harper Lee'
 
# create search URL
url = f'https://openlibrary.org/search.json?title={title}&author={author}'                 #CITANJE PODATAKA SA WEB SERVISA KOJI VRAĆA PODATKE U JSON FORMATU 
 
# send request and get response data
response = requests.get(url)
data = response.text
 
print(data)
"""

"""
{
    "students": [
        {
            "first_name": "Chad",
            "last_name": "Farley",
            "sid": "11/22"
        },
        {
            "first_name": "Dominic",                                  #PRIMER PREDSTAVLJANJA PODATAKA U JSON FORMATU  
            "last_name": "Bonilla",
            "sid": "24/22"
        },
        {
            "first_name": "Mario",
            "last_name": "Donovan",
            "sid": "15/21"
        }
    ]
}
"""

"""
{
    "company": [
        {
            "id": "101",
            "name": "John Doe",
            "position": "Software Engineer",
            "department": "IT",
            "hire_date": "2018-05-22",
            "salary": {
                "amount": "75000",
                "currency": "USD"
            }
        },
        {
            "id": "102",
            "name": "Jane Smith",
            "position": "Project Manager",
            "department": "Operations",                                  #PRIMER PREDSTAVLJANJA PODATAKA O ZAPOSLENIMA U JSON FORMATU
            "hire_date": "2015-03-10",
            "salary": {
                "amount": "90000",
                "currency": "USD"
            }
        },
        {
            "id": "103",
            "name": "Emily Johnson",
            "position": "Data Analyst",
            "department": "Marketing",
            "hire_date": "2020-07-15",
            "salary": {
                "amount": "60000",
                "currency": "USD"
            }
        }
    ]
}
"""

"""
import json

data = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published": 1960,                                                 #PRIMER PRETVARANJA PODATAKA IZ PYTHONA U JSON FORMAT
    "genre": "Fiction"
}

json_string = json.dumps(data)

print(json_string)
"""

"""
import json

json_string = '{"title": "To Kill a Mockingbird", "author": "Harper Lee", "published": 1960, "genre": "Fiction"}'                   #VRACANJE PODATAKA IZ JSON FORMAT U PYTHON 
 
data = json.loads(json_string)
 
print(data["title"])
print(data["author"])
print(data["published"])
print(data["genre"])
"""

#WEB SERVISI I PODACI U XML I JSON FORMATU PROBLEMI

"""
import requests

title = 'To Kill a Mockingbird'
author = 'Harper Lee'

url = f'https://openlibrary2.org/find.json?title={title}&author={author}'

try:

    # send request and get response data
    response = requests.get(url)
    data = response.json()  # parse JSON response into a Python dictionary

    if "error" in data:
        print(data["error"])                    #NEODGOVARAJUCI OBLIK URL ADRESE
        
    else:
        if (data["num_found"] > 0):
            first_book = data["docs"][0]  # PROVERAVA DA LI KNJIGA POSTOJI ILI NE

            if "first_sentence" in first_book:
                print(first_book["first_sentence"])
                
            if "subject" in first_book:
                print(first_book["subject"])                              #PRONADJENA KNJIGA ALI PODACI NE POSTOJE U ODGOVARAJUĆEM FORMATU
                
            if "place" in first_book:  
                print(first_book["place"])  
                
            if "time" in first_book:
                print(first_book["time"])
                

        else:
            print("No books found matching the search criteria.")

except requests.exceptions.ConnectionError:
    print("Error: The server is unavailable or the URL is invalid.")
except requests.exceptions.Timeout:
    print("Error: The request has timed out.")                                 #NEMOGUCNOST KONTAKTIRANJA SA SERVEROM
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Unexpected error:: {e}")
"""

#UNAPREDJEN KOD

"""
import requests

title = 'Chaos: Making a New Science'
author = 'James Gleick'

url = f'https://openlibrary.org/search.json'                       #UNAPREDJIVANJE KODA
params = {"q": title, "author": author}

try:

    # send request and get response data                           
    response = requests.get(url=url, params=params)
    print(response.url)                           # print the URL being accessed for debugging purposes
    data = response.json()                       # parse JSON response into a Python dictionary

    if "error" in data:
        print(data["error"])                                        #NEODGOVARAJUCI OBLIK URL ADRESE
        
    else:
        if (data["num_found"] > 0):
            first_book = data["docs"][0]                            # PROVERAVA DA LI KNJIGA POSTOJI ILI NE
            print("knjiga je pronadjena")
            if "first_sentence" in first_book:
                print(first_book["first_sentence"])
                
            if "subject" in first_book:
                print(first_book["subject"])                              #PRONADJENA KNJIGA ALI PODACI NE POSTOJE U ODGOVARAJUĆEM FORMATU
                
            if "place" in first_book:  
                print(first_book["place"])  
                
            if "time" in first_book:
                print(first_book["time"])
                

        else:
            print("No books found matching the search criteria.")

except requests.exceptions.ConnectionError:
    print("Error: The server is unavailable or the URL is invalid.")
except requests.exceptions.Timeout:
    print("Error: The request has timed out.")                                 #NEMOGUCNOST KONTAKTIRANJA SA SERVEROM
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Unexpected error:: {e}")
"""

#FINANLNI PRIMER KODA    #PRETVARANJE LISTA U STRINGOVE POMOCU SERVISA I DODAVANJE PODATAKA U DATAFRAME

"""
# get missing data function
import pandas as pd
import time
import requests

def get_missing_data(title, author):
 
    print(f'[INFO] Searching for: {title} - {author}')
 
    url = "https://openlibrary.org/search.json"
    params = {"q": title, "author": author}
 
    try:
 
        response = requests.get(url=url, params=params)
        data = response.json()
 
        if "error" in data:
            print(data['error'])
 
        elif (data["num_found"] > 0):
            first_book = data["docs"][0]
 
            first_sentence = ''
            subject = ''
            place = ''
            time = ''
 
            if "first_sentence" in first_book:
                first_sentence = first_book["first_sentence"]
 
            if "subject" in first_book:
                subject = first_book["subject"]
 
            if "place" in first_book:
                place = first_book["place"]
 
            if "time" in first_book:
                time = first_book["time"]
 
            print(f'[INFO] Found data for: {title} - {author}')
 
            return {
                "first_sentence": first_sentence,
                "subject": subject,
                "place": place,
                "time": time
            }
 
        else:
            print('Book not found')
 
    except requests.exceptions.ConnectionError:
        print("Error: The server is unavailable or the URL is invalid.")
    except requests.exceptions.Timeout:
        print("Error: The request has timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Unexpected error:: {e}")
        
# extract data from CSV
df = pd.read_csv('books.csv')
 
df['first_sentence'] = ''
df['subject'] = ''
df['place'] = ''
df['time'] = ''
 
for index, row in df.iterrows():
    # extract and transform data from web service
    missing_data = get_missing_data(row['title'], row['author'])
 
    if missing_data["first_sentence"] is not None:
        df.at[index, 'first_sentence'] = ', '.join(missing_data["first_sentence"])
 
    if missing_data["subject"] is not None:
        df.at[index, 'subject'] =  ', '.join(missing_data["subject"]) 
     
    if missing_data["place"] is not None:
        df.at[index, 'place'] = ', '.join(missing_data["place"])
 
    if missing_data["time"] is not None:
        df.at[index, 'time'] =  ', '.join(missing_data["time"])
 
    # add some sleep to stay under the service limit
    time.sleep(3)
 
    # load data
    df.to_xml('books.xml', parser='etree', root_name='library', row_name='book', index=False,  attr_cols=['id'], elem_cols=['title','author', 'published', 'genre', 'first_sentence', 'subject', 'place', 'time'])
"""
