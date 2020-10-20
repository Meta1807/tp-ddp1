import sys
import os

def clear_screen():
    ''' Executes a shell command to clear screen (Implemented so that it will be OS-aware) '''
    if sys.platform == 'win32':
        os.system("cls")
    elif sys.platform in ['linux', 'darwin', 'freebsd']:
        os.system("clear")
