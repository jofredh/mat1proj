import numpy as np
import matplotlib.pyplot as plt 

x0 = 5
min = 0
max = 10

def f(x):
    return x/np.sqrt(1+x**2)

def g(x):
    return np.longdouble((F(x0+x)-F(x0))/x)

def g(x):
    return np.longdouble((F(x0+x)-F(x0))/x)

def F(x):
    return np.sqrt(1+x**2)


for x in np.arange(0.275,max-x0,0.000001):
    Ex = abs(f(x0)-g(x))
    if(Ex<=0.001):
        print("F:{0}, G:{1}, f:{2}, E:{3}, x:{4}".format(F(x0+x),g(x),f(x0),Ex,x))
    elif(Ex>0.001):
        break

fig = plt.gcf()
fig.canvas.set_window_title('Funksjon 4: sqrt(1+x²)')
x=np.linspace(min,max,1000)
y=F(x)
yd=f(x)
yg=g(x)
ye=abs(f(x0)-g(x))
plt.grid(True)
plt.plot(x,yd,'r-', label='f \'(x)')
plt.plot(x,y,'g-',label="f (x)")
plt.plot(x,yg,'b-',label="g (x)")
plt.plot(x,ye,color='purple',label='E (x)')
plt.legend()    
plt.show()