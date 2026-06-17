#Calcular promedio de 4 notas

def EjercicioClase2():
    print("Ejercicio Clase 2")
    acumulador = 0
    print("Promedio de 4 notas: ")

    for i in range(4):
        nota = int(input("Nota " + str(i+1) + ": "))
        if nota == 0:
            print("No se puede generar promedio, reingrese nota:")
            break

        else:
            acumulador += nota

    if nota != 0:
        prom = acumulador / 4
        print("Promedio de 4 notas: ")
        print(prom)




