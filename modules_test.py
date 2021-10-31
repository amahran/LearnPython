'''
This is to test how to import a module
'''

############ Method 1: Import module as namespace
import helpers
helpers.display('Not a warning')

############ Method 2: Import all into current namespace
from helpers import *
display('Not a warning')

############ Method 3: Import specific items into current namespace
from helpers import display
display('Not a warning')
