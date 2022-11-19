#Tuples
#A tuple is simply a list that cannot change. 
#The difference is that a Tuple uses a parentheses while a List uses square brackets
#Same rules of indexing and others applicable to a List is also applicable to a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

#dimensions[0] = 250
#print(dimensions)

#Tuples are technically defined by a comma. 
#Let's make a one element tuple
my_t = (3,)
print(my_t)
print(my_t[0])

#Writing over a tuple
#This assigns a new value to a variable that represents a tuple
dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)    
#notice that we re-assigned a variable    