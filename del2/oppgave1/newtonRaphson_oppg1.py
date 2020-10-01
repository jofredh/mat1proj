'''
Denne koden tregner 1 input fra brukeren. Den trenger en startverdi på hvor
man tror det ene nullpunktet er. Hvis startverdien er nærme nok til at det kommer innenfor feilmarginen
før antall iterasjoner er nådd vil den si hvor nullpunktet er.

Hvis man ikke skulle komme frem til nullpunktet innen antallet iterasjoner jeg har lagt inn i koden
kan man i praksis øke dette tallet, men man har generelt valgt en dårlig start verdi om den skulle trenge
flere itersajoner...
'''

def f(x):
    return 3*x**2 + 4*x - 4

def g(x):
    return 6*x + 4

def newtonRaphson(x0,e,I):
    print('\nNewton Raphson metoden:')
    step = 1
    flag = 1
    condition = True

    while condition:
        if(g(x0) == 0.0): # Hvis startverdien vi skriver inn gjør den deriverte lik 0 stopper koden, kan ikke dele på 0
            print("kan ikke dele på 0")
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iterasjon-%d, x1 = %0.12f og f(x1) = %0.12f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > I:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nDet ene nullpunktet er i: %0.12f' % x1)
    else:
        print("\nIkke konvergent.")

x0 = input("Startverdi: ") #Startverdi
e = 10**(-12) #max tillatte feilen
I = 100 #Max antall iterasjoner

x0 = float(x0)
e = float(e)
I = int(I) 

newtonRaphson(x0,e,I)