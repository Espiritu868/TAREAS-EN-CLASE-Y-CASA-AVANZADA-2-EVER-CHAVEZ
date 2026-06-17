#Factorial de un numero
def EjercicioClase5():
    print("Ejercicio Clase 5")
    print("FACTORIAL DE UN NUMERO")

    acumulador = 1

    numero = int(input("Ingrese numero para factorial: "))

    for i in range(1, numero + 1):
        acumulador *= i


    print(f"{numero}! = {acumulador}")










