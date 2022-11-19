#User Input and While Loops
#The use of the input() function and the while loop

message = input('Tell me something and I will repeat it back to you:')
print(message)

name = input('Please enter your name:')
print(f"\nHello, {name}!")

print(f"\n{message},{name}.")

prompt = 'if you tell us who you are, we can personalise the messages you see.'
prompt += '\nWhat is your first name?'

name = input(prompt)
print(f'\nHello, {name}!')

#Using the int() function to accept numerical input
age = input('What is your age?')
age = (int(age))

print(age >= 18)
#the input() function by defaults take every input as a string. Therefore the integer function here helps it specify that it is a numerical value.


#eg 2
height = input('How tall are you in inches?')
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#The Modulo Operator
#Divides and returns the remainder
print(4 % 3)

number = input("Enter a number and I'll tell you whether it is even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#Try it yourself
message = input('What can do you want?')

print(f"Let me see if I can find you a {message}.")

#Introducing the While loop
#Where the for loop runs once for each item in a collection, the while loop runs as long as, or while, a certain condition is true.
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Letting the user choose when to Quit
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#Using a Flag.
#A Flag is used to avoid using various True statements in a program and instead defining the True statement once.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


