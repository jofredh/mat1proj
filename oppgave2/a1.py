import numpy as np
import matplotlib.pyplot as plt 

rangemin = 0
rangemax = 2

def f(x):
    return 7*x**2 -8*x +1


x=np.linspace(rangemin,rangemax,1000)
y=f(x)
plt.grid(True)
plt.plot(x,y)
plt.show()