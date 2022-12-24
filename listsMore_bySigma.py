# Sigma Lists youtu.be/3ak9SMRAle8
# Some of this shit is redundant with my other file:
# whileNlistsNfor_byMosh.py

print('Nested lists & Referencing them')
a = [[98,3,0.4],['fuck','you'],[['p','cunt',3],False]]
print(a)
print('\nList length is ' + str(len(a)))
print('First item is ' + str(a[0]))
print('First item in second element is ' + str(a[1][0]))
print('Third item in first element is ' + str(a[0][2]))
print('Second sub-element in first element of third item is '
      + str(a[2][0][1]))
print("\nAs before in Mosh's ex, we can assign lists by index:")
a[1]= 'balls'
print(a)
print(' ..AND we can assign multiple elements by index:')
a[0:2] = ['poop','butt']
print(a)
print("\nAnd [to review] Mosh showed us the .append() method:")
a.append('nutsack')
print(a)
print(' ..AND we can use .extend() method to add multiple items:')
a.extend(['turd','boobs'])
print(a)
print(' ..AND we can simply use "+" to do the same thing'
      '\nas .append and .extend (not sure why to choose one over the other')
a = a + [10,11]
print(a)
print('\nUsing "del" keyword:')
del a[2]
print(a)
del a[0:2]
print(a)
print('Or delete whole list.. dunno why (returns error if u try n use it after)')
del a

print('\nWe can use .insert() method as Mosh showed'
      '\nor insert items using indexing')
b=[9,8,7,6]
print(b)
print('Notice difference between indexing using b[2:2], which inserts item')
b[2:2] = [4,3]
print(b)
b=[9,8,7,6]
b[2] = [4,3]
print('..versus using b[2], which just replaces item')
print(b)
b=[9,8,7,6]
print('Using max() n min() functions')
print(max(b))
print(min(b))

print('\nWe can also use "*" to multiply the list')
b=['a','b','c','d']
print(b)
print('Using "[b]*3": ' + str([b]*3))
print('Using "[b*3]": ' + str([b*3]))
print('\nUsing .pop() method w no args returns & removes last item')
print(b.pop())
print(b)
print('Or use an arg and remove specific item')
print(b.pop(1))
print(b)
print('AAaand for some fkn reason we have a .clear() method')
print(b.clear())

c=['aids','poop','farts','penis']
print('\nUse if to see if an item exists in a list')
print(c)
if 'aids' in c:
    print('Yeppers')
if 'nuts' in c:
    print('Yeppers')

print('\nUse enumerate() function to create object containing'
      ' index and value for list:')
for ind, val in enumerate(c):
    print(ind,val)
