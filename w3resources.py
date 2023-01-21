import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print ("Raw 'Now': \t\t" + str(now))
print ("Using var's for each: \t" + str(now.strftime("%Y/%m/%d %H:%M:%S")))
print ("Using the '%D' var: \t" + str(now.strftime("%D")))

poop = datetime.datetime.utcnow()
print("\nUTC time: \t\t" + str(poop))
print("More vars returned: \t" + str(poop.strftime("%A, %d %B")))

##from math import pi
##r = float(input("Radius of circle?"))
##print("Area is: " + str(pi*2*r))

# Accepts a sequence of comma-separated numbers from user
# and generates a list and a tuple with those numbers
##n = input("\nGive me comma separated numbers, fat-tits > ")
##listt = n.split(",")
##print("List: ", listt)
##print("Tuples: ", tuple(listt))

# Print the documentation of py built-in functions
print(print.__doc__)

# Print calendar (INSANE HOW EASY THIS IS)
##import calendar
##y = int(input("Input the year : "))
##m = int(input("Input the month : "))
##print(calendar.month(y, m))

# A string that you don't have to "escape" from (wtf does this even mean?)
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

# Calculate number of days between two dates
##import datetime
##y1 = int(input("Input first date year: "))
##m1 = int(input("Input first date month: "))
##d1 = int(input("Input first date day: "))
##y2 = int(input("Input second date year: "))
##m2 = int(input("Input second date month: "))
##d2 = int(input("Input second date day: "))
##date1 = datetime.date(y1,m1,d1)
##date2 = datetime.date(y2,m2,d2)
##dif = date1 - date2f
##print("There are " + str(dif.days) + " between the dates")

# Calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the difference
##def difference(n):
##    if n <= 17:
##        return 17 - n
##    else:
##        return (n - 17) * 2
##dif = int(input("What's the number, bitch?"))
##print(difference(dif))

# Check if a number is within 100 of 1000 or 2000
##n = int(input("What's the number, asshole?"))
##if abs(1000-n) <= 100:
##    print(True)
##elif abs(2000-n) <= 100:
##    print(True)
##else:
##    print(False)
### O.. mas bien
##print((abs(1000 - n) <= 100) or abs(2000 - n) <= 100)



