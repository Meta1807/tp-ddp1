from tkinter import *

class MainMenu(Frame):
    def __init__(self, libraryData, master=None):
        super().__init__(master)
        self.master = master
        self.libraryData = libraryData
        self.initInterface()
        self.initInterfaceElements()
    
    def initInterface(self):
        self.master.title("The Great Library - CRUD v1.0")
        self.master.geometry('500x150')
        self.elementFrame = Frame(self.master)

    def initInterfaceElements(self):
        Label(self.elementFrame, text="Selamat datang di The The Great Library. Silahkan pilih Menu yang tersedia.").grid(row=0, column=1)
        Button(self.elementFrame, text="ADD BUKU", command=self.renderBookMenu).grid(row=1, column=1)
        Button(self.elementFrame, text="ADD RAK", command=self.renderShelfMenu).grid(row=2, column=1)
        Button(self.elementFrame, text="SEARCH", command=self.renderSearchMenu).grid(row=3, column=1)
        Button(self.elementFrame, text="LIST", command=self.listBooks).grid(row=4, column=1)
        # Initiate elementFrame
        self.elementFrame.pack()

    def renderBookMenu(self):
        root = Tk()
        menu = AddMenu(self.libraryData, master=root)
        menu.mainloop()

    def renderShelfMenu(self):
        root = Tk()
        menu = ShelfMenu(self.libraryData, master=root)
        menu.mainloop()

    def renderSearchMenu(self):
        root = Tk()
        menu = SearchMenu(self.libraryData, master=root)
        menu.mainloop()

    def listBooks(self):
        self.libraryData.listShelves()


class AddMenu(Frame):
    def __init__(self, libraryData, master=None):
        super().__init__(master)
        self.master = master
        self.libraryData = libraryData
        self.initInterface()
        self.initInterfaceElements()
    
    def initInterface(self):
        self.master.title("Add Buku")
        self.master.geometry('300x200')
        self.elementFrame = Frame(self.master)

    def initInterfaceElements(self):
        Label(self.elementFrame, text="Form Tambah Buku").grid(row=0, column=1)
        self.interfaceElements = {
            'type': [Label(self.elementFrame, text="Jenis"), Entry(self.elementFrame)],
            'shelf': [Label(self.elementFrame, text="Rak"), Entry(self.elementFrame)],
            'name': [Label(self.elementFrame, text="Nama"), Entry(self.elementFrame)],
            'year': [Label(self.elementFrame, text="Tahun"), Entry(self.elementFrame)],
            'writer': [Label(self.elementFrame, text="Penulis"), Entry(self.elementFrame)],
            'publisher': [Label(self.elementFrame, text="Penerbit"), Entry(self.elementFrame)],
            'extra': [Label(self.elementFrame, text="Extra"), Entry(self.elementFrame)]
        }
        for i, item in enumerate(self.interfaceElements):
            for j, element in enumerate(self.interfaceElements[item]):
                element.grid(row=i + 1, column=j)

        Button(self.elementFrame, text="Submit", command=self.submit).grid(row=len(self.interfaceElements) + 1, column=1)
        # Initiate elementFrame
        self.elementFrame.pack()

    def submit(self):
        details = {
            'type': self.interfaceElements['type'][1].get(),
            'shelf': self.interfaceElements['shelf'][1].get(),
            'name': self.interfaceElements['name'][1].get(),
            'year': self.interfaceElements['year'][1].get(),
            'writer': self.interfaceElements['writer'][1].get(),
            'publisher': self.interfaceElements['publisher'][1].get(),
            'extra': self.interfaceElements['extra'][1].get()
        }
        check = self.libraryData.searchBook(details['name'])

        if check:
            print(f"Buku dengan nama {details['name']} sudah ada di dalam sistem.")
            
        else:
            book = self.libraryData.addBook(details['shelf'], details['name'], details['year'], details['writer'], details['publisher'], details['type'], details['extra'])
            if book:
                print(f"Buku baru berhasil ditambahkan pada {details['shelf']}")
                print(book)
                self.master.destroy()
            else:
                print("Buku gagal ditambahkan :(")
                self.master.destroy()

class ShelfMenu(Frame):
    def __init__(self, libraryData, master=None):
        super().__init__(master)
        self.master = master
        self.libraryData = libraryData
        self.initInterface()
        self.initInterfaceElements()
    
    def initInterface(self):
        self.master.title("Add Buku")
        self.master.geometry('300x200')
        self.elementFrame = Frame(self.master)

    def initInterfaceElements(self):
        Label(self.elementFrame, text="Form Tambah Rak").grid(row=0, column=1)
        self.interfaceElements = {
            'name': [Label(self.elementFrame, text="Nama"), Entry(self.elementFrame)],
            'type': [Label(self.elementFrame, text="Jenis"), Entry(self.elementFrame)],
        }
        for i, item in enumerate(self.interfaceElements):
            for j, element in enumerate(self.interfaceElements[item]):
                element.grid(row=i + 1, column=j)

        Button(self.elementFrame, text="Submit", command=self.submit).grid(row=len(self.interfaceElements) + 1, column=1)
        # Initiate elementFrame
        self.elementFrame.pack()

    def submit(self):
        details = {
            'type': self.interfaceElements['type'][1].get(),
            'name': self.interfaceElements['name'][1].get()
        }
        if details['type'] in ['Pengetahuan', 'Dunia', 'Misteri', 'Compendium']:
            status = self.libraryData.addShelf(details['name'], details['type'])
            if status:
                print("Rak baru berhasil ditambahkan\n")
                print(f"Nama : {details['name']}")
                print(f"Jenis : {details['type']}")
                self.master.destroy()
            else:
                print(f"Rak dengan nama {details['name']} sudah ada di dalam sistem.")
                self.master.destroy()
        else:
            print(f"Tidak dapat menambahkan Rak dengan jenis {details['type']}")
            self.master.destroy()

class SearchMenu(Frame):
    def __init__(self, libraryData, master=None):
        super().__init__(master)
        self.master = master
        self.libraryData = libraryData
        self.initInterface()
        self.initInterfaceElements()
    
    def initInterface(self):
        self.master.title("Add Buku")
        self.master.geometry('300x200')
        self.elementFrame = Frame(self.master)

    def initInterfaceElements(self):
        Label(self.elementFrame, text="Form Cari Buku Rak").grid(row=0, column=0)
        self.interfaceElements = {
            'search': [Entry(self.elementFrame)]
        }
        for i, item in enumerate(self.interfaceElements):
            for j, element in enumerate(self.interfaceElements[item]):
                element.grid(row=i + 1, column=j)

        Button(self.elementFrame, text="Submit", command=self.submit).grid(row=len(self.interfaceElements) + 1, column=0)
        # Initiate elementFrame
        self.elementFrame.pack()

    def submit(self):
        search = self.interfaceElements['search'][0].get()
        book = self.libraryData.searchBook(search)
        if book:
            print('Buku ditemukan\n')
            print(book)
            self.master.destroy()
        else:
            print(f'Buku dengan nama {search} tidak ditemukan.')
            self.master.destroy()

