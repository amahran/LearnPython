'''
module doc string
'''

def print_hello(name: str) -> str:
    """
    Greets the user by name

    Parameters:
        name (str): the name of the user
    returns: str: The greeting
    """

    return 'Hello, ' + name

# Notice when you hover over the function name
print_hello(42)
