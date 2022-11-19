#LISTS

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = f'My first bicycle was a {bicycles[0].title()}.'
print(message)

#Modifying a List
motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements to a List
# Appending Elements to the end of a List
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserting elements in a List
motorcycles.insert(0,'ducati')
print(motorcycles)

#Removing Elements from a List
# The use of the del Statement
del(motorcycles[0])
print(motorcycles)
del(motorcycles[1])
print(motorcycles)

# The use of the pop() method
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}.')

#Popping items from any position in a list
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

#Removing an item by value
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')
#It should be noted that the remove() method only removes the first occurence of the value you specify
#to remove more than one occurence of an item, you will need to use a loop

#Organizing a List
# The use of the sort() method
cars = ['bmw','audi','toyota','subaru']
cars.sort()
#the sort() method used here arranges the item alphabetically
print(cars)

#to sort in reverse in alphabetical order, you pass the argument 'reverse=True' to the sort() method
cars.sort(reverse=True)
print(cars)

#The use of the sorted function. This function sorts a list temporarily
print('Here is the original list')
print(sorted(cars))

#The use of the reverse() method. This method is used to rearrange the chronological order in reverse 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#The use of the Length Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))