# Import all required functions from the modules package
from modules.function.clear import clear_screen
from modules.function.menu import main_menu, technical_menu
from modules.function.convert import convert

clear_screen()  # Clear screen on program start using the clear module

def main():
    printed = 0
    while True:
        if printed == 0:
            clear_screen()
            main_menu()
            printed = 1

        option = input("Masukkan operasi yang ingin dilakukan: ")
        if option in ['1', '2', '3', '4', '5', '6', '7', 'a']:
            if option == '1':
                convert(10, 3)
            elif option == '2':
                convert(3, 10)
            elif option == '3':
                convert(10, 7)
            elif option == '4':
                convert(7, 10)
            elif option == '5':
                convert(3, 7)
            elif option == '6':
                convert(7, 3)
            elif option == '7':
                print("Terima kasih telah menggunakan program")
                break
            elif option == 'a':
                clear_screen()
                technical_menu()
            input("Press Enter to Continue...")
            printed = 0
        else:
            print("Maaf input tidak valid")

if __name__ == "__main__":
    main()
