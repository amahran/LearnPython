price = input("Enter the price! ")

print ()

###### If statements #######
# Take care of indentations and the colons
if float(price) > 1.00:
    tax = 0.07
    print (tax)
else:
    tax = 0
    print (tax)

print ()

###### Nested If statements #######
country = 'CANADA'
if country.lower() == 'canada': # Avoids inputs cause comparison to fail due to case sensitive
    print ('A canadian is here')
elif country.lower() == 'egypt':
    print ('Hight Pharaoh')
else:
    print ('You are not from a canada')

print()

country = input('Where are you from? ')

######### 'or' condition #######
if country.lower() == 'egypt' \
    or country.lower() == 'usa':
    print ('Hi you')
else:
    print ('Go away')

######### Another was for or condition #######
if country.lower() in('egypt', \
                       'usa'):
    print ('Hi again!')
else:
    print()

print()

######### Check against != false #######
flag = False

if flag:
    print ('All good')
else:
    print ('No good')