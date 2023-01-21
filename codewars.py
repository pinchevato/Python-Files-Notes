# SHIT DOESN'T FUCKING WORK IN IDLE CUZ IT SUX DICK but who cares, fuck you!
# (works in iPython)

# Filter int's out of a list that also has strings (or other data types)
def filter_list(herp):
    x = []
    for i in range(len(l)):
        if isinstance(l[i],int):
            x.append(l[i])
    return x
    # MUCH BETTER SOLUTION
    return [i for i in l if not isinstance(i, str)]

l = ['as',1,2,'f',3]
filter_list(l)

# Add decimal #'s & convert to binary
def add_binary(a,b):
    return bin(a+b).replace("0b", "")
    # ORRRRrrrr
    return bin(a+b)[2:]
add_binary(12,4)
