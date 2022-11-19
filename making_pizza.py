import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
#To call a function from an imported module, enter the name of the module you imported, pizza,...
#followed by the name of the function, make_pizza(), seperated by a dot.

#Importing specific functions
# the general syntax is from module_name import function_name

#Using as to Give a Function an Alias
# from pizza import make_pizza as mp

#Using as to Give a Module an Alias
# You can also provide an alias for a module name
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Importing all Functions in a Module
#the use of the (*) operator