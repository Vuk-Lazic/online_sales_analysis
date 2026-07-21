#def __str__(self):
    #return f'i onda pisem sta sve treba dodati i kojim redom'

"""
text_file = open("output.txt", "w")
text_file.write("To Kill a Mockingbird")                       #Kreiranje jednog teskstualnog fajla
text_file.close()
"""

"""
text_file = open("output.txt", "a")
text_file.write("Moby Dick\n")                                 #Dodavanje podataka u fajl
text_file.close()
"""

"""
text_file = open("output.txt", "r")
text_file_content = text_file.read()
text_file.close()                                              #Citanje podataka iz fajla
 
print(text_file_content)
"""

"""
from Book import Book                                         #Prvo treba poseban fajl sa zadatim funkcijama 
 
my_favourite_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
 
text_file = open("output.txt", "a")
text_file.write(f"{my_favourite_book}\n")                                       #Uvod u serijalizaciju
text_file.close()
"""
                                                                                                                   
"""                                                                                                                 
class Book:                                                                                                         
    def __init__(self, title, author, published, genre):                                                            
        self.title = title                                                                                          
        self.author = author                                                                                        
        self.published = published                                        #VEZANO ZA PRETHODNI PRIMER              
        self.genre = genre
 
    def __str__(self):
        return f'{self.title}, {self.author}, {self.published}, {self.genre}'
"""

"""
text_file = open("output.txt", "r")
my_favourite_book_data = text_file.read()
text_file.close()                                                              #Uvod u deserijalizaciju
 
print(my_favourite_book_data)
"""

"""
from Book import Book
 
text_file = open("output.txt", "r")
my_favourite_book_data = text_file.read()
text_file.close()
 
def from_string_to_book(string_book):
    attributes = string_book.split(',')
 
    for i in range(len(attributes)):                                                           #Deserijalizacija
        attributes[i] = attributes[i].strip()
 
    return Book(attributes[0], attributes[1], attributes[2], attributes[3])
 
my_favourite_book = from_string_to_book(my_favourite_book_data)
 
print(my_favourite_book.title)
print(my_favourite_book.author)
print(my_favourite_book.published)
print(my_favourite_book.genre)
"""

#PICKLE

"""
import pickle
from Book import Book
 
my_favourite_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")                    #Serijalizacija uz pomoc PICKLE-A
 
with open('my_book.pkl', 'wb') as file:
    pickle.dump(my_favourite_book, file)
"""

"""
import pickle
 
with open('my_book.pkl', 'rb') as file:                                                           #Deserijalizacija uz pomoc PICKLE-A
    my_favourite_book = pickle.load(file)
 
print(my_favourite_book)
"""

"""
import pickle
from Book import Book
 
books = []
 
with open('library.pkl', 'rb') as file:
    books = pickle.load(file)
 
command = input("Add new (Y/N)?")
 
while command == 'Y':
 
    book_title = input("Book title:")
    book_author = input("Book author:")
    book_published = input("Year of publishing:")                                            #PRIMER ZA DODAVANJE KNJIGA ICUVANJE ISTIH
    book_published = int(book_published)                                                     #NIJE DOBAR ZADATAK ZATO STO FALI FAJL 
    book_genre = input("Book genre:") 
 
    book = Book(book_title, book_author, book_published, book_genre)
 
    books.append(book)
    with open('library.pkl', 'wb') as file:
        pickle.dump(books, file)
 
    print(f"You have added new book : {book.title}")
 
    command = input("Add new (Y/N)?")
 
print("\nAll books in the library:")
for book in books:
    print(book)
 
print("\nGoodbye!")
"""

#OS

"""
import os

print(os.listdir("/"))                                                                      #ISCITAVANJE CELOG C DISKA
"""

"""
import os

path = os.getcwd()                                                                         #ISCITAVANJE TRENUTNO OTVORENOG FOLDERA

print(os.listdir(path))
"""

"""
import os

path = os.path.join(os.getcwd(), "new")                                                     #PRAVLJENJE NOVOG FOLDERA
os.mkdir(path)
"""

"""
import os

path = os.path.join(os.getcwd(), "new")                                                     #BRISANJE NOVOG FOLDERA
os.mkdir(path)
"""

"""
import os 

is_exist = os.path.exists("ime foldera")                                                  #PROVERA POSTOJANJA FOLDERA ILI FAJLA
print(is_exist)
"""

"""
import os
import pickle
from Book import Book
 
books = []
 
if os.path.exists('library.pkl'):
    with open('library.pkl', 'rb') as file:
        books = pickle.load(file)
 
if(len(books) > 0):
    print("\nAll books in the library:")
    for book in books:
        print(book) 
 
command = input("Add new (Y/N)?")                                                                  #primer unosenja knjiga i iscitavanje istih
  
while command == 'Y':
 
    book_title = input("Book title:")
    book_author = input("Book author:")
    book_published = input("Year of publishing:")
    book_published = int(book_published)
    book_genre = input("Book genre:")
 
    book = Book(book_title, book_author, book_published, book_genre)
 
    books.append(book)
    with open('library.pkl', 'wb') as file:
        pickle.dump(books, file)
 
    print(f"You have added new book : {book.title}")
 
    command = input("Add new (Y/N)?")
 
print("\nGoodbye!")
"""

"""
import os
import pickle
 
todos = []
 
if os.path.exists('todos.pkl'):
    with open('todos.pkl', 'rb') as file:
        todos = pickle.load(file)
 
running = True
 
while running:
 
    command = input("What you want to do?\nread(1)\nremove(2)\nadd(3)\nexit(4)\n")
 
    if command == '1':
        if(len(todos) == 0):
            print('\nNo todos.\n')
        else:
            print("\nAll todo's:")
            for index in range(len(todos)):
                print(f"{index+1}. {todos[index]}")                                                #MINI PROJEKAT ZA KREIRANJE PODSETNIKA
            print('\n')
    elif command == '2':
        index = input("\nEnter the number of todo you want to delete?\n")
        index = int(index) - 1
        if (0 <= index) and (index < len(todos)):
            todos.remove(todos[index])
            with open('todos.pkl', 'wb') as file:
                pickle.dump(todos, file)
            print('\nTodo removed.\n')
        else:
            print('\nTodo does not exists.\n')
    elif command == '3':
        todo = input("\nTodo:")
        todos.append(todo)
        with open('todos.pkl', 'wb') as file:
            pickle.dump(todos, file)
        print(f"\nYou have added new todo.\n")
    elif command == '4':
        running = False
    else:
        print("\nWrong command.\n")
 
print("\nGoodbye!")
"""








