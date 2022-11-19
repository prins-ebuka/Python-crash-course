#Exercise 7-4
prompt = 'Enter a pizza topping.'
prompt += "\nEnter 'quit' to end the program."

while True:
    toppings = input(prompt)

    if toppings != 'quit':
        print(f"I'll add {toppings} to your pizza.")
    else:
        break

#Exercise 7-5
prompt = 'Enter your age'
prompt += "\nEnter 'quit' to end the program."

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age == int(age)

    if age < 3:
        print('Your ticket is free.')
    elif age <= 12:
        print('Your ticket is $10.')
    elif age >= 13:
        print('Your ticket is $15.')

#Example 7-8
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I am working on your {current_sandwich} sandwich')
    finished_sandwiches.append(current_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print(f'I made a {finished_sandwiches} sandwich.')  
    


    

