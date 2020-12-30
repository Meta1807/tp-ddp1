def search(bookName: str, library: dict, libraryKeys: list):
    ''' Searches for a specified book in all shelves in the library

        [ARGUMENTS]
            - bookName: str
            - library: dict
            - libraryKeys: list

        [DESCRIPTION]
        This function searches for a specified book in the library's data structure. It will recurse through the library
        and attempt to find the specified book. The function returns an empty list if it does not find any books with the
        specified name.

    '''
    if len(libraryKeys) == 0:
        return []

    elif len(libraryKeys) == 1:
        if bookName in library[libraryKeys[0]]:
            return [library[libraryKeys[0]][bookName], libraryKeys[0]]
        else:
            return []

    elif len(libraryKeys) > 1:
        return search(bookName, library, [libraryKeys[0]]) + search(bookName, library, libraryKeys[1:])

        

if __name__ == '__main__':  # When run directly this will execute test code
    library = {'rak1': { 'test': 'testDesc' }}
    library1 = {'rak1': { 'test': 'testDesc' }, 'rak2': { 'test1': 'testDesc', 'test2': 'testDesc' }}
    library2 = {}

    print(search('test', library, list(library.keys())))
    print(search('test1', library1, list(library1.keys())))
    print(search('test2', library1, list(library1.keys())))
    print(search('', library, list(library.keys())))