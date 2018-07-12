# sets the first argument to a variable called input_file
input_file = ARGV.first
# defines a function called print_all, takes f as argument
def print_all(f)
    # writes the file content after reading it
    puts f.read
# ends the function
end

# defines a function called rewind, takes a file object as a parameter
def rewind(f)
    # seeks position 0 in the file ( the beginning of the file)
    f.seek(0)
# ends the function
end

# defines a function called print_a_line that takes as arguments line_count and f
def print_a_line(line_count, f)
    # writes the line number , the next line removing the /n 
    puts "#{line_count}, #{f.gets.chomp}"
#end function
end

# opens the input_file and assigns it to current_file
current_file = open(input_file)
# writes the sentence: First let's print the whole file and adds a new line
puts "First let's print the whole file:\n"
# calls the print_all function with the current_file as argument
print_all(current_file)
# writes a string that explains what rewind should do
puts "Now let's rewind, kind of like a tape."
# calls the rewind function
rewind(current_file)
# writes a string that anounces we will print three lines
puts "Let's print three lines:"
# assigns 1 to the first argument, current_line
current_line = 1
# calls the function print_a_line with current_line and current_file as arguments 
print_a_line(current_line, current_file)
# adds current_line to 1, so current_line becomes 2
current_line += 1
# calls the function print_a_line again with current_line and current_file as arguments
print_a_line(current_line, current_file)
# adds current_line to 1 , so current_line becomes 3
current_line += 1
# calls the function print_a_line with current_line and current_file as arguments
print_a_line(current_line, current_file)