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
n = input("\nGive me comma separated numbers, fat-tits > ")
listt = n.split(",")
print("List: ", listt)
print("Tuples: ", tuple(listt))

# Print the documentation of py built-in functions
print(print.__doc__)

# Print calendar (INSANE how easy this is)
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
