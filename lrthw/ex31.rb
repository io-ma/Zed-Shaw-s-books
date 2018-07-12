puts "You enter a dark room with five doors. Do you go through door #1, door #2, door #3, door #4 or door #5?"

print "> "
door = $stdin.gets.chomp

if door == "1"
    puts "There's a giant bear here eating a cheese cake. What do you do?"
    puts "1. Take the cake."
    puts "2. Scream at the bear."

    print "> "
    bear = $stdin.gets.chomp

    if bear == "1"
        puts "The bear eats your face off.  Good job!"
    elsif bear == "2"
        puts "The bear eats your legs off.  Good job!"
    else 
        puts "Well, doing %s is probably better. Bear runs away." % bear 
    end

elsif door == "2"
    puts "You stare into the endless abyss at Cthulhu's retina."
    puts "1. Blueberries."
    puts "2. Yellow jacket clothespins."
    puts "3. Understanding revolvers yelling melodies."

    print "> "
    insanity = $stdin.gets.chomp

    if insanity == "1" || insanity == "2"
        puts "Your body survives powered by a mind of jello. Good job!"
    else 
        puts "The insanity rots your eyes into a pool of muck. Good job!"
    end

elsif door == "3"
    puts "You are afraid of a ghost. You now:"
    puts "1. Call a ghost hunter."
    puts "2. Die of heart attack."

    print "> "
    response = $stdin.gets.chomp

    if response == "1" 
        puts "This is the right way to survive."
    else
        puts "Goodbye. Nice to meet you."
    end

elsif door == "4"
    puts "There's a lion in the room. You can:"
    puts "1. Feed him chicken."
    puts "2. Feed him biscuits."
    puts "3. Feed him cake."

    print "> "
    answer = $stdin.gets.chomp

    if answer == "1"
        puts "Lion happy. You can rest on the bed."
    elsif answer == "2"
        puts "Lion hungry. Run!"
    else
        puts "Lion hungry. You skipped a meal!"
    end

else
    puts "You stumble around and fail on a knife and die. Good job!"
end