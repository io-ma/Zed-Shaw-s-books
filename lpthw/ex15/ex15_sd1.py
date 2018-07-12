# imports feature argv from module sys
from sys import argv

# sets script and filename as argv
script, filename = argv

# opens the file and assigns it to variable txt
txt = open(filename)

# prints a string that contains the filename
print(f"Here's your file {filename}:")
# prints the contents of the file
print(txt.read())

# asks the user to type the filename again
print("Type the filename again:")
# assigns the answer of the input to variable file_again
file_again = input("> ")

# opens file again and assign the content to variable txt_again
txt_again = open(file_again)

# reads and prints the content of the file again
print(txt_again.read())