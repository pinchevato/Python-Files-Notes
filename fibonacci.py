fib=[0, 1]
iter=25
for i in range(iter):
    fib.append(fib[i]+fib[i+1])
    
last_num=fib[iter]/fib[iter-1]
last_num2=fib[iter-1]/fib[iter-2]
print(str(iter) + " iterations")
print("The last two Fib ratios are\n" + str(last_num2) +
      "\nand\n" + str(last_num) + "\nOR RECIPROCALS:\n" +
      str(1/last_num2) + "\nand\n" + str(1/last_num))

import random
for i in range(5):
    print(random.randint(1,666))
