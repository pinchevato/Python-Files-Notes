#"CLASSES" youtu.be/ZDa-Z5JzLYM youtu.be/BJ-VvGyQxho

class bodyparts:
    # CLASS VARIABLES
    covered_in = 'skin'
    num_of_parts = 0
    price = 27

    # to set up object automatically we us init method, or "contructor"
    # calling first argument "self" isn't necessary but convention
    def __init__(self, name, smell, taste, size):
        # INSTANCE VARIABLES 
        # tnese names don't have to be same but makes it easier here
        self.name = name
        self.smell = smell
        self.taste = taste
        self.size = size
        self.hola = 'Your ' + size + ' ' + name + ' smells ' + smell + ' and tastes ' + taste

        #Class variable increments each time an instance is ..instantiated :-| ?
        bodyparts.num_of_parts += 1

    #Create a method - each method within a class automatically
    #takes the intance as the first arg (i.e. self)
    #This method just creates a 'description' with the name, size and smell
    def descr(self):
        print('{} {} {}'.format(self.name,self.size,self.smell))
        # **two ways of writing the SAME THING
##        print(f"{self.name} {self.size} {self.smell}")

    def cover(self):
        self.hola = self.hola +  ' n is covered in ' + self.covered_in

    def __repr__(self):
        return "Bodypart('{}','{}','{}')".format(self.name, self.taste, self.smell)
 
    def __str__(self):
        return '{} - {}'.format(self.name, self.size)


    #This is a class method hermmmderp!!!
    @classmethod
    def set_price(cls, price):
        cls.price = price

    #Class method as "alternative constructor" - provides multiple
    #ways of creating objects; e.g. you get a new bodypart as string w
    #properties delineated by commas
    #e.g. vagina='vagina,like roses,like heaven,tight'
    @classmethod
    def from_string(cls, bpart_str):
        name, smell, taste, size = bpart_str.split(',')
        return cls(name, smell, taste, size)


#Static method - ultra simple example
#just returns whether or not it's a weekend based on date below
    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Its the weekend BEYOTCH!!!'
        return 'Its a fuuuckin weekday'
import datetime
mydate=datetime.date(2022,8,28)
print('USING STATIC METHOD TO RETURN INFO THAT PERTAINS TO ALL OBJECTS:\n' + bodyparts.is_weekend(mydate))



#SUB-CLASSES, here we inherit all the functionality
#(attributes and methods) of the bodyparts class
class privates(bodyparts):
    covered_in='underwear'
    price=69
    #Same line as init method for bodyparts class,
    #but w extra argument / extra functionality
    def __init__(self, name, smell, taste, size, sexy):
        #instead of pasting all code from bodyparts init method:
        super().__init__(name, smell, taste, size)
        self.sexy = sexy

#class variables, here we can pass in values in init method
#instance "self" is passed automatically so we don't pass that
elbow=bodyparts('elbow', 'like my colon', 'like popcorn', 'pointy')
elbow.cover()
#just private parts here, w sexy attribute
print('\n\nUSING SUBCLASSES TO ADD SEXY ATTRIBUTE')
scrotum=privates('scrotum', 'good', 'delicious', 'big', 'not sexy')
scrotum.cover()
taint=privates('taint', 'questionable', 'salty', 'normal', 'not sexy')
taint.cover()
asshole=privates('asshole', 'like poop', 'like poop', 'loose', 'not sexy')
asshole.cover()
labia=privates('labia', 'like heaven', 'glorious', 'smooth', 'sexy')
labia.cover()

print('Your ' + scrotum.name + ' is ' + scrotum.sexy)
print('Your ' + taint.name + ' is ' + taint.sexy)
print('Your ' + labia.name + ' is ' + labia.sexy)
print('Your ' + asshole.name + ' is ' + asshole.sexy)
#We can give the covered_in attribute to the whole class or to only one instance

#In this first case, assigning it to whole class, NONE of the instances have
#the attribute, only the class
# Employee.covered_in = 'scales'
#Here we just assign the class variable to this instance and the rest will
#refer to the class for this variable
taint.covered_in = 'scales'

#Use class variable to cover the bodypart in "skin" (class variable set above)
#(or class variable set to instance variable a few lines above)
taint.cover()
#NOTE: this is the 2nd time this command is used so the taint is covered twice


print('\n\nUSING CLASS METHOD TO SET PRICES FOR INDIVIDUAL PARTS')
#Use default variable set at the top, just for reference
print('Your ' + elbow.name + ' costs ' + str(elbow.price))
#Use a CLASS METHOD (@classmethod above) to change price of body parts
#(in other words, all body parts cost the same for this class - makes no sense who cares)
bodyparts.set_price(64)
#replace 'asshole' w any other bodypart n it'll say the same price
print('Your ' + asshole.name + ' costs ' + str(asshole.price))
#This uses CLASS METHOD to only change one instance instead of whole class like above 
scrotum.set_price(98)
print('Your ' + scrotum.name + ' costs ' + str(scrotum.price))
#This does the EXACT SAME THING AS ABOVE LINE but..
#manually sets the class variable for an instance, does NOT use the class method
#SAME THING AS ABOVE WITH taint.covered_in = scales
scrotum.price = 99
print('\n...Now, your ' + scrotum.name + ' costs ' + str(scrotum.price))


##  HOW THE FUCK DO I MAKE THESE WORK W 'privates' subclass??!?!?!?!
##  in other words, cover them w underwear while using from_string class method
##  (it works fine when I call the privates subclass w/o from_string.. WTF?)

#CLASS METHOD AS ALTERNATIVE CONSTRUCTOR
#if you had body parts coming in the form of a string w attributes
#separated by commas n wanted to automate it
vagina=bodyparts.from_string('vagina,like roses,like heaven,tight')
vagina.cover()
#why not... add a couple more body parts, one private, one not
dingus=bodyparts.from_string('dingus,like a wet hole,like AIDS,massive')
dingus.cover()
mouth=bodyparts.from_string('mouth,of fine perfume,of honey and milk,normal-sized')
mouth.cover()

print('\n\nUSING CLASS METHOD TO MAKE A NICE SENTENCE ABOUT EACH OBJECT:')
print(elbow.hola)
print(scrotum.hola)
print(taint.hola)
print(asshole.hola)
print(labia.hola)
print(vagina.hola)
print(dingus.hola)
print(mouth.hola)

#need "()" here cuz this is a method not an attribute
print('\n\nANOTHER CLASS METHOD desc() JUST TO LIST A FEW ATTRIBUTES OF THE OBJECT')
print(scrotum.name + ' description: ')
scrotum.descr()
#this line does the same thing, must pass in 'self'
print(taint.name + ' description: ')
bodyparts.descr(taint)


#SUBCLASS which includes objects created by ANOTHER subclass
print('\n\nSUBCLASS W METHODS FOR REMOVING N ADDING OBJECTS:')
class ladyparts(bodyparts):
    def __init__(self, name, smell, taste, size, parts=None):
        super().__init__(name, smell, taste, size)
        if parts is None:
            self.parts = []
        else:
            self.parts = parts
    # instance methods for this class
    def add_part(self, part):
        if part not in self.parts:
            self.parts.append(part)
    def remove_part(self, part):
        if part in self.parts:
            self.parts.remove(part)
    def print_ladyparts(self):
        for part in self.parts:
            part.descr()

parts_for_sex=ladyparts('lady parts','like ambrosia','like crotch','magical', [labia])
#NOTICE: we're using inherited code from the bodyparts class (hola method)
print(parts_for_sex.hola)

print('\nthe ladyparts list/descr is: ')
parts_for_sex.print_ladyparts()
parts_for_sex.add_part(vagina)
print('\n..now we added the vag using method in ladyparts sublcasssss: ')
parts_for_sex.print_ladyparts()
parts_for_sex.remove_part(labia)
print('\n..now we removed the labia: ')
parts_for_sex.print_ladyparts()


#using the class variable that is set to the class by "bodyparts.num_of_parts"
#statement above; this differs from the self.covered_in statement (also using
#a class variable) bc this can't be different for different instances
print('\nUSING SIMPLE CLASS VARIABLE TO KEEP COUNT '
      'IN ORIGINAL INIT METHOD:\nThere are '
      + str(bodyparts.num_of_parts) + ' body parts total')


#An object can be an instance of more than one class:
# isinstance(labia,bodyparts) = True
# isinstance(labia,privates) = True
# isinstance(elbow,privates) = False

#Similarly, we can check which classes are subclasses of which
# issubclass(ladyparts,bodyparts) = True
# issubclass(privates,bodyparts) = True
# issubclass(privates,ladyparts) = False

#"namespace"
# print(elbow.__dict__)
# print(bodyparts.__dict__)

#display info OUTSIDE the class
# print('{} {}'.format(scrotum.size,asshole.smell))


#REDUNDANT
#instance variables (contain data unique to each instance)
#same as in __init__ sequence but manual instead of automatic

# balls.smell = 'good'
# balls.taste = 'sweet'
# balls.size = 'big'
# taint.smell = 'questionable'
# taint.taste = 'sweaty'
# taint.size = 'average'

# print(balls.smell)
# print(taint.size)
