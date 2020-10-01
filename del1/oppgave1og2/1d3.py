import numpy as np
import matplotlib.pyplot as plt 

x0 = 1
min = -2
max = 2

def f(x):
    return (x-5)/(x+3)**3

def g(dx,x=x0):
    return np.longdouble((F(x+dx)-F(x))/dx)

def G(x):  #To funksjoner for tilnærmingen g fordi dette gjør det enklere å tegne grafen separert fra f'
    return np.longdouble((F(x+0.32389)-F(x))/0.32389)#DeltaX hardkodet inn etter funn i Del1:Oppgave1D

def F(x):
    return (1-x)/((x+3)**2)


for x in np.arange(0.032,0.1,0.000001):#Loop for å finne største gyldige DeltaX for E<=0.001. Loop grenser og stepsize funnet ved prøv&feil
    Ex = abs(f(x0)-g(x))
    if(Ex<=0.001):
        valid=x
        #print("F:{0}, G:{1}, f:{2}, E:{3}, x:{4}".format(F(x0+x),g(x),f(x0),Ex,x))#Fjern '#' tegnet foran denne linjen for å kjøre koden med printing av E og deltaX
    elif(Ex>0.001):
        break

i=0
E = [0]*1000
for x in np.linspace(min,max,1000): #Loop for å beregne variasjon i E over et gitt intervall min -> max
    E[i] = np.longdouble(abs(f(x)-g(x=x,dx=valid)))
    i+=1

fig = plt.gcf()
fig.canvas.set_window_title('Funksjon 3: (1-x)/(x+3)²')
x=np.linspace(min,max,1000)
y=F(x)
yd=f(x)
yg=G(x)
ye=E
plt.grid(True)
plt.plot(x,yd,'r-', label='f \'(x)')
plt.plot(x,y,'g-',label="F (x)")
plt.plot(x,yg,'b-',label="g (x)")
plt.plot(x,ye,color='purple',label='E (x) for deltaX %.3f'%(valid))
plt.legend()    
plt.show()