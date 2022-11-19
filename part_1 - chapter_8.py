#Functions
import re


def greet_user():
    """Display a simple greeting."""
    print('Hello!')

greet_user()

#Passing information to a Function 
def greet_user(username):
    '''Display a simple greeting.'''
    print(f'Hello, {username.title()}!')

greet_user('ebuka')

#Passing arguments 
#Positional arguments and Keyword arguments
#Positional arguments
def describe_pet(animal_type, pet_name):
    '''Display information about a pet'''
    print(f'I have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog',"willie")
#Remember that order matters in a positional call

#Keyword Arguments
#It is a name-value pair that you pass to a function
def describe_pet(animal_type, pet_name):
    '''Display information about a pet'''
    print(f'I have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#Default Values
def describe_pet(pet_name, animal_type='dog'):
    '''Display information about a pet'''
    print(f'I have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

#Equivalent Function Calls
def describe_pet(pet_name, animal_type='dog'):
    '''Display information about a pet'''
    print(f'I have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="harry", animal_type="hamster")

#Try it yourself
def make_shirt(size):
    """Define the size of the shirt and the message printed on it"""
    print(f"The size of the shirt is {size}.")
    print("That is the size of the shirt you are wearing.")

make_shirt(8)

#Return Values
#A function doesn't have to display its output directly. Instead, it can process some data...
#and then return a value or set of values. The value the function returns is called the RETURN VALUE.
#The return statement takes a value from inside a function and sends it back to the line that called the function.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
#When you call a function that returns a value, you need to provide a variable that the return...
#value can be assigned to. In this case, the return value is assigned to variable musician.

#Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hooker', 'lee')
print(musician)

#Returning a Dictionary
#A function can return any value you want including more complicated data structures like a dictionaryn and lists
def build_person(first_name, last_name):
    '''Return a Dictionary of information about a person'''
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

#Let us extend the earlier definition
def build_person(first_name, last_name, age=None):
    """Return a Dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#Using a Function with a while loop
#You can use a Function with all the Python structures you've learnt about so far
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is an infinite loop!
while True:
    print('\nPlease tell me your name:')
    print("Enter 'q' at anytime to quit")

    f_name = input('First name:')
    if f_name == 'q':
        break

    l_name = input('Last name:')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")

#Try it yourself
def city_country(city, country):
    '''Return the name of a city and its country'''
    city_name = f"{city}, {country}"
    return city_name.title()

city_details = city_country('abuja', 'nigeria')
print(city_details)
city_details = city_country('lagos','nigeria')
print(city_details)

#Try it yourself 8-7
def make_album(artist, album_title, number=None):
    """Return an artist and his album title"""
    person = {'artist': artist, 'album': album_title}
    if number:
        person['number'] = number
    return person

artiste = make_album('Wizkid', 'Go slowly')
print(artiste)
artiste =make_album('Wizkid', 'Go slowly', 9)
print(artiste)

while True:
    print('Tell me the artiste details:')
    print("At anytime, enter 'q' to end the program.")

    art = input('Enter the artiste name')
    if art == 'q':
        break
    al = input('Enter the artist album:')
    if al == 'q':
        break
    num = input('Enter the number of songs:')
    if num == 'q':
        break

    artit = f"{art, al, num}"
    print(artit)


