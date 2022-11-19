message = 'Hello Python world'
print(message)

message = 'Hello Python Crash Course World'
print(message)

mesage = "Hello Python Crash Course reader!"
print(mesage)

name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

#Using Variables in Strings
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)
print(f'Hello, {full_name.title()}!')

#Adding Whitespace to strings with tabs and Newlines
#Whitespace is simply nonprinting characters in Python
#We will first add a tab with \t
print('Python')
print('\tPython')
#Let us look at adding a newline to a string represented with \n
print('Languages:\nPython\nC\nJavascript')
#We can also print tabs and newlines together
print('Languages:\n\tPython\n\tC\n\tJavascript')

#Stripping Whitespaces
#To strip whitespaces on the right, use the rstrip() method
favourite_language = 'python '
print(favourite_language)
print(favourite_language.rstrip())
#to remove the whitespace from the string permanently, you have to associate the stripped value with the variable name
favourite_language=favourite_language.rstrip()
print(favourite_language)

#You can also remove from the left side using the lstrip() method
#You can also eliminate whitespaces from both sides using the strip() method
favourite_language = ' python '
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

#Numbers
print(3/2)
print(0.2+0.1)
print(3*0.1)
universe_age = 14_000_000_000
print(universe_age)

#Constants
#Constants are variable names that stays the same throughout the program
#it is done by capitalizing the variable name. Eg...
MAX_CONNECTIONS = 5000

import this



