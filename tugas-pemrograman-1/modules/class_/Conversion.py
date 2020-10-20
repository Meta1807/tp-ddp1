class Conversion():
    @staticmethod
    def to_decimal(value: str, base: int) -> str:
        ''' Converts a value to it's decimal equivalent.

        [PARAMETERS]
            - value: string
            - base: int

        [INFO]
        Whem method is called it will convert the user's inputted value into it's decimal representation
        and assign the value to itself (the class inherits int). for ease of conversion. The inputted value's 
        radix is determined by the "base" parameter.
        
        Base-n to Base-10 Conversion Algorithm:
            1. Create a variable to hold decimal_value and assign a default value of 0.
            2. Loop through the reversed value parameter and increments decimal_value by the value
               of the digit multiplied by "base" to the power of the digit's weight.
            3. Return decimal_value and base of the initial number

        [DISCLAIMER]
        The conversion algorithm only uses the int method to convert the user input
        into an integer value so it can be used in the calculation. It does not convert directly
        from base-n to base-10.
        '''
        decimal_value = 0
        for power, item in enumerate(value[::-1]):
            decimal_value += int(item) * (base ** int(power))  # Convert char to int and multiply by base ** power
        # Assign initial value inputted by user and its decimal representation to object property
        return decimal_value

    @staticmethod
    def to_base(decimal_value: int, output_base: int) -> str:
        ''' Convert object's "value" property to base-n

            [PARAMETERS]
                - output_base: 1 < int <= 10

            [INFO]
            The "to_base" method is used to convert the object's value property into it's base-n equivalent.
            It uses the standard method of converting from decimal to the expected base.

            Base-10 to Base-n Conversion Algorithm:
                1. Assign value of object's initial value to "temp"
                2. Find the remainder of temp's division by output_base and append to the converted
                3. Assign value of temp's integer division by output_base to itself
                4. Repeat until the value of temp is 0
                5. Return value of reversed "converted" string
        '''
        temp = decimal_value
        converted = ''
        while temp != 0:
            converted += str(temp % output_base)  # Convert result of modulo to string so it can be concatenated.
            temp //= output_base
        return converted[::-1]
