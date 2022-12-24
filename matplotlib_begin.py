import numpy as np
import matplotlib.pyplot as plt
 
# create data
x = np.linspace(1, 50, 50)
np.random.seed(1)
y = np.random.randint(0, 20, 50)
 
# plot graph
plt.plot(x, y)
 
# add legend
plt.legend(['Legend'], loc=3)
plt.show()

z=1/x
plt.plot(x,z)
plt.show()
