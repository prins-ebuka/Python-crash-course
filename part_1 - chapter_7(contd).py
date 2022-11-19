#Using break to Exit a Loop
#This is used to exit a while loop immediately without running any remaining code in the...
#loop, regardless of the results of any conditional test
#The break statement directs the flow of your program
# NB: You can use the break statemnt in any of Python's loops.


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#Using continue in a loop
#As compared to the break statment that ends the code entirely, the continue statement...
#returns to the beginning of the loop based on the result of a conditional test
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

#Avoiding Infinite Loops
x = 1

while x <= 5:
    print(x)
    x += 1

#Try it yourself
prompt = 'What topping would you like on your pizza?'
prompt += "\nEnter 'quit' when you are finished."

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"\tI'll add {topping} to your pizza.")
    else:
        break

#Try it yourself 2
prompt = 'Enter your age'
prompt += "\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print('Your ticket is free.')
    elif age <= 12:
        print('Your ticket is $10.')
    elif age >= 13:
        print('Your ticket is $15.')

#Using a while loop with Lists and Dictionaries
#Unlike the for loop, the while loop is better in modifying a List or Dictionary
#Example...
#Start with users that need to be verified,...
#and an empty list that needs to hold confirmed users

unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed users
#Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verfifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing all instances of Specific Values from a List
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Filling a Dictionary with User Input
responses = {}

#Set a flag to indicate that the polling is active.
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name?")
    response = input('Which mountain would you like to climb someday?')

    #Store the responses in the dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n --- Poll Results ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")

#Try it yourself
sandwich_orders = ['young','old','new','underage']

finished_sandwiches = []

while sandwich_orders:
    temps = sandwich_orders.pop()
    finished_sandwiches.append(temps)

    for temp in finished_sandwiches:
        print(f'I made your {finished_sandwiches} sandwich.')




    

    

    
        
    