from classes.Book import *
from classes.Library import *
from classes.Shelf import *

def main():
    libraryData = Library()
    while True:
        try:
            user_input = input("Perintah anda: ").split()
            if user_input[0] == "ADD":
                try:
                    if user_input[1] == "BUKU":
                        check = libraryData.searchBook(user_input[3])
                        if check:
                            print(f"Buku dengan nama {user_input[3]} sudah ada di dalam sistem.")
                            
                        else:
                            book = libraryData.addBook(*user_input[2:])
                            if book:
                                print(f"Buku baru berhasil ditambahkan pada {user_input[2]}")
                                print(book)
                            else:
                                print("Buku gagal ditambahkan :(")
                    
                    elif user_input[1] == "RAK":
                        status = libraryData.addShelf(*user_input[2:])
                        try:
                            if status:
                                print("Rak baru berhasil ditambahkan\n")
                                print(f"Nama : {user_input[2]}")
                                print(f"Jenis : {user_input[3]}")
                            else:
                                print(f'Rak dengan nama {user_input[2]} sudah ada di dalam sistem.')
                        except KeyError:
                            print(f"Tidak dapat menambahkan Rak dengan jenis {user_input[3]}")
                        except Exception:
                            print("Perintah Tidak Valid.")
                            print("Penggunaan Command: ADD BUKU <Rak> <Nama Buku> <Tahun Terbit> <Pengarang> <Penerbit> <Jenis> <Atribut Khusus>")

                except Exception:
                    print("Perintah tidak valid.")
                    print("Perintah tersedia:")
                    print("- ADD BUKU <Rak> <Nama Buku> <Tahun Terbit> <Pengarang> <Penerbit> <Jenis> <Atribut Khusus>")
                    print("- ADD RAK <Nama> <Tipe>")

            if user_input[0] == "SEARCH":
                try:
                    book = libraryData.searchBook(user_input[1])
                    if book:
                        print('Buku ditemukan\n')
                        print(book)
                    else:
                        print(f'Buku dengan nama {user_input[1]} tidak ditemukan.')
                except:
                    print("Perintah tidak valid.")
                    print("Penggunaan Perintah: SEARCH <Nama Buku>")

            if user_input[0] == 'LIST':
                libraryData.listShelves()

            if user_input[0] == 'EXIT':
                break
        except IndexError:
            print("Perintah Invalid.")
        
        finally:
            print()

if __name__ == "__main__":
    main()
