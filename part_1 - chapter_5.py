#If Statements
#Python's if statement allows you to examine the current state of a program and respond appropriately to that state.

cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Conditional Tests
# Checking for equality
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'Audi')
print(car.title() == 'Audi')

#Checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies')

#Numerical comparisons
age = 18
print(age==18)

answer = 17
if answer != 42:
    print('This is not the correct answer. Please try again!')

#Checking Multiple conditions. The use of 'and' and 'or' keywords
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 and age_1 >= 21)

#Checking whether a value is in a List
#The use of the keyword 'in' and 'not in'
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#not in
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')

#Boolean Expressions
#Another name for a conditional test
game_active = True
print(game_active)

#Try it yourself
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car =='subaru')

#if Statements
#Simple if Statements: one test, one action
#eg if conditional_test:
#       do something
age = 19
if age >= 18:
    print('You are old enough to vote')
    print('Have you registered to vote yet?')

#if-else Statements
age = 17
if age >= 18:
    print('You are old enough to vote')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as you turn 18!')

#if-elif-else Statements
#You want to test more than two possible situations, and to evaluate them
age = 12
if age < 4:
    print('Your admission cost is $0')
elif age < 18:
    print('Your admission cost is £25')
else:
    print('Your admission cost is $40')

#specific test on the else block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is ${price}.')

#Multiple elif blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f'Your admission cost is ${price}.')

#Omitting the else Block
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'Your admission cost is ${price}')

#Testing Multiple Conditions
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print('\nFinished making your pizza')

#Try it yourself
alien_colour = 'red'

if alien_colour == 'green':
    print('The player just earned 5 points') 
elif alien_colour == 'yellow':
    print('The player earned 10 points')
else:
        print('The player just earned 15 points')
       
#Using the if statement with lists
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')

print('\nFinished making your pizza!')

#What if we run out of green peppers?
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}.')

print('\nFinished making your pizza!')

#Checking that a List is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
#python returns True if a list contains at least one item and returns False for an empty list


#Using Multiple lists
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni', 'pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry, we don't have {requested_topping}")

print('\nFinished making your pizza!')

#Try it yourself
usernames = ['ebuks','ikye','kelzi','chinbees','admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else:
    print('We need to find some users!')

#Try it yourself
current_users = ['ebuks','ikye','kelzi','chinbees','admin']
new_users = ['Ebuks','tessy','mon ami','ikye','joe']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Enter a new username')
    else:
        print('The username is available')

