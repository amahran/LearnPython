# Lambdas is a sort of inline functions 
# Used for example when you pass a function pointer to the sort function 
# WIKIPEDIA: In computer programming, an anonymous function (function literal, lambda abstraction, or lambda expression) 
#            is a function definition that is not bound to an identifier.
print()

# Callback for the sort function (Which called the key parameter)
# The sort function is calling this function for each item in the list before comparison
def sorter(item):
    return item['age']

family = [
    {'name': 'Alaa', 'age': 30},
    {'name': 'Hisham', 'age': 26}
]

family.sort(key=sorter)
print(family)

print()

# another way to do it is using Lambda functions 
family.sort(key=lambda item: item['name']) # Here item is the parameter list, and item[] is the return 
print(family)

print()

family.sort(key=lambda item: len(item['name'])) # sort by the length of the name
print(family)

print()