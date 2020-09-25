'''
Denne koden tregner 2 input fra brukeren. Den trenger en startverdi på hvor
man tror det ene nullpunktet er. Og det trenger en mengde iterasjoner den
maksimalt skal gjenta seg, før den sier at det ikke konvergerer.
Hvis startverdien er nærme nok til at det kommer innenfor feilmarginen
før antall iterasjoner er nådd vil den si hvor nullpunktet er.
'''

import numpy as np
import matplotlib.pyplot as plt
import math

x0 = input("Startverdi: ")
e = 10**(-12)
N = 100

x0 = float(x0)
e = float(e)
N = int(N)
x = x0
cos = math.cos
sin = math.sin

def f(x):
    return (10 - (-2 + 8.5*cos(x)))**2 + (6 - (8.5*sin(x)))**2 - 49

def g(x):
    return -102*cos(x) + 204*sin(x)

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

newtonRaphson(x0,e,N)