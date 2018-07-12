from sys import exit
from textwrap import dedent


class Reward(object):

    def __init__(self, measurement):
        self.counter = measurement
        self.points = self.counter * 10


class Death(object):

    def __init__(self, reason):
        self.reason = reason
        print(reason, "This is the end. At least you died in a beautiful scenery.")


class Equipment(object):

    def __init__(self):

        self.equipment = {
            'Fins': "Fins come in many shapes.",
            'Mask': "You always have to carry one extra mask with you.",
            'Drysuit': "Wear a drysuit in cold waters!",
            'Bottles': "Better be careful how you handle them",
            'Computer': "Always do the safety stops",
            'Reel': "Never go cave diving without it",
            'Cookies': "They help you find your way",
            'Knife': "Cut through when entangled",
            'Bungee': "Fix that equipment!",
            'Gases mix': "Know your mixes."
        }

        self.equipment_list = list(self.equipment.keys())
        self.choices = []

    def choose_equipment(self):
        print(dedent("""
                    You better know your equipment.
                    You will receive points for getting ready
                    without asking our divers for help.
                    First we need to test your knowledge.
                    What do you need?
                    """))

        available_items = self.equipment_list

        # check if there are available items
        while available_items:
            # print remaining equipment
            print("Available equipment")
            print(*available_items, sep=', ')
            # prompt user for an item
            choice = input('> ')

            if choice in available_items:
                # find out the index of the chosen item
                item_place = available_items.index(choice)
                # pop the item
                item = available_items.pop(item_place)
                # print what the item does
                print(f"{self.equipment[item]}")
                # append the item to the choices list
                self.choices.append(item)
                # ask user if they need more equipment
                print("\nDo you need more equipment? Answer with yes or no.")

                next_choice = input('> ')

                if "yes" in next_choice:
                    continue

                else:
                    print("You chose:")
                    print(*self.choices, sep=(', '))
                    break

            # check if the item is in the chosen ones
            elif choice in self.choices:
                print("You already chose that.")

            # other possible cases
            else:
                print("Not an option")
                # print the chosen items
                print("You chose:")
                print(*self.choices, sep=(', '))


class Cave(object):

    def __init__(self, name):
        self.name = name
        self.entry_scene = """
        dummy text dummy text
        dummy text dummy text
        dummy text dummy text
        """

        self.description = """
        some dummy text for the cave
        description in general
        """
        self.cave_map = """
        this is the map
        of the cave and it should be
        totally cool
        """
        self.depth = None
        self.problem = """
        this is the problem
        the diver needs to solve
        to find out if he won
        or lost.
        """
        self.won_choice = "won choice"
        self.death_choice = "death choice"
        self.death_phrase = "death phrase"
        self.won_phrase = "won phrase"

    def enter(self):
        print(dedent(self.entry_scene))

    def get_description(self):
        print(dedent(self.description))

    def get_map(self):
        print(dedent(self.cave_map))

    def get_depth(self, depth):
        self.depth = depth

    def get_problem(self):
        print(dedent(self.problem))

    def get_won_phrase(self):
        print(dedent(self.won_phrase))


class Diver(object):

    def __init__(self, diver_name):
        self.name = diver_name
        self.choices = {
            'instructor_name': 'x',
            'cave_name': 'y',
            'equipment': []
        }

        self.points = None

    def set_instructor(self, instructor_name):
        self.choices['instructor_name'] = instructor_name

    def set_cave(self, cave_name):
        self.choices['cave_name'] = cave_name

    def set_equipment(self, equipment_choices):
        self.choices['equipment'] = equipment_choices


class Instructor(object):
    def __init__(self, name):
        self.name = name


def main():

    mike = Instructor("Mike")
    alex = Instructor("Alex")
    vali = Instructor("Vali")

    instructors = [mike, alex, vali]

    izbandis = Cave("Izbandis")
    mina = Cave("Mina")
    bulz = Cave("Bulz")

    caves = [izbandis, mina, bulz]
    equip = Equipment()

    izbandis.entry_scene = "Izbandis is quite dangerous if you are not good at cave diving."

    izbandis.description = """
			You see a beautiful tiny cristal clear lake.
			It is not very cold outside.
			The autumn leaves are the only reminders of this planet.
			The rest looks like in a dream.
			You put your drysuit on, carry your big tanks to the brink of the lake.
			Your heart is pounding with hope:
			this is starting well, it will be a promissing dive.
			The instructor is already in the water, waiting for you.
			"""
    izbandis.depth = 100
    izbandis.cave_map = """
			Hey, he says, we are going to descend directly to 28 m then find the entrance of the cave on the left.
			No guiding reel to that point.
			Once in the cave we are going to see the reel on the left.
			Following a narrow left corridor we'll reach a point where the reel goes under in a deep tunnel.
			50 m deep. Then it opens up to a bigger cave.
			We explore that a little bit then ascend.
			Let's go!
			"""
    izbandis.problem = """
			You found the reel on the left .
			There is a long, narrow corridor and two entrances:
			one up, one down.
			Where do you go?
			"""

    izbandis.won_choice = "up"
    izbandis.death_choice = "down"
    izbandis.death_phrase = "Wrong and bad. Your air finishes as you try to find the way back."
    izbandis.won_phrase = """
                        Perfect, your dive goes on as planned.
                        You have enough air to explore the big beautiful cave.
                        You ask the instructor to take a few pictures of you then you both ascend.
                        Well done!
                        """

    mina.entry_scene = """
			There's an old gold mine that was abandoned 20 years ago.
			After an earthquake some of its walls collapsed
			and the mine was filled with water.
			"""
    mina.description = """
			You enter a dark tunnel. The water level is high enough.
			Once you reach the water, the instructor is helping you with handling the bottles.
			Just follow the reel, the instructor tells you.
			I will be in front of you at all times.
			If you stay behind and can't see me just check the reel.
			You go in and follow him. You turn on the light.
			Brilliant turquoise shafts of light plunge more than 30 m straight down.
			"""
    mina.depth = 35
    mina.cave_map = """
		There is a 500 m long, 4 m wide tunnel right in front of you.
		It then goes right and opens up downwards in a huge chamber.
		The descent is quite rocky and you have to be careful and follow the reel.
		"""
    mina.problem = """
		while enjoying the view your lights go off.
		what do you do?
		change batteries or dive into the unknown?
		"""
    mina.won_choice = "change"
    mina.death_choice = "dive"
    mina.won_phrase = """
                    Good, you are going to enjoy a great dive.
                    You know what to do in limit situations.
                    The instructor takes pictures of you and you ascend happy.
                    """
    mina.death_phrase = "You should have listened to your mommy, this is a dangerous sport."

    bulz.entry_scene = """
			Bulz doesn't have long galleries, but it's spectacular.
			The surrounding Valley is called The Valey of Hell.
			"""

    bulz.description = """
			This one is a 4 km cave. It has lots of tunnels and obstacles.
			You really need to stay close to me, says the instructor.
			"""
    bulz.depth = 95

    bulz.cave_map = """
		The entrance is 6 m long and it's entirely submersed.
		The first gallery is 13 m long and it's only accessible by rib.
		There's a 2 m waterfall on the South wall. We can bypass it keeping right.
		In 5 m we face the second waterfall. On the left of it, the main tunnel.
		We enter this one then go down to 40 m. We play a bit there than come back.
		The reel is always on our right.
		You go in the water and swim to the rib. The instructor lights the waterfall.
		You follow the reel and reach 40 m in a 5 minutes descent.
		"""
    bulz.problem = """
		You look back but the instructor is gone.
		What do you do next?
		Go back? Wait for him there?
		"""
    bulz.won_choice = "wait"
    bulz.death_choice = "go"
    bulz.won_phrase = """
                    You have lots of air to wait for him.
                    Soon enough you see his light above you.
                    The dive goes on.
                    He takes pictures of you and you surface
                    """
    bulz.death_phrase = "You panick and get lost.You breathe like a running giraffe. At 30 bars you don't have enough air for safety stops"

    print(dedent("""
                Welcome to our cave diving center, brave creature.
                What is you name?
                """))

    answer = input('> ')

    diver = Diver(answer)
    diver.name = answer

    equip.choose_equipment()
    diver.set_equipment(equip.choices)
    reward = Reward(len(equip.choices))

    print(f"You get {reward.points} points!")

    print(dedent(f"""
                We have 3 instructors you can choose from, {diver.name}.
                They all are quite experienced. Make a wise choice:
                """))
    for instructor in instructors:
        print(instructor.name)

    instructor_choice = input('> ')

    diver.set_instructor(instructor_choice)

    if instructor_choice == "Alex" or instructor_choice == "Vali":
        print(dedent("""
                    Good choice! Your life is in good hands.
                    There are very beautiful underwater caves out there.
                    What is the cave you'd like to explore today?
                    """))

        for cave in caves:
            print(cave.name)

        cave_choice = input('> ')

        for cave in caves:
            if cave_choice in cave.name:
                diver.set_cave(cave_choice)
                cave.enter()
                cave.get_description()
                cave.get_map()
                cave.get_problem()
                choice = input('> ')
                if cave.won_choice in choice:
                    cave.get_won_phrase()
                elif cave.death_choice in choice:
                    Death(cave.death_phrase)
                else:
                    print("Not an option")
                    Death(cave.death_phrase)

            else:
                continue

    elif instructor_choice == "Mike":

        print(dedent("""
                    Hmmm, I wouldn't trust that one.
                    He is sneakier than a serpent.
                    He is a good diver though.
                    Expect the unexpected.
                    Mike:
                    For 5000 GBP I can take you to the secret caves.
                    If you buy me a pizza, you get to see the normal caves.
                    Where do you want to dive?
                    """))
        cave = input("> ")

        if "secret" in cave:
            print(dedent("""
			I can show you 3 more caves!
			But life is short and time is money.
			Give me the 5000.
			You give him the money and the adventure begins.
			"""))
            print(dedent("""
                        Mike points a gun at you:
                        We are all alone in the equipment room.
                        I must tell you the truth.
                        Your money's lost.
                        I am a dangerous killer hiding in this diving resort.
                        You either choose to tell everyone or dive in the usual places.
                        No such thing as the promised secret caves.
                        What's your choice?
                        """))
            choice = input('> ')

            if "tell" in choice:
                Death("Mike shoots you")

            elif "dive" in choice:
                print(dedent("""
                            Good choice! Your life is in good hands.
                            There are very beautiful underwater caves out there.
                            What is the cave you'd like to explore today?
                            """))

                for cave in caves:
                    print(cave.name)

                cave_choice = input('> ')

                for cave in caves:
                    if cave_choice in cave.name:
                        diver.set_cave(cave_choice)
                        cave.enter()
                        cave.get_description()
                        cave.get_map()
                        cave.get_problem()
                        choice = input('> ')
                        if cave.won_choice in choice:
                            cave.get_won_phrase()
                        elif cave.death_choice in choice:
                            Death(cave.death_phrase)
                        else:
                            print("Not an option")
                            Death(cave.death_phrase)

                    else:
                        continue
            else:
                Death("Not an option, you die!")

        elif "normal" in cave:
            Death("Bye bye life! Mike shoots you.")

        else:
            print("You can only choose a normal cave or a secret one.")

    else:
        Death("You can't even type a name. You die!")


if __name__ == '__main__':
    main()
