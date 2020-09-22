import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**2 + 4*x - 4

def g(x):
    return 6*x + 4

def newtonRaphson(x0,e,N):
    print('\nNewton Raphson metoden:')
    step = 1
    flag = 1
    condition = True

    while condition:
        if(g(x0) == 0.0):
            print("kan ikke dele på 0")
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iterasjon-%d, x1 = %0.12f og f(x1) = %0.12f' % (step, x1, f(x1)))
        x0 = x1
        step= step + 1

        if step > N:
            flag = 0
            break

        condition= abs(f(x1)) > e

    if flag == 1:
        print('\nDet ene nullpunktet er i: %0.12f' % x1)
    else:
        print("\nIkke konvergent.")

x0 = input("Antagelse: ")
e = 10**(-12)
N = input("Max iterasjoner: ")

x0 = float(x0)
e = float(e)
N = int(N)

newtonRaphson(x0,e,N)