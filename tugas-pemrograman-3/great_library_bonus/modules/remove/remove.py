from ..add.shelf import addShelf

def removeShelf(shelfName: str, libraryData: dict):
    ''' Removes a shelf and move the books it previously contained into the next shelf available shelf

        [ARGUMENTS]
        - shelfName: str
        - libraryData: dict

        [DESCRIPTION]
        This function removes a shelf and moves the books to the other in a round-robin manner. The function will iterate through the list
        of available shelves and inserts the book to the shelf if it has capacity. If all of the added shelf's capacity has been exceeded,
        the function will generate new shelves accordingly.

    '''
    if shelfName not in libraryData.keys():
        print(f'Rak dengan nama {shelfName} tidak ditemukan di dalam sistem')
        return False

    temporaryBooks = libraryData[shelfName]['books']
    del libraryData[shelfName]
    
    for i in list(temporaryBooks.keys()):
        for j in list(libraryData.keys()):
            if len(libraryData[j]['books']) < libraryData[j]['capacity']:
                print(f'{i} dipindahkan ke rak dengan nama {j}')
                libraryData[j]['books'][i] = temporaryBooks.pop(i)
                break
        else:
            k = 1
            while True:
                status = addShelf(f'RakTambahan{k}', libraryData)
                if status == False:
                    k += 1
                    continue
                else:
                    libraryData[f'RakTambahan{k}']['books'][i] = temporaryBooks.pop(i)
                    print(f'{i} dipindahkan ke rak dengan nama RakTambahan{k}')
                    break
    
    print(f'Rak dengan nama {shelfName} berhasil dihapus')
    return True