from dictionary import Dictionary

class Testing(object):

    def __init__(self):
        self.states = Dictionary()
        self.cities = Dictionary()

    def test_set(self):
        # create a mapping of state to abreviation
        self.states.set('Oregon', 'OR')
        self.states.set('Florida', 'FL')
        self.states.set('California', 'CA')
        self.states.set('New York', 'NY')
        self.states.set('Michigan', 'MI')

        # creates a basic set of states and some cities in them
        self.cities.set('CA', 'San Francisco')
        self.cities.set('MI', 'Detroit')
        self.cities.set('FL', 'Jacksonville')

        # add some more cities
        self.cities.set('NY', 'New York')
        self.cities.set('OR', 'Portland')


    def test_get(self):
        # print(out some cities
        print('-' * 10)
        print("NY State has: %s" % self.cities.get('NY'))
        print("OR State has: %s" % self.cities.get('OR'))

        # print(some states
        print('-' * 10)
        print("Michigan's abbreviation is: %s" % self.states.get('Michigan'))
        print("Florida's abbreviation is: %s" % self.states.get('Florida'))

        # do it by using the state then cities dict
        print('-' * 10)
        print("Michigan has: %s" % self.cities.get(self.states.get('Michigan')))
        print("Florida has: %s" % self.cities.get(self.states.get('Florida')))

        # print(every state abbreviation
        print('-' * 10)
        self.states.list()

        # print(every city in state
        print('-' * 10)
        self.cities.list()

        print('-' * 10)
        state = self.states.get('Texas')

        if not state:
            print("Sorry, no Texas.")

        # default values using ||= with the nil result
        # can you do this on one line?
        city = self.cities.get('TX', 'Does Not Exist')
        print("The city for the state 'TX' is: %s" % city)

test = Testing()
test.test_set()
test.test_get()
