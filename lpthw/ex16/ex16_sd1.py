# imports feature argv from module sys
from sys import argv

# sets script and filename as argv
script, filename = argv

# prints an f string that warns about erasing the file
print(f"We're going to erase {filename}.")
# prints a way to prevent erasing the file
print("If you don't want that, hit CTRL-C (^C).")
# ask for confirmation to erase the file
print("If you do want that, hit RETURN.")

# takes the user input on wheeter to erase the file or not
input("?")

# prints "opening the file...
print("Opening the file...")
# calls the open method on the file, in write mode and 
# assigns it to variable target
target = open(filename, 'w')

# prints a "truncating the file" message
print("Truncating the file. Goodbye!")
# calls the truncate method on the file
target.truncate()

# prints a message to ask user for three lines
print("Now I'm going to ask you for three lines.")

# takes the input ffrom the user for the first line
# and assign it to the variable line1
line1 = input("line 1: ")
# takes the input ffrom the user for the second line
# and assign it to the variable line2
line2 = input("line 2: ")
# takes the input ffrom the user for the third line
# and assign it to the variable line3
line3 = input("line 3: ")

# prints it will write these lines to the file
print("I'm going to write these to the file.")

# calls write method on the file and writes the first line
target.write(line1)
# calls write method on the file and writes a new line
target.write("\n")
# calls write method on the file and writes the second line
target.write(line2)
# calls write method on the file and writes a new line
target.write("\n")
# calls write method on the file and writes the third line
target.write(line3)
# calls write methof on the file and writes a new line
target.write("\n")

# prints a warning that the file will be closed
print("And finally, we close it.")
# calls the close method on the file
target.close()