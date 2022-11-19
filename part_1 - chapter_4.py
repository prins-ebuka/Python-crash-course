#WORKING WITH LISTS

magicians = ['alice','david','carolina','alice']
for magician in magicians:
    print(magician)
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print('Thank you, everyone. That was a great magic show!\n')

#Try it yourself - Pizza test
pizzas = ['surelere pizza','lawanson pizza','yaba pizza']
for pizza in pizzas:
    print(pizza)
    print(f'I like {pizza}')
print('I love pizza so much!\n')

#Try it yourself - Favourite animals
animals = ['dog','cat','rabbit']
for animal in animals:
    print(animal)
    print(f'{animal} would make a pretty pet\n')
print('Any of these animals would make a great pet!\n')

#Numerical Lists
# The use of the range() function: It is used to generate a series of numbers
for value in range(1,5):
    print(value)

print()

for value in range(6):
    print(value)
#this starts printing from 0 to 5 and obeys the off-by-one behaviour

#Using range() to make a List of Numbers in conjunction with the list() function
numbers = list(range(1,6))
print(numbers)

print()

#use of the step
even_numbers = list(range(2,11,2))
print(even_numbers)

print()

# the range function is powerful and can even be used to get the square of the first 10 integers
squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)
    #better is squares.append(value**2)

print(squares)

#Simple statistic with a list of numbers. The use of min, max and sum
digits = list(range(10))
print(max(digits))
print(min(digits))
print(sum(digits))

print()

#List Comprehension
#pay attention as this is not usually presented to beginners
#remember the square of a list we earlier created, we can compress it into one line of code
squares = [value**2 for value in range(1,11)]
print(squares)

print()

#Try it yourself
numbers = [value for value in range(1,21)]
print(numbers)

numbers = []
for value in range(1,21):
    numbers.append(value)
    #print(numbers) this iterates the whole output to form a triangle like shape
print(numbers)

#millions = [figure for figure in range(1,1_000_001)]
#print(millions)
#print(sum(millions))

#millions = []
#for figure in range(1,1_000_001):
#    millions.append(figure)
#print(millions)

odd_numbers = [odd for odd in range(1,20,2)]
print(odd_numbers)

cubes = [cube**3 for cube in range(1,11)]
print(cubes)


#Working with Parts of a List
#Slicing a list

players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print('Here are the first three players of my team:')
for player in players[:3]:
    print(player.title())


#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] 
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('my favourite foods are:')
print(my_foods)
print(friend_foods)


