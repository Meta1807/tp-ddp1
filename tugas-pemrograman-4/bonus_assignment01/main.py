from classes.Book import *
from classes.Library import *
from classes.Shelf import *
from classes.Interface import *
from tkinter import *

def main():
    libraryData = Library()
    while True:
        try:
            user_input = input("Perintah anda: ").split()
            if user_input[0] == "ADD":
                try:
                    if user_input[1] == "BUKU":
                        root = Tk()
                        menu = AddMenu(libraryData, master=root)
                        menu.mainloop()
                    
                    elif user_input[1] == "RAK":
                        root = Tk()
                        menu = ShelfMenu(libraryData, master=root)
                        menu.mainloop()

                except Exception:
                    print("Perintah tidak valid.")
                    print("Perintah tersedia:")
                    print("- ADD BUKU <Rak> <Nama Buku> <Tahun Terbit> <Pengarang> <Penerbit> <Jenis> <Atribut Khusus>")
                    print("- ADD RAK <Nama> <Tipe>")

            if user_input[0] == "SEARCH":
                root = Tk()
                menu = SearchMenu(libraryData, master=root)
                menu.mainloop()

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
