from textwrap import dedent
import instructor as inst
import equipment as eq
import result as res
import diver as dv


def main():
    """Create the entry point and start the game."""

    # We need to ask the user for their name
    print(dedent("""
            Welcome to our cave diving center, brave creature.
            What is you name?
            """))

    answer = input('> ')

    # We create the user's diver profile
    #
    # NOTE: to keep things organized,
    #       we will need to create a database
    #       in the upcoming version
    #
    diver = dv.Diver(answer)

    # The diver needs to choose the
    # equipment they use and get points
    eq.equip.choose_equipment()
    diver.set_equipment(eq.equip.choices)

    reward = res.Reward(len(eq.equip.choices))

    print(f"Well done, {diver.name}, you get {reward.points} points!")

    # Diver needs to choose an instructor
    inst.choose_instructor()


if __name__ == '__main__':
    main()
