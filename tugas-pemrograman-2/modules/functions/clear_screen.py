import os, sys

def clear_screen():
    ''' This function is used to clear the screen when necessary '''
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')