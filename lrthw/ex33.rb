i = 0 
numbers = []

while i < 6
    puts "At the top i is #{i}"
    numbers.push(i)

    i += 1
    puts "Numbers now: ", numbers
    puts "At the bottom i is #{i}"
end

puts "The numbers: "

# remember you can write this 2 other ways?
numbers.each {|num| puts num }
# numbers.each do |number|
#    puts number
# end

# for number in numbers
#    puts number
# end

def loop(number, nr)
    i = 0
    numbers = []
    while i < number
        puts "At the top i is #{i}"
        numbers.push(i)
        i += nr
        puts "Numbers now: ", numbers
        puts "At the bottom i is #{i}"
    end
    puts "The numbers: "
    numbers.each {|num| puts num }
end

loop(75, 87)
loop(987, 1098)

def range(incr, up_limit)
    numbers = []
    for nmbr in (incr..up_limit)
        puts "The number is #{nmbr}"
        numbers.push(nmbr)
    end
    puts "The numbers: "
    
    for nmbr in numbers
        puts nmbr
    end
end

range(3, 9)
