# This is to practice creating modules to be used on the other python modules

from colorama import init, Fore

init()

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)