#Files and Exceptions

#refer to file_reader.py

#Writing to an Empty File

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    #the 'w' tells Python that we want to write to the file.
    #u can also open a file in readmode with 'r' and append mode with 'a' or..
    #read and write mode represented as 'r+'
    #be careful with the 'w' as it can erase the contents of an existing file.
    file_object.write("I love programming.\n")
    file_object.write('I love creating new games.\n')

#Appending to a File
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n") 