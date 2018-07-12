def add(a, b)
    puts "ADDING #{a} + #{b}"
    return a + b
end

def substract(a, b)
    puts "SUBSTRACTING #{a} - #{b}"
    return a - b 
end

def multiply(a, b)
    puts "MULTIPLYING #{a} * #{b}"
    return a * b 
end

def divide(a, b)
    puts "DIVIDING #{a} / #{b}"
    return a / b 
end 


puts "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

puts "Age: #{age}, Height: #{height}, Weight: #{weight}, IQ: #{iq}"


# A puzzle for the extra credit, type it in anyway.
puts "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

puts "That becomes: #{what}. Can you do it by hand?"

# study drills
# 2
what = age + (height - (iq/2) * weight)
# 3
new_what = add(age, substract(multiply(weight, divide(iq, 2)), height))
puts "That becomes: #{new_what}. Yes, I can do it by hand, but I'd rather let the computer do the math."
# 4
my_formula = weight - (height + (age * iq/3))
puts " This now becomes: #{my_formula}. Hope it works."