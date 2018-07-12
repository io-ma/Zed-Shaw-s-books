class Reward(object):
    """ Main reward class """

    def __init__(self, measurement):
        """ Initialize game reward """

        # We need a measurement unit
        # to calculate points
        self.counter = measurement
        self.points = self.counter * 10


class Death(object):
    """ Main death class """

    def __init__(self, reason):
        """ Initialize game penalty """

        self.reason = reason
        print(reason, "This is the end. At least you died in a beautiful scenery.")


