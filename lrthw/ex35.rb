# starts the game 
def start 
    puts "You are in a dark room."
    puts "There is a door to your right and left."
    puts "Which one do you take?"

    print "> "
    choice = $stdin.gets.chomp
# evaluates the choice, if left goes to bear_room
    if choice == "left"
        bear_room
# if choice == right, goes to cthulhu_room
    elsif choice == "right"
        cthulhu_room
# if anything else, you starve
    else
        dead("You stumble around the room until you starve.")
    end
end

# bear room
def bear_room
    puts "There is a bear here."
    puts "The bear has a bunch of honey."
    puts "The fat bear is in front of another door."
    puts "How are you going to move the bear?"
    puts "take honey"
    puts "taunt bear"
    puts "open door"
    # bear is there
    bear_moved = false

    while true
        print "> "
        choice = $stdin.gets.chomp

        if choice == "take honey"
            dead("The bear looks at you then slaps your face off.")
        elsif choice == "taunt bear" && !bear_moved
            puts "The bear has moved from the door. You can go through it now."
            # moves bear
            bear_moved = true
        elsif choice == "taunt bear" && bear_moved
            dead("The bear gets pissed off and chews your leg off.")
            # if open door and bear has moved, go to gold_room
        elsif choice == "open door" && bear_moved
            gold_room
        else 
            puts "I got no idea what that means."
        end
    end
end

def gold_room
    puts "This room is full of gold. How much do you take?"

    print "> "
    choice = $stdin.gets.chomp

    # choice has to be equal to or greater than 0
    if choice >= "0"
        how_much = choice.to_i
    else
        dead("Man, learn to type a number.")
    end

    if how_much < 50
        puts "Nice, you're not greedy, you win!"
        exit(0)
    else 
        dead("You greedy bastard!")
    end
end
# defines the why argument
def dead(why)
    puts why, "Good job!"
    exit(0)
end

def cthulhu_room
    puts "Here you see the great evil Chtulu."
    puts "He, it, whatever stares at you and you go insane."
    puts "Do you flee for your life or eat your head?"

    print "> "
    choice = $stdin.gets.chomp

# verifies if choice includes the word "flee"
    if choice.include? "flee"
        start
# verifies if choice includes the word "head"
    elsif choice.include? "head"
        # the why argument of dead function changes
        dead("Well that was tasty!")
# studdy drill 4
    else
# replaced cthulhu_room with gold_room so the user can get the chance to play the game forward
        gold_room
    end
end
# calls the start function
start
