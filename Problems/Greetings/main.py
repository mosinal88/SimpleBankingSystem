class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {}!".format(self.name)


name_for_greet = Person(input())
print(name_for_greet.greet())
