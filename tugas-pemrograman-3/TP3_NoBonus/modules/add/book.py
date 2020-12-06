from .shelf import addShelf
from ..recursive.search import search

def addBook(bookObject: dict, libraryObject: dict, shelf: str):
    ''' Adds a new book into the specified shelf.

        [ARGUMENTS]
        - bookObject: dict
        - libraryObject: dict
        - shelf: str

        [DESCRIPTION]
        This function adds a new book into the system. Because there is a constraint in the program specifications that
        disallows duplicate books in any of the library's shelves, this function will first call the recursive search
        function. If the search function does not return any results, it will then check if the specified shelf exists
        in the system, generate it if it does not, and then add the book into the shelf.

    '''
    if search(bookObject['name'], libraryObject, list(libraryObject.keys())):
        return False
    else:
        if shelf not in libraryObject.keys():
            addShelf(shelf, libraryObject)
        libraryObject[shelf][bookObject['name']] = {
            'year': bookObject['year'],
            'writer': bookObject['writer'],
            'publisher': bookObject['publisher'],
            'genre': bookObject['genre']
        }
        return True