#Passing a List
#You can use a function to have direct access to a List
def greet_users(names):
    '''Print a simple message to each user in a list'''
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Modifying a List in a Function
def print_models(unprinted_designs, completed_modules):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_modules after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_modules.append(current_design)

def show_completed_modules(completed_modules):
    """Show all the models that was printed."""
    print("\nThe following models has been printed:")
    for completed_module in completed_modules:
        print(completed_module)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_modules = []

print_models(unprinted_designs[:], completed_modules)
#The slice notation makes a copy of the list to send to the function
show_completed_modules(completed_modules)

#Try it yourself 8-9
def show_magicians(magicians):
    """Print the name of each magician in the list"""
    for magician in magicians:
        print(magician.title())

magicians = ["ebuka","ike","kelechi"]
show_magicians(magicians)

#Remember to do Try it yourself 8-9, 8-10, 8-11

#Passing an arbitrary number of arguments
#This happens when you are not sure in advance how many arguments a function needs to accept in advance
def make_pizza(*toppings):
    #The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings
    """Print the list of toppings that has been requested."""
    print("\nMake a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make"""
    print(f"\n  Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#My code which is exactly what is in the test did not output like what is in the text

#Using Arbitrary Keyword Arguments
#Represented by the double asterisk(**), used to write functions that accept as many key-value pairs
#This is used when you anticipate a kind of information from the user but not certain about it yet
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile) 

#Try it yourself
#comeback