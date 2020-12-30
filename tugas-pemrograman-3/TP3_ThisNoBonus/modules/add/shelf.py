def addShelf(shelfName: str, libraryObject: dict):
    ''' Adds a new shelf into the library system.

        [ARGUMENTS]
        - shelfName: str
        - libraryObject: dict

        [DESCRIPTION]
        This function adds a new shelf into the system. If the user attempts to add an already added shelf, it will respond with a rejection
        message and does not add a new shelf. Otherwise, it will add a new shelf into the system (i.e a key-value pair of the shelf name and
        an empty dictionary.)

    '''
    if shelfName in libraryObject.keys():
        print(f'Rak dengan nama {shelfName} sudah ada di dalam sistem')
    else:
        libraryObject[shelfName] = {}
        print(f'Rak dengan nama {shelfName} telah berhasil ditambahkan.')
        return True