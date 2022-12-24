# MORE dictionary shit from Sigma Coding: youtu.be/pDVgVMlqPd0
# just using same dict example from Mosh's script:
customer = {
    'name': 'Balls',
    'age': 29,
    'has_tits': True,
    'pubes': 'thick n bushy'}
print('\nTwo ways of deleting items in a dict:')
del customer["age"]
print(customer)
customer.pop('has_tits')
print(customer)

# REALLY don't get this one. popitem() removes the most-
# recently-added item from the dict AND you can set the
# item to a variable
print('\nAdd new item to dict:')
customer["dick size"] = 7.3
print(customer)
print('\nRemove an item using popitem() method... idfk')
butthole = customer.popitem()
print(butthole)
print(customer)

# Some built-in methods for dictionaries
print('\nSOME BUILT IN MEHTODS:\nThere are this '
      'many key-value pairs in the dict: ' + str(len(customer)))
print(customer.keys())
print(customer.values())
print(customer.items())

print('\nCheck to see if a key exists')
if 'pubes' in customer:
    print('The key exits')
else:
    print('Key doesnt exist')

print('\nCheck to see if a value exists')
if 'thick n bushy' in customer.values():
    print('The value exits')
else:
    print('Value doesnt exist')

print('\nCheck to see if a item exists')
# Here we pass in a tuple as the item
# (remember a dict is just a bunch of tuples)
if ('name', 'Balls') in customer.items():
    print('The item exits')
else:
    print('Item doesnt exist')

print('\nTwo ways of updating values:')
customer['name'] = 'Satan'
print(customer)
customer.update({'name':'Bill'})
print(customer)
print('\nupdate() can also be used to add new items:')
customer.update({'has_erection' : True})
print(customer)

print('\ncopy() to copy a dictionary:')
new_dic = customer.copy()
print(new_dic)

print('\nget() to see if key is in dict, '
      'argument if value not found:')
print(new_dic.get('has_erection', 'Key doesnt exist, dicknose'))
print(new_dic.get('loose_butt', 'Key doesnt exist, dicknose'))

print('\nsetdefault() to add an item.. yes '
      'ANOTHER WAY to add shit:')
new_dic.setdefault('shits_today', 2)
print(new_dic)

print('\nCreate dict using fromkeys(), arguments '
      'are a tuple w key names and the initial value of all')
keyss = ('Key1', 'Key2', 'Key3', 'Key4')
dict3 = dict.fromkeys(keyss, 'defauck')
print(dict3)

##print('\nclear() - clears a dict:')
##dict3.clear()
##print(dict3)

print('\nLoop thru dict to print keys neatly, instead of print(dict.keys())')
for key in dict3.keys():
    print(key)
# Can do same thing w .values() and .item() methods
print('\nNotice the diff when we loop thru .items() w one index or w two:')
for item in dict3.items():
    print(item)
for key, value in dict3.items():
    print(key, value)

print('\nDUNDER methods that do some shit:'
      '\nAnOTHER way of checking to see if a dict contains'
      '\na key (is dunder better? idfk..)')
print(dict3.__contains__('Key1'))
print('How much space in memory does the dict take up:')
print(dict3.__sizeof__())
print('Convert dict into a string, why better than str(dict)?')
print(dict3.__str__())


## COMPARING DICTIONARIES
dick1 = {'Key1': 'poop', 'Key2': 'balls', 'Key3': 'taint', 'Key4': 'boobs'}
dick2 = {'Key1': 'trees', 'Key2': 'balls', 'Key3': 'nutsack', 'Key23': 'boobs'}
print('\n\nCOMPARING THESE TWO DICTIONARIES')
print(dick1)
print(dick2)
print('\nKeys in Common using &')
print(dick1.keys() & dick2.keys())
print('\nDifferences in Keys using -')
print(dick1.keys() - dick2.keys())
print('..and reversed (order matters here)')
print(dick2.keys() - dick1.keys())
print('\nKeys from both dictionaries using | (no duplicates)')
print(dick1.keys() | dick2.keys())

print('\nItems in Common using &')
print(dick1.items() & dick2.items())
print('\nDifferences in Items using -')
print(dick1.items() - dick2.items())
print('..and reversed (order matters here)')
print(dick2.items() - dick1.items())
print('\nItems from both dictionaries using | (no duplicates)')
print(dick1.items() | dick2.items())

print('\nSUBSETS (will use new dicts):')
dick1 = {'k1': 'ab', 'k2': 'bc', 'k3': 'cd'}
dick2 = {'k1': 'ab', 'k2': 'bc'}
print('Is dick1 a subset of dick2?')
print(set(dick1) <= set(dick2))
print('Is dick1 a subset of dick2?')
print(set(dick1) >= set(dick2))
