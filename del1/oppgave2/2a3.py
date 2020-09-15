import numpy as np
import matplotlib.pyplot as plt 

rangemin = -2
rangemax = 2

def f(x):
    return (1-x)/((x+3)**2)


x=np.linspace(rangemin,rangemax,1000)
y=f(x)
plt.grid(True)
plt.plot(x,y)
plt.show()