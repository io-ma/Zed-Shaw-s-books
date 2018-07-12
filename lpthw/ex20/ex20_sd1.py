# imports package argv from module sys
from sys import argv

# sets script and input_file as argument variables
script, input_file = argv

# function print_all takes f as argument
def print_all(f):
    # prints the content of f
    print(f.read())

# function rewind takes f as argument
def rewind(f):
    # calls seek method on f and seeks from 0
    f.seek(0)
# function print_a_line takes line_count and f as arguments
def print_a_line(line_count, f):
    # prints line_count and calls readline method on f
    print(line_count, f.readline())

# opens input_file and assigns it to current_file
current_file = open(input_file)

# prints astring and a new line
print("First let's print the whole file:\n")

# calls print_all function and gives it current_file as argument
print_all(current_file)

# prints a string about rewinding like a tape
print("Now let's rewind, kind of like a tape.")

# calls function rewind, gives it argument current_file
rewind(current_file)

# prints a string
print("Let's print three lines:")

# assigns 1 to variable current_line
current_line = 1
# calls print_a_line with arguments current_line and current_file
print_a_line(current_line, current_file)

# adds a 1 to current_line
current_line = current_line + 1
# calls print_a_line function with arguments current_line and current_file
print_a_line(current_line, current_file)

# adds a 1 to current_line
current_line = current_line + 1
# calls print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)