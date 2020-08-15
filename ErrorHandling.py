from datetime import datetime

birthday = input('What is your birthday (dd/mm/yyyy)? ')

try:
    # creates a datetime object from the given string.
    birthday_date = datetime.strptime(birthday, '%d/%m/%Y') # strip time out of a string
    print('Birthday: ' + str(birthday_date))
except:
    print('Please enter a valid date format as indicated!')
finally:
    print('This will run whatever try was successful or failed')
