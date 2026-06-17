from Ejercicios_Clase import Ejercicio1
from Ejercicios_Clase import Ejercicio2
from Ejercicios_Clase import Ejercicio3
from Ejercicios_Clase import Ejercicio4
from Ejercicios_Clase import Ejercicio5
from Ejercicios_Clase import Cuadratica
from Ejercicios_Clase import EjercicioConversionGrados


from Ejercicios_Tarea import EjerciciosTarea


while True:
    print("MENU DE EJERCICIOS")
    print("1. EJERCICIOS CLASE")
    print("2. EJERCICIOS CASA")
    print("0. SALIR")

    opcion = int(input("Ingrese su opcion: "))
    match opcion:
        case 0:
            print("CERRANDO EL PROGRAMA.....")
            break

        case 1:
            print("1. Ejercicio 1")
            print("2. Ejercicio 2")
            print("3. Ejercicio 3")
            print("4. Ejercicio 4")
            print("5. Ejercicio 5")
            print("6. Ejercicio 6")
            print("7. Conversion Grados")
            print("0. Regresar")
            opcion = int(input("Ingrese su opcion: "))

            match opcion:
                case 0:
                    print("CERRANDO EL PROGRAMA.....")
                    break

                case 1:
                    Ejercicio1.ejercicioClase1()
                    input("Ingrese una tecla para continuar ")

                case 2:
                    Ejercicio2.EjercicioClase2()
                    input("Ingrese una tecla para continuar ")

                case 3:
                    Ejercicio3.EjercicioClase3()
                    input("Ingrese una tecla para continuar ")

                case 4:
                    Ejercicio4.EjercicioClase4()
                    input("Ingrese una tecla para continuar ")

                case 5:
                    Ejercicio5.EjercicioClase5()
                    input("Ingrese una tecla para continuar ")

                case 6:
                    Cuadratica.cuadratica(1,0,-1)
                    input("Ingrese una tecla para continuar ")

                case 7:
                    print("1. ºC a ºF")
                    print("2. ºC a ºK")
                    print("3. ºC a ºR")
                    print("4. ºF a ºC")
                    print("5. ºF a ºK")
                    print("6. ºF a ºR")
                    print("7. ºK a ºC")
                    print("8. ºK a ºF")
                    opcion = int(input("Ingrese su opcion: "))

                    match opcion:
                        case 0:
                            print("CERRANDO EL PROGRAMA.....")
                            input("Ingrese una tecla para continuar ")

                        case 1:
                            Formulas.CelsiusAFahrenheit()
                            input("Ingrese una tecla para continuar ")



                case _:
                    print("---------------------------------------------")
                    print("")
                    print("Opcion invalida")
                    print("")
                    print("--------------------------------------------")
        case 2:
            print("1. Ejercicio 1")
            print("2. Ejercicio 2")
            print("3. Ejercicio 3")
            print("4. Ejercicio 4")
            print("5. Ejercicio 5")
            print("6. Ejercicio 6")
            print("7. Ejercicio 7")
            print("8. Ejercicio 8")
            print("9. Ejercicio 9")
            print("10. Ejercicio 10")
            print("0. Regresar")

            opcion = int(input("Ingrese su opcion: "))

            match opcion:
                case 0:
                    print("CERRANDO EL PROGRAMA.....")
                    input("Ingrese una tecla para continuar ")

                case 1:
                    EjerciciosTarea.EjercicioPractico1()
                    input("Ingrese una tecla para continuar ")

                case 2:
                    EjerciciosTarea.EjercicioPractico2()
                    input("Ingrese una tecla para continuar ")

                case 3:
                    EjerciciosTarea.EjercicioPractico3()
                    input("Ingrese una tecla para continuar ")

                case 4:
                    EjerciciosTarea.EjercicioPractico4()
                    input("Ingrese una tecla para continuar ")

                case 5:
                    EjerciciosTarea.EjercicioPractico5()
                    input("Ingrese una tecla para continuar ")

                case 6:
                    EjerciciosTarea.EjercicioPractico6()
                    input("Ingrese una tecla para continuar ")

                case 7:
                    EjerciciosTarea.EjercicioPractico7()
                    input("Ingrese una tecla para continuar ")

                case 8:
                    EjerciciosTarea.EjercicioPractico8()
                    input("Ingrese una tecla para continuar ")

                case 9:
                    EjerciciosTarea.EjercicioPractico9()
                    input("Ingrese una tecla para continuar ")

                case 10:
                    EjerciciosTarea.EjercicioPractico10()
                    input("Ingrese una tecla para continuar ")

                case _:
                    print("---------------------------------------------")
                    print("")
                    print("Opcion invalida")
                    print("")
                    print("--------------------------------------------")

        case _:
            print("---------------------------------------------")
            print("")
            print("Opcion invalida")
            print("")
            print("--------------------------------------------")