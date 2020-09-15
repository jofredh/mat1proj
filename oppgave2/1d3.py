import numpy as np
import matplotlib.pyplot as plt 

x0 = 1
min = -2
max = 2

def f(x):
    return (x-5)/(x+3)**3

def g(x):
    return np.longdouble((F(x0+x)-F(x0))/x)

def G(x):
    return 0.1+np.longdouble((F(x+0.32389)-F(x))/0.32389)

def F(x):
    return (1-x)/((x+3)**2)


for x in np.arange(0,0.1,0.000001):
    Ex = abs(f(x0)-g(x))
    if(Ex<=0.001):
        print("F:{0}, G:{1}, f:{2}, E:{3}, x:{4}".format(F(x0+x),g(x),f(x0),Ex,x))
    elif(Ex>0.001):
        break

fig = plt.gcf()
fig.canvas.set_window_title('Funksjon 3: (1-x)/(x+3)²')
x=np.linspace(min,max,1000)
y=F(x)
yd=f(x)
yg=G(x)
ye=abs(f(x0)-g(x))
plt.grid(True)
plt.plot(x,yd,'r-', label='f \'(x)')
plt.plot(x,y,'g-',label="f (x)")
plt.plot(x,yg,'b-',label="g (x)")
plt.plot(x,ye,color='purple',label='E (x)')
plt.legend()    
plt.show()