class Animal():
    pass


class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name


class Person():
    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish():
    pass


class Salmon():
    pass


class Halibut(Fish):
    pass


rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
