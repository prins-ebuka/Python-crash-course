#Exceptions are handled with the try-except block

#Handling the ZeroDivisionError

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by Zero.")

#Using Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
    #we will have a traceback if we divide by 0

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!")
    else:
        print(answer)
    #we put the try-except block on the line that we expect the error which is the division

#Handling the FileNotFoundError Exception
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} does not exist.")

#Analyzing Text
title = 'Python for Data Analysis_Data Wrangling with Pandas, Numpy, and IPython.pdf'

print(title.split())

try:
    with open(title, encoding='utf 8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {title} does not exist.")
else:
    #Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {title} has about {num_words} words.") 

#Working with Multiple Files

#Failing Silently
#the use of the 'pass' keyword
#the pass is a placeholder, reminding your code to do nothing at a specific point in your program's execution
