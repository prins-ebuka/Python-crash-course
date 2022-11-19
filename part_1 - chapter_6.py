#DICTIONARIES
#They are used to connect pieces of information, used to store any two kind of information that can be matched up

alien_0 = {'colour':'green','points': 5}

print(alien_0['colour'])
print(alien_0['points'])

#Accessing values in a Dictionary
new_points = alien_0['points']
print(f'You just earned {new_points} points')

#Adding new Key-Value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Starting with an empty dictionary
alien_0 = {}

alien_0['colour'] = 'green'
alien_0 ['points'] = 5

print(alien_0)

#Modifying 'values' in a dictionary
#This is done in the same way of changing the variable value of a scalr data type
alien_0 = {'colour':'green'}
print(f"The alien is {alien_0['colour']}.")

alien_0['colour'] = 'yellow'
print(f"The alien is now {alien_0['colour']}.")

#Example 2 on modifying 'values'
alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}.")

#Move the alien to the right
#Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#Removing Key-Value pairs
#The use of del statement
alien_0 = {'colour':'green','points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#Dictionary of similar objects
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

#Using the get() method to access values
#in using the get method, the first parameter is the key, the second is what to return if the key does not exist in the dictionary

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points','No point value assigned')
print(point_value)


#Looping through a dictionary
#u can loop through the key-value pair, through its keys or thrpough its values
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'femi'
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
#the variable key,value represents the key and the value respectively. NB: this can be any variable
#the items method returns a list of key-value pairs

favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

#Looping through all the keys in a dictionary
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }

for name in favourite_languages.keys():
    print(name.title())


friends = ['phil', 'sarah']
for name in favourite_languages:
    print(name.title())

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")