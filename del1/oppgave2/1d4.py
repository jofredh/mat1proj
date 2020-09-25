import numpy as np
import matplotlib.pyplot as plt 

x0 = 5
min = 0
max = 10

def f(x):
    return x/np.sqrt(1+x**2)

def g(dx,x=x0):
    return np.longdouble((F(x+dx)-F(x))/dx)

def G(x):
    return 0.5+np.longdouble((F(x+0.28)-F(x))/0.28)

def F(x):
    return np.sqrt(1+x**2)


for x in np.arange(0.275,max-x0,0.000001):
    Ex = abs(f(x0)-g(x))
    if(Ex<=0.001):
        valid=x
        #print("F:{0}, G:{1}, f:{2}, E:{3}, x:{4}".format(F(x0+x),g(x),f(x0),Ex,x))
    elif(Ex>0.001):
        break

i=0
E = [0]*1000
for x in np.linspace(min,max,1000):
    E[i] = 5*np.longdouble(abs(f(x)-g(x=x,dx=valid)))
    i+=1


fig = plt.gcf()
fig.canvas.set_window_title('Funksjon 4: sqrt(1+x²)')
x=np.linspace(min,max,1000)
y=F(x)
yd=f(x)
yg=G(x)
ye=E
plt.grid(True)
plt.plot(x,yd,'r-', label='f \'(x)')
plt.plot(x,y,'g-',label="F (x)")
plt.plot(x,yg,'b-',label="g (x)")
plt.plot(x,ye,color='purple',label='5*E (x) for deltaX %.2f'%(valid))
plt.legend()    
plt.show()