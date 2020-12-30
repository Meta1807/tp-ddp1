from .shelf import addShelf
from ..recursive.search import search
from ..table.table import printTable

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
        
        if len(libraryObject[shelf]['books']) < libraryObject[shelf]['capacity']:
            libraryObject[shelf]['books'][bookObject['name']] = {
                'year': bookObject['year'],
                'writer': bookObject['writer'],
                'publisher': bookObject['publisher'],
                'genre': bookObject['genre']
            }
            printTable(bookObject['name'], [bookObject, shelf])
            return True

        else:
            print(f'Rak dengan nama {shelf} sudah penuh.')
            for i in list(libraryObject.keys()):
                if len(libraryObject[i]['books']) < libraryObject[i]['capacity']:
                    print(f'Buku ditambahkan pada {i}')
                    libraryObject[i]['books'][bookObject['name']] = {
                        'year': bookObject['year'],
                        'writer': bookObject['writer'],
                        'publisher': bookObject['publisher'],
                        'genre': bookObject['genre']
                    }
                    printTable(bookObject['name'], [bookObject, i])
                    return True
                
            else:
                i = 1
                while True:
                    status = addShelf(f'RakTambahan{i}', libraryObject)
                    if status == False:
                        i += 1
                        continue
                    else:
                        libraryObject[f'RakTambahan{i}']['books'][bookObject['name']] = {
                            'year': bookObject['year'],
                            'writer': bookObject['writer'],
                            'publisher': bookObject['publisher'],
                            'genre': bookObject['genre']
                        }
                        print(f'Buku ditambahkan pada RakTambahan{i}')
                        printTable(bookObject['name'], [bookObject, f'RakTambahan{i}'])
                        return True
