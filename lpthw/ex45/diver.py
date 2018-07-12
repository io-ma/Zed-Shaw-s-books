class Diver(object):
    """ Main diver class """

    def __init__(self, diver_name):
        """ Initialize diver class """

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


