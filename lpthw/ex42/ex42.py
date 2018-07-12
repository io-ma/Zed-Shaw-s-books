## Animal is-a object (yes, sort of confusing)look at the extra credit
class Animal(object):
    pass

## Sog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee calls the __init__ from Person
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## is-a Fish
class Fish(object):
    pass

## is-a Salmon
class Salmon(Fish):
    pass

## is-a Halibut
class Halibut(Fish):
    pass


## rover is_a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## frank is-a Employee and has-a 120000 salary
frank = Employee("Frank", 120000)

## frank has-a pet called Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
