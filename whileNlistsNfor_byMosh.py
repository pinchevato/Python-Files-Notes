#!/usr/bin/python3.8
## youtu.be/kqtD5dpn9C8 - starting at ~42min

print('WHILE LOOP:')
i = 1
while i <= 4:
    print(i * 'balls ')
    i += 1

print('\nINDEXING LISTS:')
names = ["Berenice", "Aziz", "Gordo", "Carajo", "Ruth"]
print(names)
# Indexing
print(names[4])
# Negative indexing
print(names[-4])
# Replace one element
names[1] = "Dirkadirka"
print(names[-4])
print(names[3:])
# Index range ***NOTE: 2nd number is not the index,
# but like index - 1 or some shit idfk..
print(names[2:4])

# LIST METHODS
print('\nLIST METHODS LIKE APPEND N REMOVE:')
names.append("Dingus")
print(names)
names.insert(1, "Dante")
print(names)
names.remove("Gordo")
print(names)
# .pop() function simply removes last item in a list
names.pop()
print(names)
names.clear()
print(names)
# The following stupid shit doesn't fucking work with
# lists of strings apparently so make new one
print("\nOPERATOR 'in' TO FIND ELEMENTS IN A LIST, AND len() FUNC, AND .index method:")
numbers = [99, 24, 18, 67, 1930]
print(numbers)
print(18 in numbers)
print(4 in numbers)
print(len(numbers))
# This works just like 'in' operator BUT! ..generates error instead of False
# ..soo why the fuck ever use it idk..
print(numbers.index(67))

print("\nUNPACKING A LIST")
a,b,c,d,e = numbers
print(a,b,c,d,e)

print('\nCOUNT & SORT & REVERSE & COPY')
# How many ties does 1930 occur in list
numbers.append(1930)
print(numbers)
print(numbers.count(1930))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
# don't understand yet why you'd need this method
numbers2 = numbers.copy()
print(numbers2)

# Use for loop to print list as separate elements, vertically
print('\nFOR LOOP TO MAKE IT VERTICAL:')
for item in numbers:
    print(item)
# To illustrate why the for is better than while here (more code)
##i=0
##while i < len(numbers):
##    print(numbers[i])
##    i += 1

print('\nUSE FOR LOOP TO ADD UP NUMBERS IN LIST')
total = 0
for i in numbers:
    total += i
print(f"Sum of list is {total}")
print('Or use sum() function to do same shit:')
print("Sum of list is " + str(sum(numbers)))

# Range function (generates range from 0 to this index)
print('\nUSING RANGE FUNCTION:')
nums = range(5)
# Default output for a range object
print(nums)
# How to print all elements in range object
for num in nums:
    print(num)
# A range not starting at zero
print('\n')
nums = range(7, 11)
for num in nums:
    print(num)
# A range not going one by one
print('\n')
nums = range(29, 70, 7)
for num in nums:
    print(num)
# IMPORTANT: don't need to even create the range separately
print("\nDON'T EVEN NEED TO CREATE VARIABLE SEPARATELY (just do within for loop)")
for num in range(16, 27, 4):
    print(num)
