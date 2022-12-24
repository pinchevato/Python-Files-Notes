#!/usr/bin/python3.8
class Point:
    # init method is a 'constructor' - it gets
    # called every time we create a new Point obj
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# (this doesn't work once init method is in place)
### Adding attributes to object point1
##point1 = Point()
##point1.x = 10
##point1.y = 20
##print(point1.x)
##point1.draw()

# Use constructor instead of creating obj manually
point2 = Point(10,20)
print(point2.x)
# and of course we can redefine attributes manually
point2.x = 13
print(point2.x)


# Just another simple example
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hey I'm {self.name}, fuck you")

        
bob = Person("Bob")
bob.talk()

# Subclass
class Retard(Person):
    def shit_pants(self):
        print("Aahh no! I shit my pants!")

retard1 = Retard("Timmaahhh!")
retard1.talk()
retard1.shit_pants()

