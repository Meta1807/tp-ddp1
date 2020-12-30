from modules.add.book import addBook
from modules.add.shelf import addShelf
from modules.move.move import moveBook
from modules.recursive.search import search
from modules.table.table import printTable

def main():
    libraryData = {}
    while True:
        print('Selamat datang di The The Great Library')
        print('Silahkan masukkan perintah!')
        command = input('Perintah anda: ').split()
        try:
            if command[0] == 'ADD':
                try:
                    if command[1] == 'RAK':
                        try:
                            addShelf(command[2], libraryData)
                        except:
                            print('PERINTAH TIDAK VALID, USAGE: ADD RAK <Nama Rak>')

                    elif command[1] == 'BUKU':
                        try:
                            book = {
                                'name': command[3],
                                'writer': command[4],
                                'year': command[5],
                                'publisher': command[6],
                                'genre': command[7]
                            }
                            status = addBook(book, libraryData, command[2])
                            if status == True:
                                print('Buku berhasil ditambahkan!')
                                printTable(command[3], [book, command[2]])
                            else:
                                print('Buku dengan nama yang sama sudah ada di The The Great Library')

                        except IndexError:
                            print('Perintah Tidak Valid')
                            print('Penggunaan Command: ADD BUKU <Nama Rak> <Judul Buku> <Penulis> <Tahun Terbit> <Penerbit> <Genre Buku>')

                    else:
                        print('Perintah Tidak Valid')
                        print('Command Tersedia: ADD RAK, ADD BUKU')
                
                except IndexError:
                    print('Perintah Tidak Valid')
                    print('Command Tersedia: ADD RAK, ADD BUKU')

            elif command[0] == 'MOVE':
                try:
                    if command[1] == 'BUKU':
                        buku = search(command[2], libraryData, list(libraryData.keys()))
                        if buku:
                            moveBook(command[2], buku[1], command[3], libraryData)
                            print(f'Buku dengan nama {command[2]} dipindahkan dari rak dengan nama {buku[1]} ke rak dengan nama {command[3]}')
                        else:
                            print(f'Buku dengan nama {command[2]} tidak ditemukan dalam sistem.')

                    else:
                        print('Perintah Tidak Valid')
                        print('Penggunaan Command: MOVE BUKU <Nama Buku> <Rak Tujuan>')

                except IndexError:
                    print('Perintah Tidak Valid')
                    print('Penggunaan Command: MOVE BUKU <Nama Buku> <Rak Tujuan>')

            elif command[0] == 'SEARCH':
                try:
                    if command[1] == 'BUKU':
                        result = search(command[2], libraryData, list(libraryData.keys()))
                        if result:
                            printTable(command[2], result)
                        else:
                            print(f'Buku tidak ditemukan')

                except IndexError:
                    print('Perintah Tidak Valid')
                    print('Penggunaan Command: SEARCH BUKU <Nama Buku>')

            elif command[0] == 'EXIT':
                break

            else:
                print('Command tidak ditemukan, untuk melihat guide silahkan ketik HELP')

        except IndexError:
            print('Untuk melihat guide, silahkan ketik HELP')

        finally:
            print()

if __name__ == '__main__':
    main()