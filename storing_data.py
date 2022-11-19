#Storing Data

#the use of the json module

#using json.dump() and json.load()
#the json.dump() takes two arguments: a piece of data to store and a file object it can use
# to store the data

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers,f)

