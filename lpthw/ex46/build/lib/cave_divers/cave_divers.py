# choose diver
def choose_diver():
    print("""Welcome to our cave diving center. We have 3 instructors you can choose from.
    They all are quite experienced. Make a wise choice:\n\tAlex\n\tVali\n\tMike""")

    diver = input("> ")
    # alex or vali
    # alex and vali are buddies and know 3 caves only
    # if alex or vali, you see a, b, c caves
    if "Alex" in diver or "Vali" in diver:
        print("Good choice! Your life is in good hands!")
        choose_cave()
    # mike
    # if mike , he asks for pizza or more than 5000
    # pizza - you see a, b, c  caves
    # money - you get to choose among other 3 secret caves
    elif "Mike" in diver:
        print("""Hmmm, I wouldn't trust that one. He is sneakier than a serpent.
        He is a good diver though. Expect the unexpected.\nMike: For 5000 GBP I can take you to the secret caves.
        If you buy me a pizza, you get to see the normal caves.
        Where do you want to dive?""")

        cave = input("> ")

        if "secret" in cave:
            secret_caves()
        elif "normal" in cave:
            choose_cave()
        else:
            print("You can only choose a normal cave or a secret one.")
            choose_diver()

    # else
    else:
        print("Only three instructors available")
        choose_diver()

# choose cave


def choose_cave():
    print("""There are very beautiful underwater caves to explore.\nWhat is the cave you'd like to explore today?
    \n1. Izbandis\n2. Mina\n3. Bulz""")

    normal_cave = input("> ")

    if "1" in normal_cave:
        print(
            "Izbandis is quite dangerous if you are not good at cave diving.")
        choose_equipment()
        izbandis()
    elif "2" in normal_cave:
        print("Mina is very good for training your cave diving skills.")
        choose_equipment()
        mina()
    elif "3" in normal_cave:
        print("Bulz doesn't have long galleries, but it's spectacular.")
        choose_equipment()
        bulz()
    else:
        print("That's not a cave. Try again.")
        choose_cave()


def secret_caves():
    print(
        """I can show you 3 more caves! But life is short and time is money.\n Give me the 5000. You give him the money and the adventure begins.""")
    choose_equipment()

    print(
        """Mike points a gun at you: We are all alone in the equipment room. I must tell you the truth. \n Your money is lost. I am a dangerous killer hiding in this diving resort. \n You either choose to tell everyone or dive in the usual places.\n No such thing as the promised secret caves. What's your choice?""")
    secret_choice = input('> ')

    if "tell" in secret_choice:
        print("Mike shoots you.")
    elif "dive" in secret_choice:
        choose_cave()
    else:
        print("Not an option.")
        secret_caves()


def choice():
    equip_choice = input('> ')
    return equip_choice

# equipment room


def choose_equipment():
    print("""You better know your equipment. You will get points for getting ready
    without asking our divers for help. First we need to test your knowledge.""")
    print("What do you need?")

    equipment = {
        'Fins': "Fins come in many shapes.",
        'Mask': "You always have to carry one extra mask with you.",
        'Drysuit': "Wear a drysuit in cold waters!",
        'Bottles': "Better be careful how you handle them",
        'Computer': "Always do the safety stops",
        'Reel': "Never go cave diving without it",
        'Cookies': "They help you find your way",
        'Knife': "Cut through when entangled",
        'Bungee': "Fix that equipment!",
        'Gases mix': "Know your mixes."}

    # print out the equipment list
    equipment_list = list(equipment.keys())

    print("Choose the equipment you need:")

    # make a list of chosen items
    choices = []

    # check if all the items were chosen
    while len(equipment_list) != len(choices):

        # remaining possible choices
        def items_remaining(a, b):
            return [item for item in a if item not in b]

        remaining = items_remaining(equipment_list, choices)

        # print remaining items
        print("Remaining items:")
        print(*remaining, sep=', ')

        # prompt user for new item
        new_item = choice()

        # if item is in the chosen items list  let the user know they must
        # choose smth else
        if new_item in choices:
            print(f"You already chose {new_item}")

        # else if item is not in the chosen list but in the equipment print its
        # value
        elif new_item not in choices and new_item in equipment_list:
            print(f"{equipment[new_item]}")

            # add the new_item to the choices
            choices.append(new_item)
        # else let the user know there is no such equipment
        else:
            print("No such equipment.")
            choose_equipment()

    print("The equipment you chose is:")
    print(*choices, sep=', ')


def death(reason):
    print(reason, "This is the end. At least you died in a beautiful scenery.")


def izbandis():
    print(
        """You see a beautiful tiny cristal clear lake. It is not very cold outside.\n The autmun leaves are the only reminders of this planet.\n The rest looks like in a dream.\n You put your drysuit on, carry your big tanks to the brink of the lake. Your heart is pounding with hope: this is starting well, it will be a promissing dive.\nThe instructor is already in the water, waiting for you.\n Hey, he says, we are going to descend directly to 28 m then find the entrance of the cave on the left. No guiding reel to that point.\n Once in the cave we are going to see the reel on the left.\n Following a narrow left corridor we'll reach a point where the reel goes under in a deep tunnel. 50 m deep.\n Then it opens up to a bigger cave. We explore that a little bit then ascend.\nLet's go!""")
    print(
        "You found the reel on the left . There is a long, narrow corridor and two entrances: one up, one down. Where do you go?")

    izbandis_choice = input('> ')

    if "up" in izbandis_choice:
        death(
            "Wrong and bad. Your air finishes as you try to find the way back.")

    elif "down" in izbandis_choice:
        print("""Perfect, your dive goes on as planned.\n You have enough air to explore the big beautiful cave.\n You ask the instructor to take a few pictures of you then you both ascend. Well done!"""
              )
    else:
        print("Not an option!")
        izbandis()


def mina():
    print(
        """There's an old gold mine that was abandoned 20 years ago. \n After an earthquake some of its walls collapsed and it was filled with water.\n You enter a dark tunnel. The water level is high enough.\n Once you reach the water, the instructor is helping you with handling the bottles.\n Just follow the reel, the instructor tells you. I will be in front of you at all times.\n If you stay behind and can't see me just check the reel.\n You go in and follow him. You turn on the light. \n Brilliant turquoise shafts of light plunge more than 30 m straight down.\n While enjoying the view your lights go off. What do you do? Change batteries or dive into the unknown?""")

    mina_choice = input('> ')

    if "change" in mina_choice:
        print(
            """Good, you are going to enjoy a great dive.\n You know what to do in limit situations.\n The instructor takes pictures of you and you ascend happy.""")

    elif "dive" in mina_choice:
        death(
            "You should have listened to your mother when she said this is a dangerous sport.\n You die like she expected.")

    else:
        print("Not an option!")
        mina()


def bulz():
    print(
        """This one is a 4 km cave. It has lots of tunnels and obstacles. You really need to stay close to me, says the instructor.\n The entrance is 6 m long and it's entirely submersed. The first gallery is 13 m long and it's only accessible by rib.\n There's a 2 m waterfall on the South wall. We can bypass it keeping right.\n In 5 m we face the second waterfall. On the left of it, the main tunnel.\n We enter this one then go down to 40 m. We play a bit there than come back. The reel is always on our right.\n You go in the water and swim to the rib. The instructor lights the waterfall. \n You follow the reel and reach 40 m in a 5 minutes descend. \n You look back but the instructor is gone. What do you do next? Go back? Wait for him there? """)

    bulz_choice = input('> ')

    if "go" in bulz_choice:
        death(
            "You panick and get lost.You breathe like a running giraffe. At 30 bars you don't have enough air for safety stops")

    elif "wait" in bulz_choice:
        print(
            """You have lots of air to wait for him. Soon enough you see his light above you.\n The dive goes on. He takes pictures of you and you surface""")

    else:
        print("Not an option!")
        bulz()

choose_diver()
