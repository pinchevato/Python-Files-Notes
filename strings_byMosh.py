#!/usr/bin/python3.8
## https://youtu.be/_uQrJ0TkZlc 35min

print('STRING INDEXING:')
derp = 'Sniff my balls.'
print(derp)
print(derp[-4])
print(derp[6:10])
# You can clip the ends of the string
print(derp[4:])
print(derp[:4])
# Comibine positive and negative indexing
print(derp[2:-2])
# NOTE: to copy string, use [:]
print('\nNOTE: TO COPY A STRING USE new=[:] NOTATION')
derp2=derp[:]
print(derp2)

#FORMATTED STRINGS
print('\nFORMATTED STRINGS:')
first = 'Kamala'
last = 'Harris'
# Non-dyanmic way of inserting variables into code
##msg = first + ', the giant cunt, ' + last + ' is the devil.'
# WE CAN DYNAMICALLY INSERT VALUES INTO THE FOLLOWING STRING
# (don't really get what this means)
msg = f'{first}, the giant cunt, {last} is the devil.'
print(msg)
# len function, upper, lower, title
print('The length of the previous string is ' + str(len(msg)))
print(msg.upper())
print(msg.lower())
print(msg.title())
# find() and replace() methods
print('\nUSING find() and replace()\nThe word "cunt" appears at spot #' + str(msg.find('cunt')) + ' in the string')
print(msg.replace('cunt', 'whore'))
# in operator - BOOLEAN
print('USING "in" OPERATOR: Is "devil" in our string?')
print('devil' in msg)

# FOR LOOPS WORK THE SAME W STRINGS AND LOOPS
##print('\nUSING FOR LOOPS W STRINGS (work the same as w lists)')
for i in msg:
    print(i)


