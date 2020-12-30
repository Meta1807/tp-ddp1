from .Shelf import Pengetahuan, Dunia, Misteri, Compendium
from .Book import Referensi, Fiksi, Ensiklopedia

class Library():
    ''' This class is the main class that stores all of the Shelf objects in the system. 
    
        Description:
        This class stores all Shelf objects in the system in it's private "shelves" attribute. The shelves attribute is a dictionary which
        stores the Shelf objects in a key-value pair with the shelf's name as the key and the corresponding Shelf object as the value.

        Methods:
        - getShelves -> dict:
            Returns the Dictionary containing the library's shelves.
        - addShelf -> Shelf/bool:
            Adds a new shelf to the library.
        - addBook -> Book/bool:
            Adds a new book to the library.
        - searchBook -> Book/bool:
            Attempts to search for the requested book in shelves. Returns either the Book object if found or False if it isn't.
        - listShelves -> Boolean:
            Lists all shelves in the system along with the books contained in them. Returns False if the library does not contain atleast 1 book.

    '''
    def __init__(self):
        defaultShelves = {
            'Pengetahuan01': Pengetahuan(),
            'Dunia01': Dunia(),
            'Misteri01': Misteri(),
            'Compendium01': Compendium()
        }
        self.__shelves = defaultShelves
    
    def getShelves(self):
        return self.__shelves

    def addShelf(self, shelf, shelfType):
        shelfTypes = {'Pengetahuan': Pengetahuan, 'Dunia': Dunia, 'Misteri': Misteri, 'Compendium': Compendium}
        if shelf not in self.getShelves():
            self.getShelves()[shelf] = shelfTypes[shelfType]()
            return self.getShelves()[shelf]
        return False

    def addBook(self, shelf, title, year, writer, publisher, bookType, attribute):
        bookTypes = {'Fiksi': Fiksi, 'Referensi': Referensi, 'Ensiklopedia': Ensiklopedia}
        if bookType in ['Fiksi', 'Referensi', 'Ensiklopedia'] and shelf in self.getShelves():
            book = bookTypes[bookType](title, year, writer, publisher, attribute)
            return self.getShelves()[shelf].addBook(book)
        else:
            return False

    def searchBook(self, name):
        for i in self.getShelves():
            book = self.getShelves()[i].searchBook(name)
            if book:
                return book
        else:
            return False

    def listShelves(self):
        for i in self.getShelves():
            if len(self.getShelves()[i].getBooks()) != 0:
                break
        else:
            print("Perpustakaan tidak memiliki buku :(")
            return False
            
        print()
        for i in self.getShelves():
            print(i)
            books = self.getShelves()[i].listBook()
            if books:
                print(books)
