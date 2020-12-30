from .Book import *

class Shelf():
    ''' This class functions as a container for Book objects. It is the Parent to Pengetahuan, Dunia, Misteri, and Compendium
    
        Description:
        This class stores Book objects in it's private books attribute (List). It also contains all methods required to access the
        private books variable, search for books within the object, and to list all the books it is storing.

        Methods:
        - getBooks -> list:
            Returns the private attribute containing all books in the object.
        - searchBook -> Book/bool:
            Returns the requested book if it exists within the shelf, else it will return False.
        - listBook -> str:
            Returns a string which lists all the books in the shelf object.
        
    '''
    def __init__(self):
        self.__books = []
    
    def getBooks(self):
        return self.__books

    def searchBook(self, name):
        for item in self.getBooks():
            if item.getName() == name:
                return item
        else:
            return False

    def listBook(self):
        books = [x.getName() for x in self.getBooks()]
        string = ''
        for index, item in enumerate(sorted(books, key=lambda x: x.lower())):
            if index != len(books) - 1:
                string += f"   - {item}\n"
            else:
                string += f"   - {item}"
        return string

class Pengetahuan(Shelf):
    ''' This child class represents the Pengetahuan shelf sub-type and handles the logic required for checking and adding allowed books.
    
        Methods:
        - addBook -> Book/bool:
            Adds a book to the shelf. Before adding the book it will check if the book is either a Referensi book or a Ensiklopedia book.
            If it finds that the book is neither of those types, it will reject the operation. Else it will add the book object and returns
            it back to the function caller.
        
    '''
    def __init__(self):
        super().__init__()

    def addBook(self, book=''):
        if type(book).__name__ == 'Referensi' or type(Ensiklopedia).__name__ == 'Ensiklopedia':
            self.getBooks().append(book)
            return book
        else:
            return False

class Dunia(Shelf):
    ''' This child class represents the Dunia shelf subtype and handles all logic required for checking and adding allowed books.
    
        Methods:
        - addBook -> Book/bool:
            Adds a book to the shelf. Before adding the book it will check if the book is either a Fiksi book or a Ensiklopedia book.
            If it finds that the book is neither of those types, it will reject the operation. Else it will add the book object and returns
            it back to the function caller.
        
    '''
    def __init__(self):
        super().__init__()

    def addBook(self, book=None):
        if type(book).__name__ == 'Fiksi' or type(book).__name__ == 'Ensiklopedia':
            self.getBooks().append(book)
            return book
        else:
            return False

class Misteri(Shelf):
    ''' This child class represents the Misteri shelf subtype and handles all logic required for checking and adding allowed books.
    
        Methods:
        - addBook -> Book/bool:
            Adds a book to the shelf. Before adding the book it will check if the book is either a Fiksi book or a Referensi book.
            If it finds that the book is neither of those types, it will reject the operation. Else it will add the book object and returns
            it back to the function caller.
        
    '''
    def __init__(self):
        super().__init__()

    def addBook(self, book=None):
        if type(book).__name__ == 'Fiksi' or isinstance(book).__name__ == 'Referensi':
            self.getBooks().append(book)
            return book

        else:
            return False

class Compendium(Shelf):
    ''' This child class represents the Compendium shelf subtype and handles all logic required for checking and adding allowed books.
    
        Methods:
        - addBook -> Book:
            Adds a book to the shelf. This shelf allows any type of book to be added to it, hence unlike all of the previous classes, the
            addBook method will never reject a Book because of an invalid type.
        
    '''
    def __init__(self):
        super().__init__()

    def addBook(self, book=None):
        self.getBooks().append(book)
        return book