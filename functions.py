"""
functions.py: demonastrate function usage
"""
import datetime


def test(task_name):
    """ Print the task name and the current time """
    print(task_name)
    print(datetime.datetime.now())
    #print ()



def get_initial(name, force_uppercase=True):
    '''
    Get the first letter from a name
    '''
    initial = name[0:1] # Start at position 0 and count 1 letter => extract the first letter

    if force_uppercase:
        initial = initial.upper()

    return initial

FIRST_NAME = 'Alaa'
test('intialization')


for x in range(1, 10):
    print(x)
test('For Loop completed')

first_name = input('Enter your first name: ')
second_name = input('Enter your second name: ')

print('Your Initials are: '    \
    + get_initial(first_name)   \
    + get_initial(force_uppercase=False, name=second_name))
    # Use always for readability (name notation)
