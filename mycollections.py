# By collectios you can create arrays, lists and so on

########### Lists => Store anything, store any type ################
names = ['Alaa', 'Hisham'] # [] for creating lists
scores = []

scores.append(98) # Add new item to the end
scores.append(99)
names.append('Hossam')
scores.append(95)

print (names)
print(scores)
print(scores[1])

# Common operations on lists
print(len(names)) # Get number of items inside the list
names.insert(0, 'Hazem') # insert the specified string into place 0 and shift the rest
print(len(names))
print(names)
names.sort()
print(names)

greplist = names[1:3] # grep these items from the list including the start idx but not the end idx 
                      # also with [:3] => grap from 0 to 2
print(greplist)

print()

########### Arrays => Numeric datatypes, must all be the same type ################
from array import array
new_scores = array('d') # 'd' is indicating the numeric datatype of the array elements => 'd' means double
new_scores.append(97)
new_scores.append(89)
print(new_scores)
print(new_scores[1])


print()

########### Dictionaries => key-value pairs (key here is the replacement of numeric index) ################
#### Unlike lists the order is not gurnteed, some libs give the options for order gurntee ####
person = {'first': 'Alaa', 'second': 'Hisham'}
person['last'] = 'Hossam' # in [] the key is specified and the value after the = sign
print(person)
print(person['second'])

print()

##Lists of dictionaries
people = [{
    'first': 'Bill', 'last': 'Gates'
},
{
    'first': 'Warner', 'last': 'Buffet'
}]

print(people[1]['last'])
