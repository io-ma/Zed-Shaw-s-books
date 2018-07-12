from textwrap import dedent
import cave as ca
import result as res


class Instructor(object):
    """ This builds the instructors """

    def __init__(self, name):
        """ Initialize instructor """
        self.name = name
        self.instructor = " "
        self.intro = """ """

    def get_intro(self):
        """ Gets the instructor intro """

        print(dedent(self.intro))

# We need to instantiate 
# all the instructors
mike = Instructor("Mike")
alex = Instructor("Alex")
vali = Instructor("Vali")

instructors = [mike, alex, vali]

mike.intro = """
            Hmmm, I wouldn't trust that one.
            He is sneakier than a serpent.
            He is a good diver though.
            Expect the unexpected.
            Mike:
            For 5000 GBP I can take you to the secret caves.
            If you buy me a pizza, you get to see the normal caves.
            Where do you want to dive?
            """
alex.intro = """
            Good choice! Your life is in good hands.
            There are very beautiful underwater caves out there
            """

vali.intro = """
            Good choice! Your life is in good hands.
            There are very beautiful underwater caves out there
            """


def choose_instructor():
    """ This chooses an instructor """

    print(dedent("""
                We have 3 instructors you can choose from.
                They all are quite experienced. Make a wise choice:
                """))

    print("Alex\nVali\nMike")

    instructor_choice = input('> ')

    # we need to make sure 
    # the instructor name exists 
    for instructor in instructors:
        if instructor_choice in instructor.name:
            instructor.get_intro()

            # if the chosen instructor is Alex or Vali 
            # diver chooses a cave
            if instructor_choice == "Alex" or instructor_choice == "Vali":

                ca.choose_cave()

            # if chosen instructor is Mike
            # diver needs to choose between a 
            # secret or a normal cave
            else:

                cave = input('> ')

                # if diver chooses secret caves
                # Mike robs the diver and asks them 
                # if they want to tell everyone or
                # dive in the normal caves
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

                    # if diver chooses to tell 
                    # Mike shoots them
                    if "tell" in choice:
                        res.Death("Mike shoots you")

                    # if diver chooses to dive 
                    # they go in the normal 
                    # caves
                    elif "dive" in choice:
                        ca.choose_cave()

                    else:
                        print("Learn to type!")

                # if diver chooses normal caves 
                # they go there
                elif "normal" in cave:
                    ca.choose_cave()

                else:
                    print("Learn how to type!")


        else:
            continue
