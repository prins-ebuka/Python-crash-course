with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

#Notice that the open function has only one argument, the name of the file you want opened
#the with closes the file once access to it is no longer required
#after Python opens the txt file, it assigns it to an object, here we use file_object
#the read method reads the entire content of the file

#File Paths
filename = '/home/ecihekwereme/Other_files/file1.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents)


#Reading Line by Line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

#there was an invisible newline in the character above
#let us use the rstrip() method
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#Making a List of Lines from a File
#This is used to work with the line outside the with block
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    #the readlines() method takes the line from a file and stores it in a list.

for line in lines:
    print(line.rstrip())

#Working with a File's Contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#Large Files: One Million Digits
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

