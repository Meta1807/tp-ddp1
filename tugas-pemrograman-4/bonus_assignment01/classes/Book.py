class Book():
    ''' Base class for all book objects

        Description:
        The Book class is the base class for all objects that store Book information in the program. This class' methods and variables
        is shared between all classes, hence removing the need for repetitive and explicit reassignment of variables in it's derived classes.

    '''
    def __init__(self, name, year, writer, publisher) -> None:
        ''' Initialization function called on object instantiation 
        
            Parameters:
            name (str)   : Book title, given by user
            year (str)   : Year published, given by user
            writer (str) : Book writer, given by the user
            publisher (str): Book publisher, given by the user

            Returns:
            None

        '''
        self.__name = name
        self.__year = year
        self.__writer = writer
        self.__publisher = publisher

    def getName(self) -> str:
        ''' Getter function for the object's private name attribute. 
        
            Parameters:
            self: Book

            Returns:
            str

        '''
        return self.__name
    
    def getAttributes(self):
        ''' Getter function that returns all of the object's attributes in the form of a list.
        
            Paramaters:
            self: Book

            Returns:
            list

        '''
        return [self.__name, self.__year, self.__writer, self.__publisher]


class Fiksi(Book):
    ''' Stores all of the information required for Fiction books
    
        Description:
        The Fiksi class stores all of the information required to represent a Fiksi book in the program. This class extends it's parent object
        (Book) by adding a new attribute __genre and adds a new method called getBookDescription for returning a dictionary with the book's
        contents.

    '''
    def __init__(self, name: str, year: int, writer: str, publisher: str, genre: str):
        ''' Initialization function called on object instantiation 
        
            Parameters:
            name (str)   : Book title
            year (str)   : Year published
            writer (str) : Book writer
            publisher (str): Book publisher
            genre (str): Book genre, specific to the Fiksi class

            Returns:
            None

        '''
        super().__init__(name, year, writer, publisher)
        self.__genre = genre

    def getBookDescription(self) -> dict:
        ''' The getBookDescription method returns a dictionary with the attributes of this classes' base class along with it's extra attribute. '''
        return {
            'name': self.getAttributes()[0],
            'year': self.getAttributes()[1],
            'writer': self.getAttributes()[2],
            'publisher': self.getAttributes()[3],
            'genre': self.__genre
        }

    def __str__(self) -> str:
        ''' Returns all details stored by the object in the form of a formatted string when the program requests the string representation of the object. '''
        info = (
            "Buku Fiksi\n"
            f"Nama Buku     : {self.getBookDescription()['name']}\n"
            f"Tahun         : {self.getBookDescription()['year']}\n"
            f"Pengarang     : {self.getBookDescription()['writer']}\n"
            f"Penerbit      : {self.getBookDescription()['publisher']}\n"
            f"Genre         : {self.getBookDescription()['genre']}\n"
        )
        return info

class Referensi(Book):
    ''' This class stores all information required to represent a Reference book in the system. '''
    def __init__(self, name: str, year: int, writer: str, publisher: str, location: str) -> None:
        super().__init__(name, year, writer, publisher)
        self.__location = location

    def getBookDescription(self):
        ''' The getBookDescription method returns a dictionary with the attributes of this classes' base class along with it's extra attribute. '''
        return {
            'name': self.getAttributes()[0],
            'year': self.getAttributes()[1],
            'writer': self.getAttributes()[2],
            'publisher': self.getAttributes()[3],
            'location': self.__location
        }

    def __str__(self):
        ''' Returns all details stored by the object in the form of a formatted string when the program requests the string representation of the object. '''
        info = (
            "Buku Referensi\n"
            f"Nama Buku     : {self.getBookDescription()['name']}\n"
            f"Tahun         : {self.getBookDescription()['year']}\n"
            f"Pengarang     : {self.getBookDescription()['writer']}\n"
            f"Penerbit      : {self.getBookDescription()['publisher']}\n"
            f"Lokasi Terbit : {self.getBookDescription()['location']}\n"
        )
        return info

class Ensiklopedia(Book):
    ''' This class stores all information required to represent a Encyclopedia book in the system. '''
    def __init__(self, name: str, year: int, writer: str, publisher: str, revision: str):
        super().__init__(name, year, writer, publisher)
        self.__revision = revision
    
    def getBookDescription(self):
        ''' The getBookDescription method returns a dictionary with the attributes of this classes' base class along with it's extra attribute. '''
        return {
            'name': self.getAttributes()[0],
            'year': self.getAttributes()[1],
            'writer': self.getAttributes()[2],
            'publisher': self.getAttributes()[3],
            'revision': self.__revision
        }    

    def __str__(self):
        ''' Returns all details stored by the object in the form of a formatted string when the program requests the string representation of the object. '''
        info = (
            "Buku Ensiklopedia\n"
            f"Nama Buku     : {self.getBookDescription()['name']}\n"
            f"Tahun         : {self.getBookDescription()['year']}\n"
            f"Pengarang     : {self.getBookDescription()['writer']}\n"
            f"Penerbit      : {self.getBookDescription()['publisher']}\n"
            f"Revisi        : {self.getBookDescription()['revision']}\n"
        )
        return info