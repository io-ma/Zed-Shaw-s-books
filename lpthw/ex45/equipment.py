from textwrap import dedent


class Equipment(object):
    """ Equipment class """

    def __init__(self):
        """ Initialize game equipment """

        # We need small descriptions for each
        # piece of equipment
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

        # We need a list of all equipment
        self.equipment_list = list(self.equipment.keys())
        self.choices = []

    def choose_equipment(self):
        """ Prints the chosen equipment """

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
                # print short description of the item
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

equip = Equipment()
