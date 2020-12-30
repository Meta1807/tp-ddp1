from classes.Book import *
from classes.Library import *
from classes.Shelf import *
from classes.Interface import *
from tkinter import *

def main():
    libraryData = Library()
    menuRoot = Tk()
    mainMenu = MainMenu(libraryData, master=menuRoot)
    mainMenu.mainloop()

if __name__ == "__main__":
    main()
