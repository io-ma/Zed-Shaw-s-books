print("""You enter a dark room with 7 doors.
Choose a door from #1 to #7. """)

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Wink two times.")
    print("4. Run for my life.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("The bear winks back at you and doesn't move.")
    elif bear == "4":
        print("The bear loughs. He never saw such a coward.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
    
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("4. Hungry medusas approaching.")
    print("5. Cthulu closes one eye.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif insanity == "3" or insanity == "4":
        print("Keep quiet or you can go insane.")
        print("Good job!")
    elif insanity == "5":
        print("You are doomed. A single retina is bad luck. Your head will explode in 20 seconds.") 
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("There's Count Dracula grinning and asking you for a secret word.")
    print("You need to guess the first letter or your head is chopped off.")
    print("The word starts with:")
    print("A")
    print("B")
    print("C")
    print("D")
    print("E")
    
    letter = input("> ")

    if letter == "A" or letter == "B":
        print("Wrong.Try more.")
        print("My biggest pleasure is to see your head chopped off.")
    elif letter == "C" or letter == "D":
        print("Wrong.Try more.")
        print("My machette has been sharpen in the morning...ha ha!")
    elif letter == "E":
        print("Good job, you didn't seem so clever at first sight.")
        print("You are forgiven, your head will stay where it is.")
    else:
        print("How dare you choose another letter?! You deserve to die!")
        print("I will chop you head off! Good job!")

elif door == "4":
    print("There's a giant cat yawning.")
    print("You can only pass if you give her the right food.")
    print("1. Give her mice.")
    print("2. Give her kibble.")
    print("3. Give her pizza.")

    food = input("> ")

    if food == "1":
        print("There you go, mice is what I craved for.")
        print("You can pass.")
    elif food == "2":
        print("Kibble is for sucker dogs who obey their owners.")
        print("You won't pass.")
    elif food == "3":
        print("This pizza looks 5 years old. How about you eat it?")
    else:
        print("A cat like me would never eat such crap.")

elif door == "5":
    print("A huge spider is ready to jump on you.")
    print("You need something to scare him off.")
    print("1. You take a broom.")
    print("2. You choose a towel.")
    print("3. You use a spray.")

    tool = input("> ")

    if tool == "1":
        print("You fail at scaring me away. Good job!")
    elif tool == "2":
        print("Not scared at all. Good job!")
    elif tool == "3":
        print("Not moving anywhere. Having lunch.")
    else:
        print("Didn't expect this one. You are really good at scaring spiders!")
        print("The door is yours.")

elif door == "6":
    print("Here's a cursed mummy. If you touch it with the wrong gloves, you turn into stone.")
    print("You need a pair of special gloves to move it.")
    print("1. red gloves.")
    print("2. yellow gloves.")
    print("3. pink gloves.")

    gloves = input("> ")

    if gloves == "1":
        print("Wrong pair of gloves. You are cursed. Good job.")
    elif gloves == "2":
        print("Not the best choice. Be a stone for the next 400 years!")
    elif gloves == "3":
        print("You broke the ancient curse. The mummy will move out of your way!")
        print("Good job!")
    else:
        print("There's no such thing. Go see an eye doctor.")

elif door == "7":
    print("A slow loris sits at his desk.")
    print("Only a combo of numbers will make him move faster.")
    print("1. 1 , 3")
    print("2. 4, 6")
    
    numbers =  input("> ")

    if numbers == "1":
        print("Life is unfair. You have to wait for one month till I move.")
    elif numbers == "2":
        print("Bingo!This combo makes me faster than a lightning!")
        print("Door is free, good job!")
    else:
        print("Slow Loris is my name. Slooooow moooving is myyyy gaaaaame!")

else:
        print("You stumble around and fall on a knife and die. Good job!")