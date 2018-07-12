print("""You are in the forest.
You have no ideea what mushrooms are poisonous.
You pick the #1 red ones or the #2 purple ones?""")

mushrooms = input("> ")

if mushrooms == "1":
    print("Among the two red mushrooms only 1 is edible")
    print("Which one you choose?")
    print("1. The smaller one.")
    print("2. The bigger one.")

    red = input("> ")
    
    if red == "1":
        print("This is the safe mushroom. Go for it!")
        print("You're safe!")
    elif red == "2":
        print("You better stay away.It looks good, but it smells bad.")
        print("You die!")
    else:
        print("No way, not an option!")

elif mushrooms == "2":
    print("All the violet mushrooms are poisonous.")
    print("Seriously? Good bye, your life was short.")
    
else:
    print("Not an option. Choose #1 or #2.")
    
