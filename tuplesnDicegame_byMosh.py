# TUPLES - use parentheses instead of brackets
print('\nFUCKIN TUPLES BRUH')
nums = (2, 9, 158, 3, 3)
print(nums)
# Returns how many times an element occurs in tuple
print("3 appears " + str(nums.count(3)) + " times in the tuple")
# Returns index of element
print("The index of 2 is " + str(nums.index(2)))
# to use tuples as variables, either do this:
x=nums[0]
y=nums[1]
z=nums[2] # blah blah..
# ..OR this shit "Unpacking"
v,w,x,y,z = nums
print("Unpacked Tuple")
print(v,w,x,y,z)


import random
class Dice:
    def roll(self):
        a = random.randint(1,6)
        b = random.randint(1,6)
        # NOTICE: no parentheses needed when returning a tuple
        return a,b

dice = Dice()
print(dice.roll())


