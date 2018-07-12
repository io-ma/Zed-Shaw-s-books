## Animal is-a object (yes, sort of confusing)look at the extra credit
class Animal(object):
    def __init__(self, name):
        self.name = name

    def furry(self):
        self.has_fur = "furry"
        print(f"This is  a {self.has_fur} animal.")

    def not_furry(self):
        self.no_fur = "not furry"
        print(f"This is a {self.no_fur} animal.")

    def predator(self):
        print("It attacks smaller birds and eats them.")

    def prey(self):
        print("It is eaten by its enemies.")

    def veg(self):
        print("It loves eating grass.")
## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
        self.furry()
        print(f"His name is {self.name}.")
        self.predator()

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
        self.age = None
    
 
## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## super() gets the __init__ from Person
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        self.age = int(input("Tell me your age.\n"))
        print(f"Employee's age is {self.age}")

## Fish is-a object
class Fish(object):

    def __init__(self, name):
        self.name = name
        self.colours = ['pink', 'blue', 'violet']

## Salmon is-a Fish
class Salmon(Fish):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        print(f"{self.name} is a {self.colours[0]} fish.")


## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is_a Dog
rover = Dog("Rover")

## satan is_a Cat 
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## frank is-a Employee and has-a 120000 salary
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a fish
flipper = Fish("Flipper")

## crouse is-a Salmon
crouse = Salmon("Crouse")

## harry is-a Halibut
harry = Halibut("Harry")
