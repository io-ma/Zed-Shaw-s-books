# sets the file name to the first argument 
filename = ARGV.first

# opens a file and sets this action to txt variable
txt = open(filename)
# writes a string that contains the filename
puts "Here's your file #{filename}:"
# displays the content of the file
print txt.read
txt.close
# asks the user to type the filename again
print "Type the filename again: "
# sets file_again to user's answer
file_again = $stdin.gets.chomp
# sets txt_again to opening the file_again file
txt_again = open(file_again)
# displays the content of the txt_again opened file
print txt_again.read
txt_again.close