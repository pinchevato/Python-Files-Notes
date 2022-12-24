# youtu.be/3ohzBxoFHAY
# Returning to Corey Shafer vids using his example
# instead of my vulgar example. EXACT copy of his:
# (see classes_basics.py for my example w notes)

class Employee:

    raise_amt = 1.04
    
    # Review: 'dunder' init method is implicitly
    # called when we create Employee objects
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@anus.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Just returning a string to RECREATE OBJECT
    # so print(emp1) will return exact string used below to create emp1 obj
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # Meant for end-user so a lil more arbitrary
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # Say we want __add__ to combine 2 employees together n
    # have result be their combined salaries then..
    def __add__(self, other):
        return self.pay + other.pay

    # Say we want __len__ to retrn length of employee's
    # full name
    def __len__(self):
        return len(self.fullname())


emp1 = Employee('John', 'Johnson', 30000)
##print(emp1.fullname())
##emp1.apply_raise()
##print(emp1.pay)


# Notice this returns some dumb bullshit
# w/o defining __repr__ or __str__ method above
##print(emp1)

# repr built-in dunder method is unambiguous representation
# of the object n should be used for debugging n logging
print(repr(emp1))
# What's really happening is that it's directly calling
# the special method (this returns same thing)
print(emp1.__repr__())
# str built-in dunder method is a readable representation
# of an object n should be used for end-user
print(str(emp1))
# Same thing here, as w repr (returns same thing as prev line)
print(emp1.__str__())



# This is actually accessing __add__ func in background
print(1+2)
# Access this directly (returns same thing)
print(int.__add__(1,2))
# Same shit w strings:
print('a'+'b')
print(str.__add__('a','b'))

# Using __add__ method we defined above
# (would give error if __add__ wasn't defined above
emp2 = Employee('Butt', 'Fucker', 30001)
print(emp1 + emp2)


# Illustrating same idea as above, but
# with built-in __len__ method
print(len('penis'))
print('penis'.__len__())


# Using our re-defined __len__ method above
# (returns length of full name
print(len(emp1))
