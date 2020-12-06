from ..add.shelf import addShelf

def moveBook(bookName: str, oldShelf: str, newShelf: str, libraryObject: dict):
    ''' Move a specified book from a shelf to another shelf.

        [ARGUMENTS]
        - bookName: str
        - oldShelf: str
        - newShelf: str
        - libraryObject: dict

        [DESCRIPTION]
        This function moves a specified a book from a shelf to another shelf. If it detects that the destination shelf does not exist,
        the function calls addShelf and generates the new shelf.

    '''
    if newShelf not in libraryObject.keys():
        addShelf(newShelf, libraryObject)
        libraryObject[newShelf][bookName] = libraryObject[oldShelf].pop(bookName)