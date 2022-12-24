#!/usr/bin/python3.8
## youtu.be/kqtD5dpn9C8

name = input("What's your name dingus? ")
print(name + " is a cunt.")

# Comparison Operators
sizz = input("What is your dick size in inches? ")
if float(sizz) < 7.5:
    dif = 7.5 - float(sizz)
    print("Your dick is " + str(dif) + " inches smaller than mine. haHA FUCK YOU!!")
elif float(sizz) == 7.5:
    print("We have the same sized dick! :D")
elif float(sizz) > 7.5:
    dif = float(sizz) - 7.5
    print("Your dick is " + str(dif) + " inches bigger than mine... damn..")

# Adding numbers
num1 = input("First number: ")
num2 = input("Second number: ")
# if you don't use float() here, it'd just concat 2 strings
# e.g. 10 + 20 = 1020
summ = float(num1) + float(num2)
print(num1 + " plus " + num2 + " equals " + str(summ))

# More Comparison Operators
temp = float(input("What's the temperature, dingus? "))
if temp > 30:
    print("over 30 is Hot")
elif temp > 15:
    print("over 15 is Nice")
else:
    print("15 or less is chilly, your dick is probably shrunk")


# Simple weight conversion
weight = input("What is your weight? ")
unitz = input("K for kg or L for pounds: ").lower()
if unitz == "l":
    weight = float(weight) / 2.2
    # FORMATTED STRING
    print(f"Weight in kg: {weight}")
else:
    weight = float(weight) * 2.2
    # NON FORMATTED STRING - DOES SAME THING!
    print("Weight in lb: " + str(weight))


