import numpy as np
import matplotlib.pyplot as plt 

rangemin = 0
rangemax = 10

def f(x):
    return np.sqrt(1+x**2)


x=np.linspace(rangemin,rangemax,1000)
y=f(x)
plt.grid(True)
plt.plot(x,y)
plt.show()