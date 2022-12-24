#!/usr/bin/python3.8
## https://youtu.be/_uQrJ0TkZlc 1:31

x=""
car_state=False
while True:
    x = input("> ").lower()
    if x == "start":
        if not car_state:
            print("Car started.")
        else:
            print("Car is already on, stupid.")
        car_state = True
    elif x ==  "stop":
        if car_state:
            print("Car stopped.")
        else:
            print("Car is already off, idiot.")
        car_state = False
    elif x == "help":
# IMPORTANT NOTE: w triple quotes, code will be
# printed EXACTLY as is (INCLUDING INDENTS)
        print("""
start - starts car
stop - stops car
quit - exits game
        """)
    elif x == "quit":
        break
    else:
        print("You're not making any fukin sense dingus")
