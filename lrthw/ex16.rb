filename = ARGV.first

puts "We're going to erase #{filename}"
puts "If you don't want that, hit CTRL-C (^C)."
puts "If you do want that, hit RETURN."

$stdin.gets

puts "Opening the file..."
target = open(filename, 'w')

puts "Truncating the file.  Goodbye!"
target.truncate(0)

puts "Now I'm going to ask you for three lines."

print "line 1: "
line1 = $stdin.gets.chomp
print "line 2: "
line2 = $stdin.gets.chomp
print "line 3: "
line3 = $stdin.gets.chomp

puts "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

puts "And finally, we close it."
target.close

# study drills

# 2.
text = open(filename)
puts "This is your file #{filename}:"
print text.read
text.close

# 3
puts "Opening the file again..."
t = open(filename, "w+")
t.write("line 1: #{line1}\nline 2: #{line2}\nline 3: #{line3}\n")
puts "Look at your file #{filename}:"
print t.read
t.close
