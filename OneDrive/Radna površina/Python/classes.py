class Book:                                                                                                         
    def __init__(self, title, author, published, genre):                                                            
        self.title = title                                                                                          
        self.author = author                                                                                        
        self.published = published                                        #VEZANO ZA PRETHODNI PRIMER              
        self.genre = genre
 
    def __str__(self):
        return f'{self.title}, {self.author}, {self.published}, {self.genre}'