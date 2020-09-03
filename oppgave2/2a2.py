import numpy as np
import matplotlib.pyplot as plt 

rangemin = 0
rangemax = 2*np.pi

def f(x):
    return np.sin(x)


x=np.linspace(rangemin,rangemax,1000)
y=f(x)
plt.grid(True)
plt.plot(x,y)
plt.show()