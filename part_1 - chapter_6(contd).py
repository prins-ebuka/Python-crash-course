favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }
    
friends = ['phil', 'sarah']
for name in favourite_languages:
    print(name.title())

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#eg 3
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }

if 'erin' not in favourite_languages:
    print('Erin, please take our poll!')

#Looping through a Dictionary's Keys in a Particular Order 
#The use of the sorted() function
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping through values in a Dictionary
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

#Building a set. I don't understand the book clearly
#from my little understanding this is used to avoid duplicates in a list
languages = {'python','ruby','python','c'}
print(languages)

#Try it yourself
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
    }

users = ['jen','ebuks','sarah','eddy','phil']
for user in users:
    if user not in favourite_languages:
        print(f'{user.title()}, you are invited to take the survey')
    elif user in favourite_languages:
        print(f'{user.title()}, thanks for responding.')

#Nesting
#storing multiple dictionaries in a list, or a list of items as a value in a dictionary is called NESTING
alien_0 = {'colour':'green', 'points': 5}
alien_1 = {'colour':'yellow', 'points': 10}
alien_2 = {'colour':'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#using the range and len function in nesting
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour':'green','points': 5,'speed':'slow'}
    aliens.append(new_alien)

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print('...')

#Show how many aliens have been created.
print(f'Total number of aliens: {len(aliens)}')

#List of dictionaries
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour':'green','points': 5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print(aliens[:5])

#A List in a Dictionary. This is preferable than having a Dictionary in a List
pizza = {'crust': 'thick',
        'toppings': ['mushrooms','extra cheese'],
        }

#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
#notice that the + is not printed in the output terminal

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name,languages in favourite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favourite language is {languages}.")
    else:
        print(f"{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

#A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")