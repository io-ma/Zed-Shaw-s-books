from textwrap import dedent
import result as res


class Cave(object):
    """ Main cave class """

    def __init__(self, name):
        """Initialize cave class """

        self.name = name

        # We need an entry scene
        self.entry_scene = """ """

        # We need a description
        self.description = """ """

        # We need a map of the cave
        # NOTE: implement a real map
        #       in future versions
        #
        self.cave_map = """ """

        # We might need the depth
        # in future versions
        self.depth = None

        # This is the problem the
        # diver needs to solve
        self.problem = """ """

        # We need a winning choice
        self.won_choice = "won choice"

        # This is the unlucky choice
        self.death_choice = "death choice"

        # We need a different penalty
        # phrase for each cave
        self.death_phrase = "death phrase"

        # The divers gets rewarded with
        # this winning phrase
        self.won_phrase = "won phrase"

        # choose cave intro
        self.intro = """What is the cave you'd like to explore today? """

    def enter(self):
        """ prints the cave entry scene """
        print(dedent(self.entry_scene))

    def get_description(self):
        """ prints description of cave """
        print(dedent(self.description))

    def get_map(self):
        """ prints cave map """
        print(dedent(self.cave_map))

    def get_depth(self, depth):
        """ defines cave depth"""
        self.depth = depth

    def get_problem(self):
        """ prints cave problem """
        print(dedent(self.problem))

    def get_won_phrase(self):
        """ prints winning phrase """
        print(dedent(self.won_phrase))


def choose_cave():

    izbandis = Cave("Izbandis")
    mina = Cave("Mina")
    bulz = Cave("Bulz")

    caves = [izbandis, mina, bulz]

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
                What is the cave you'd like to explore today?
                """))

    print("Izbandis\nMina\nBulz")

    cave_choice = input('> ')

    for cave in caves:
        if cave_choice in cave.name:
            cave.enter()
            cave.get_description()
            cave.get_map()
            cave.get_problem()
            choice = input('> ')
            if cave.won_choice in choice:
                cave.get_won_phrase()
            elif cave.death_choice in choice:
                res.Death(cave.death_phrase)
            else:
                print("Not an option")
                res.Death(cave.death_phrase)

        else:
            continue
