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
    if len(libraryObject[newShelf]['books']) < libraryObject[newShelf]['capacity']:
        print(f'Buku dengan nama {bookName} dipindahkan dari rak dengan nama {oldShelf} ke rak dengan nama {newShelf}')
        libraryObject[newShelf]['books'][bookName] = libraryObject[oldShelf]['books'].pop(bookName)
    else:
        print(f'Rak dengan nama {newShelf} sudah penuh.')
        for i in list(libraryObject.keys()):
            if len(libraryObject[i]['books']) < libraryObject[i]['capacity']:
                libraryObject[newShelf]['books'][bookName] = libraryObject[oldShelf]['books'].pop(bookName)
                print(f'Buku dengan nama {bookName} dipindahkan dari rak dengan nama {oldShelf} ke rak dengan nama {i}')
                return True
        else:
            i = 1
            while True:
                status = addShelf(f'RakTambahan{i}', libraryObject)
                if status == False:
                    i += 1
                    continue
                else:
                    libraryObject[f'RakTambahan{i}']['books'][bookName] = libraryObject[oldShelf]['books'].pop(bookName)
                    print(f'Buku dengan nama {bookName} dipindahkan dari rak dengan nama {oldShelf} ke rak dengan nama RakTambahan{i}')
                    return True