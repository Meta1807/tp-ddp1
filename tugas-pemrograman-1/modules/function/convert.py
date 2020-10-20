import re  # Used for checking if number is not valid
from ..class_.Conversion import Conversion  # Import Number class from _class subpackage

# This dictionary is used for dynamic formatting of the output string.
base = {3: 'ternary', 7: 'septenary', 10: 'decimal'}

def convert(input_base: int, output_base: int):
    ''' Asks user to input a number and converts it to a base-n value (via Number class' to_base() method).

        [ARGUMENTS]
            - input_base: int
            - output_base: int

        [INFO]
        The "convert()" function asks the user to input a valid base-n number (radix determined by input_base param) 
        and converts it to a Number object. The program then calls static methods from the Conversion class to 
        convert it into the requested base and prints the number to STDOUT. The outputted string will change 
        based on the input_base and output_base parameters. This function uses regex with a dynamically 
        formatted pattern to check if an inputted number is valid.

    '''
    number = ''
    loop = True
    regular_pattern = '[^%s-%s]' % (0, input_base - 1)  # Dynamically format regex pattern based on "input_base"

    while loop == True:
        number = input("Masukkan input angka: ")
        # Reject input if regex search returns one or more matches or if input contains alphabet.
        if number.isnumeric() == False or re.match(regular_pattern, number):
            print("Input angka harus %s" % (base[input_base]))
        else:
            break

    number_dec = Conversion.to_decimal(number, input_base)  # Use the to_decimal static method from the Conversion class
    print("Nilai %s dari %s %s adalah %s" % (base[output_base], base[input_base], number, Conversion.to_base(number_dec, output_base)))

