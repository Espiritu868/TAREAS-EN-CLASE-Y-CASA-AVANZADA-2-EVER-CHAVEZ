#Promedio de 4 notas con excepcion de 0

def EjercicioClase4():
    print("Ejercicio Clase 4")
    print("Promedio de 4 notas con excepcion de 0")

    n = 0
    notaFinal = 0

    for i in range(1, 5):
        n = int(input(f"Ingrese nota {i}: "))
        while(n == 0):
            print("Ingrese una nota correcta")
            n = int(input(f"Ingrese nota {i} "))
        notaFinal += n

    promedio = notaFinal / 4
    print("Promedio es: ", promedio)

