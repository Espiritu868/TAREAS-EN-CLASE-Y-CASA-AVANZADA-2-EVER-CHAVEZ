#RESOLVER UNA ECUACION CUADRATICA CON CASOS POSIBLES IMAGINARIOS O REALES

import math

#FORMULA: ax^2+bx+c=0
#FORMULA 2: Delta = b^2-4ac

def cuadratica(a,b,c):
    Discriminante = b**2 - 4*a*c

    print("SOLUCION DE ECUACION CUADRATICA")
    if Discriminante > 0:
        x1=(-b+Discriminante**0.5)/(2*a)
        x2=(-b-Discriminante**0.5)/(2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    if Discriminante < 0:
        parteReal = -b/(2*a)
        parteCompleja = abs(Discriminante)**0.5/(2*a)
        print(f"x = {parteReal} + {parteCompleja}i")
        print(f"x = {parteReal} - {parteCompleja}i")

cuadratica(0,0,4)
