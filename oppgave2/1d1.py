import numpy as np
import matplotlib.pyplot as plt 

x0 = 1
min = 0
max = 2

def f(x):
    return (14*x) - 8

def g(x):
    return np.longdouble((F(x0+x)-F(x0))/x)

def G(x):
    return 0.5+np.longdouble((F(x+0.00014)-F(x))/0.00014)
    #+0.5 for å flytte grafen litt opp fra f'

def F(x):
    return 7*x**2 -8*x +1


for x in np.arange(0,0.001,0.000001):
    Ex = abs(f(x0)-g(x))
    if(Ex<=0.001):
        print("F:{0}, G:{1}, f:{2}, E:{3}, x:{4}".format(F(x0+x),g(x),f(x0),Ex,x))
    elif(Ex>0.001):
        break


fig = plt.gcf()
fig.canvas.set_window_title('Funksjon 1: 7x² - 8x + 1')
x=np.linspace(min,max,1000)
y=F(x)
yd=f(x)
yg=G(x)
ye=abs(f(x0)-g(x))
plt.grid(True)
plt.plot(x,yd,'r-', label='f \'(x)')
plt.plot(x,y,'g-',label="f (x)")
plt.plot(x,yg,'b-',label="g (x) + 0.5")
plt.plot(x,ye,color='purple',label='E (x)')
plt.legend()    
plt.show()