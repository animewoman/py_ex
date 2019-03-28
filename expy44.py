class Parent(object):
    def implicit(self):
        print("PARENT implicit")

    def override(self):
        print("PARENT override")

    def altered(self):
        print("PARENT altered")


class Other(object):
    def override(self):
        print("OTHER override")

    def implicit(self):
        print("OTHER implicit")

    def altered(self):
        print("OTHEr altered")


class Child(Parent):
    def override(self):
        print("CHILD override")

    def altered(self):
        print("CHILD, BEFORE PARENT altered")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


class Ours(object):
    def override(self):
        print("OURS override")

    def  implicit(self):
        print("OURS override")

    def altered(self):
        print("OURS altered")


class Other(object):
    def __init__(self):
        self.other = Ours()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print("OTHER, BEFORE OURS altered")
        self.other.altered()
        print("OTHER, AFTER OURS altered")


our = Ours()
other = Other()

our.altered()
other.altered()
