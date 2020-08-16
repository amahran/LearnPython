import datetime

# Print the task name and the current time
def test(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

# Get the first letter from a name
def get_initial(name):
    return name[0:1].upper() # Start at position 0 and count 1 letter => extract the first letter

first_name = 'Alaa'
test('intialization')


for x in range(1,10):
    print (x)
test('For Loop completed')

first_name = input('Enter your first name: ')
second_name = input('Enter your second name: ')

print ('Your Initials are: '    \
    + get_initial(first_name)   \
    + get_initial(second_name))