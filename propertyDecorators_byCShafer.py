class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
##        self.email = first + '.' + last + '@anus.com'

    # PROPERTY DECORATOR - method acts like an attribute
    @property
    def email(self):
        return '{}.{}@retard.com'.format(self.first, self.last)

    # Same thing w fullname
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Setter decorator - changes an attribute
    # -must use name of property ("fullname")
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Deleter decorater - deletes an attribute
    @fullname.deleter
    def fullname(self):
        print('\nDeleting name.. beep boop..')
        self.first = None
        self.last = None
        
emp1 = Employee('Penis', 'Licker')
print(emp1.fullname)
print(emp1.email)
print(emp1.first)

# Notice that when we change the first name (with old code),
# the first name in the email does NOT change
# (but it does change first and fullname), this is because
# email attribute is set when obj is instantiated

# We created the email method w property decorator
# AND removed email attribute from init method; we
# also simply put the deorator before the fullname method
# (and removed parentheses after method calls below)
emp1.first = 'Dickhole'
print("\n" + emp1.fullname)
print(emp1.email)
print(emp1.first)

# Using Setter
emp1.fullname = 'Beavis Jones'
print("\n" + emp1.fullname)
print(emp1.email)
print(emp1.first)

#Using Deleter
del emp1.fullname
print(emp1.fullname)
print(emp1.email)
print(emp1.first)
