print "How old are you? "
age = gets.chomp
print "How tall are you? "
height = gets.chomp
print "How much do you weigh? "
weight = gets.chomp

puts "So, you're #{age} old, #{height} tall and #{weight} heavy"

# study drills

# input variables
name = ""
years = 0
MONTHS_PER_YEAR = 12 # a constant

# output variable
months = 0

# processing
print "What is your name? "
name = gets

months = years * MONTHS_PER_YEAR

puts "#{name}, at #{years} years old, "\
  "you are #{months} months old."