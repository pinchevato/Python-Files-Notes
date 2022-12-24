# Import entire module
import return_byMosh
print(return_byMosh.sqrt(64))

# Import specific functions from a module
from return_byMosh import sqrt
print(sqrt(66))

from numberListShit_byMosh import find_max
print(f"Max number is {find_max([2398,389,818,4])}")

# Package is just a fkn directory
# (ALL 3 OF THESE (pairs of lines) DO THE SAME THING)
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
# ..but this is verbose, if we only need one/more func's
# (can also add other functions separated by comma)
from ecommerce.shipping import calc_shipping
calc_shipping()
# ..OR to import whole module as an object
from ecommerce import shipping
shipping.calc_shipping()

# ..n just for funsies, we'll roll 
from tuplesnDicegame_byMosh import Dice
dice = Dice()
# this line will produce the same output as previous
print(dice.roll())
