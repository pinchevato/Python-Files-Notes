# Corey tips n tricks: youtu.be/C-gEQdGVXbk

# Basic if else:
aa = False
if aa:
    x=1
else:
    x=0

# OR using ternary conditional:
aa= True
x = 1 if aa else 0
print(x)
#_____________________


# Use underscores to make large numbers more readable
a=12_392_849_299
# And you can add them to the output too
print(f'{a+999:,}')
#_____________________


# 'r' simply means we want to read the file
f = open('test.txt', 'r')
file_contents = f.read()
f.close()
words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# Instead of manually closing the file, it's better
# to use a 'context manager.' Better code:
with open('test.txt', 'r') as f:
    file_contents = f.read()
words = file_contents.split(' ')
word_count = len(words)
print(word_count)
#_____________________


# Keeping track of count w/o enumerate() func
names = ['fuck', 'shit', 'ass', 'dick', 'bitch']
index = 0
for j in names:
    print(index, j)
    index += 1
print('\n')

# Use enumerate() func when keeping track of count
# to 'clean up' code, also allows us to start wherever
names = ['boobs', 'tits', 'breasts', 'chesticles', 'bazongas']
for ind, j in enumerate(names, start=655):
    print(ind, j)
print('\n')

# Looping thru TWO lists using enumerate()
# (no automatic numbers next to each item in this case)
names = ['Peter', 'Charles', 'Stephen', 'Arthur']
nicks = ['Pete', 'Chuck', 'Steve', 'Art']
for index, name in enumerate(names):
    nick = nicks[index]
    print(f'{nick} is short for {name}')

# HOWEVER, better to use zip() instead of enumerate
# AND we can use 3+ LISTS! ..aaand how!
titles = ['Mister', 'Sir', 'Duke', 'King']
for name, nick, title in zip(names, nicks, titles):
    print(f'{nick} is short for {title} {name}')
          
# We can also just return tuples - not "unpacking"
# IMPORTANT FOR UNSDERSANING WHAT UNPACKING MEANS
for derp in zip(names, nicks, titles):
    print(derp)

# ***STOPPED VID AT 13:55 AT UNPACKING - KINDA OVER MY HEAD
# ***CONT LATER(?)
