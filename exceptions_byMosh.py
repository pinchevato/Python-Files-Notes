try:
    height = int(input('Height: '))
    weight = int(input('Weight: '))
    bmi = weight / (height**2)
    print(bmi)
except ValueError:
    print("write a number, shitbird.")
except ZeroDivisionError:
    print("You must weigh something, ya scrotum!")
