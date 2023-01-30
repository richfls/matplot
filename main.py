import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

#example 1
# for i in range(-10,11,1):
#     x.append(((-1*(2/5))*i)+3)

# for i in range(-10,11,1):
#     y.append(i)
#example 2
#for i in range(-10,11,1):
    #x.append(np.absolute(i))

#for i in range(-10,11,1):
    #y.append(i)
#example 3
#for i in range(-10,11,1):
    #x.append(-1*(i**2)+(2*i)+3)

#for i in range(-10,11,1):
    #y.append(i)
#example 11
#for i in range(-10,11,1):
    #x.append(i**3)

#for i in range(-10,11,1):
    #y.append(i)
#example 15
for i in np.arange(-10,11,.01):
    x.append(1/np.cos(i))

for i in np.arange(-10,11,.01):
    y.append(i)
plt.plot(y,x)
plt.show()
