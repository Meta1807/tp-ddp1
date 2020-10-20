# This variable is the array of strings that will be printed by the main_menu() function.
menu =  [   
            "====================================================",
            "    Selamat datang di Program Konverter Bilangan",
            "    Created By: Adrian Ardizza - DDP1 Kelas C",
            "====================================================",
            "    1. Decimal ke Ternary",
            "    2. Ternary ke Decimal",
            "    3. Decimal ke Septenary",
            "    4. Septenary ke Decimal",
            "    5. Ternary ke Septenary",
            "    6. Septenary ke Ternary",
            "    7. Keluar",
            "For more information about this application, enter 'a'"
            
        ]

technical = [
                "========================================================",
                "        Technical Information for This Program",
                "========================================================",
                "                 External Libraries Used:",
                "             os (for executing shell commands)",
                "                sys (for detecting host OS)",
                "         re (for checking if number input is valid)",
                "\n",
                "  All Functions defined  in  this  program's  modules",
                "  folder has been written by me, with some exceptions",
                "  being  the  use of  the  aforementioned  libraries",
                "  for regex and os shell support.",
                "\n",
                "  In making this program, I used the slides given for",
                "  the  base  conversion section  of  'Introduction to",
                "  Digital   Systems'  as  reference   in  coding  the",
                "  base conversion algorithms (specifically  base-n to",
                "  base-10 and base-10 to base-n conversion)"
                "\n"
            ]

def main_menu():
    '''  Prints every item in the menu array.  '''
    for item in menu:
        print(item)

def technical_menu():
    ''' Prints every item in the technical array. '''
    for item in technical:
        print(item)
