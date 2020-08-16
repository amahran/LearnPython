##### For loops => No condition can be specified ##########
for name in ['Alaa', 'Hisham']: # Loop on a list of items
    print (name)


# To loop a certain number of times
for index in range(0, 2): # range will automatically create array of [0, 1]
    print(index)

###### While loops => Looping with condition #########
names = ['Alaa', 'Hisham']
index = 0
while index < len(names): # condition
    print(names[index])
    index = index + 1

