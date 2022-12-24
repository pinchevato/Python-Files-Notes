#!/usr/bin/python3.8
## https://youtu.be/_uQrJ0TkZlc 1:49

print("Use nested loops to print coordinates")
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
    
# PRINT AN 'F' MADE OF X's
print("\nPrint an F made of x's\n")
nums = [5,2,5,2,2]
for i in nums:
    print(i*'x')
# Same thing using nested loops
print("\n..with nested loops\n")
for i in nums:
    exes = ''
    for j in range(i):
        exes += 'X'
    print(exes)
