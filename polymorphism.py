# https://youtu.be/pii3hAksya0
# You have diff implementation of same func
# for diff situations

# Define abstract class (cuz it's not doing
# anything, just reading error (abstract polymorphism)
class language:
    def say_hi(self):
        # This will return error if there is no
        # say_hi() func in child class
        raise NotImplementedError('Please use say_hi class in child class')

# These are inherited classes
class French(language):
    def say_hi(self):
        print('Bonjour')

class Spanish(language):
    def say_hi(self):
        print('Hola')

def intro(lang):
    lang.say_hi()

# steve is an object of class French..
steve = French()
barbara = Spanish()

intro(steve)
intro(barbara)
