puts "Let's practice everything."
puts 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
    
# the <<END is a "heredoc". See the Student Questions.
# multi line string
poem = <<END
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
END

puts "--------------"
puts poem 
puts "--------------"


five = 10 - 2 + 3 - 6

puts "This should be five: #{five}"

# defines the function secret_formula and takes the argument started
def secret_formula(started)
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
end 

# variable start_point 
start_point = 10000
# whatever secret_formula returns goes into the 3 vars down here:
beans, jars, crates = secret_formula(start_point)

puts "With a starting point of: #{start_point}"
puts "We'd have #{jars} beans, #{jars} jars, and #{jars} crates."

start_point = start_point / 10
puts "We can also do that this way:"
puts "We'd have %s beans, %d jars, and %d crates." % secret_formula(start_point)