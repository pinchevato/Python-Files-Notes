# DICTIONARIES
# composed of keys on left and values on right:
# KEY-VALUE PAIRS

print("Four ways of making a dictionary:")
# 1st way of making dict (use zip func):
keys = ["name", "age", "has_tits"]
values = ["Pendejo", 2983, False]
d1 = dict(zip(keys,values))
print(d1)
# 2nd way of making dict:
d2 = dict(name = "Pendejo", age = 2983, has_tits = False)
print(d2)
# 3rd way of making dict (list w tuple):
d3 = dict([("name", "Pendejo"),("age", 2983), ("has_tits", False)])
print(d3)

# 4th way of making dict (MORE CONVENTIONAL WAY):
customer = {
    "name": "Pendejo",
    "age": 2983,
    "has_tits": False
}
print(customer)
print("His name is " + customer["name"])
print("He has tits? : " + str(customer["has_tits"]))
# You can change the elements, just like fkn lists
customer["name"] = "Balls"
print("Now his name is " + customer["name"])
customer["has_tits"] = True
print("Now he has tits? : " + str(customer["has_tits"]))
# Also add new key
print("\nADD A NEW KEY")
customer["pubes"] = "thick n bushy"
print("He has " + str(customer["pubes"]) + " pubes.")

# don't really understand the diff between this and
# print(customer("name")), except that you don't get
# an error if you use a key that doesn't exist.. so wtf?
print("\nUSING .get() METHOD\n" + str(customer.get("name")) + "\n")
# soo.. this returns a value but it's not actually in the dict..?
print(customer.get("birthday", "Jan 99, 2938"))


# SIMPLE EXERCISE
numdict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
num_orig = input("\n\nGimme the number, jabroni ")
num_words = ""
for i in num_orig:
    num_words += numdict.get(i, "NaN, cuntmuscle") + " "
print(num_words)
