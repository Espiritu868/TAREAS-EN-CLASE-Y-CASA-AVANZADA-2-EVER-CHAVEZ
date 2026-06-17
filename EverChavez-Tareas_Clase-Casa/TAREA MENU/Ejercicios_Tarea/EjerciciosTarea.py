import os
def limpiar_pantalla():
    os.system('cls')


#01 CALCULADORA DE RESTAURANTE

def EjercicioPractico1():
    limpiar_pantalla()
    print("-------------------------------------------------")
    print("CALCULADORA PARA RESTAURANTE")
    valorPizza = 12.50
    valorTacos = 8.25

    cantPizza = int(input("Ingrese pizzas totales: "))
    cantTacos = int(input("Ingrese tacos totales: "))

    costoPizza = valorPizza * cantPizza
    costoTacos = valorTacos * cantTacos

    print("-------------------------------------------------")

    print(f"COSTO TOTAL PIZZAS: {costoPizza}")
    print(f"COSTO TOTAL TACOS: {costoTacos}")
    print(f"COSTO TOTAL TOTAL: {costoPizza + costoTacos}")

    print("-------------------------------------------------")

#02 PERFIL DE MEMBRESIA

def EjercicioPractico2():
    limpiar_pantalla()
    nombre = "EVER ROLANDO CHAVEZ RAMIREZ"
    pesoKg = 73.64
    membresia = True

    print("Nombre de usuario: ", nombre)
    print("Peso de usuario: ", pesoKg)
    print("Membresia: ", membresia)
    print("Tipo de dato membresia:", type(membresia))

#03 CLASIFICACION DE MOTOCICLETAS

def EjercicioPractico3():
    limpiar_pantalla()
    cilindrada = int(input("Ingrese numero de cilindrada: "))
    if cilindrada >= 400:
        limpiar_pantalla()
        print("Tu moto es de alto rendimiento")
    else:
        print("Tu moto es eficiente para uso diario")

#04 PAR O IMPAR

def EjercicioPractico4():
    esPar = False
    numero = int(input("Ingrese un numero entero: "))

    if numero % 2 == 0:
        esPar = True

    if esPar:
        saber = "Par"
    else:
        saber = "Impar"

    print(f"El numero {numero} es: {saber}")

#05 DIAGNOSTICO TECNICO

def EjercicioPractico5():
    salir = True
    while True:
        print("INGRESE UNA DE LAS SIGUIENTES OPCIONES: ")
        print("1. Smartphones")
        print("2. Computadoras")
        print("3. Impresoras")
        print("4. Salir")

        opcion = int(input("Ingrese su opcion: "))
        match opcion:

            case 4:
                break
            case 1:
                os.system('cls')
                print("PANEL SMARTPHONES")
                print("Pantalla esta rota? Y/N")
                opcion = input("")
                if opcion == "Y" or opcion == "y":
                    print("Costo de cambio de pantalla = L.1,300.00")
                    input("")
                if opcion == "N" or opcion == "n":
                    print("Revisar Puerto de Carga.")
                    input("")

            case 2:
                limpiar_pantalla()
                print("PANEL COMPUTADORAS")
                print("Enciende? Y/N")
                opcion = input("")

                if opcion == "Y" or opcion == "y":
                    print("Revisar Sistema Operativo")
                    input("")
                if opcion == "N" or opcion == "n":
                    print("Diagnosticar Placa Base")
                    input("")

            case 3:
                limpiar_pantalla()
                print("Aplicar Mantenimiento General de Rodillos")
                input("")

            case _:
                print("Opcion Invalida")
                input("")
#06 CALIFICACIONES

def EjercicioPractico6():
    while True:
        nota = int(input("Ingrese numero de nota (o -1 para salir): "))

        if nota == -1:
            print("¡Cerrando!")
            break
        if 90 <= nota <= 100:
            print("Sobresaliente")
        elif 80 <= nota < 90:
            print("Muy Bueno")
        elif 70 <= nota < 80:
            print("Bueno")
        elif 0 <= nota < 70:
            print("Requiere mejorar")
        else:
            print("Nota no válida. Ingrese un valor entre 0 y 100.")

        print("-" * 20)

#07 Inventario de Repuestos (listas)

def EjercicioPractico7():
    repuestos = ["baterias", "pantallas", "centros de carga", "camaras", "flex encendido"]
    print("---------------")
    print("lista de repuestos: ")
    print(repuestos)
    print(" ")
    print("---------------")

    repuestos.append("microfono")

    del repuestos[1]
    print("lista de repuestos actual:")
    print(repuestos)
    print("---------------")

#08 Impresion de un numero en listas

def EjercicioPractico8():
    numeros = [1,2,3,4,5]

    print(numeros[0] + numeros[2] +numeros[4])

#09 Listas de consolas

def EjercicioPractico9():
    consolas = ["PlayStation 3", "Nintendo 64", "Super Nintendo"]
    print(consolas[0])
    print(consolas[1])
    print(consolas[2])
    emular = input("Ingrese consola: ")
    tiene_bios = True

    if emular in consolas:
        if tiene_bios == True:
            print("Iniciando emulador...")
        else:
            print("Falta archivo de sistema para iniciar")
    else:
        print("Consola no instalada")

#10 CONTRASEÑAS
def EjercicioPractico10():
    passw = []

    for i in range(3):
        password = input(f"Ingrese contraseña #{i+1}: ")
        passw.append(password)

    print("Final", passw)
