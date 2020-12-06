def printTable(title: str, info: list):
    ''' Prints a formatted table of a book's info '''
    print(f'{"Posisi":<15}: {info[1]}')
    print(f'{"Nama Buku":<15}: {title}')
    print(f'{"Pengarang":<15}: {info[0]["writer"]}')
    print(f'{"Penerbit Buku":<15}: {info[0]["publisher"]}')
    print(f'{"Tahun Terbit":<15}: {info[0]["year"]}')
    print(f'{"Genre":<15}: {info[0]["genre"]}')