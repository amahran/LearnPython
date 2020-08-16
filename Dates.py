# to get current date and time
# datatime lib has to be imported
from datetime import datetime, timedelta

current_date = datetime.now() # return a datetime object
print('Today is ' + str(current_date))

# time delta isuse dto define a period of time
one_day = timedelta(days=1)
print (one_day)
yesterday = current_date - one_day
print ('Yesterday was: ' + str(yesterday)) 

# Picking up the information we need
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

############# more functions
birthday = input('What is your birthday (dd/mm/yyyy)? ')
# creates a datetime object from the given string.
birthday_date = datetime.strptime(birthday, '%d/%m/%Y') # strip time out of a string
print('Birthday: ' + str(birthday_date)) 