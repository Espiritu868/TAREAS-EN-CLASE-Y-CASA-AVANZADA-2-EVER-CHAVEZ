from Ejercicios_Clase.EjercicioConversionGrados import Formulas

opcion = True
while(True):
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
            opcion = False

        case 1:
            Formulas.CelsiusAFahrenheit()
            input("Ingrese una tecla para continuar ")

        case 2:
            Formulas.CelsiusAKelvin()
            input("Ingrese una tecla para continuar ")
        case 3:
            Formulas.CelsiusARankine()
            input("Ingrese una tecla para continuar ")
        case 4:
            Formulas.FahrenheitACelsius()
            input("Ingrese una tecla para continuar ")
        case 5:
            Formulas.FahrenheitAKelvin()
            input("Ingrese una tecla para continuar ")
        case 6:
            Formulas.FahrenheitARankine()
            input("Ingrese una tecla para continuar ")
        case 7:
            Formulas.KelvinACelsius()
            input("Ingrese una tecla para continuar ")
        case 8:
            Formulas.KelvinAFahrenheit()
            input("Ingrese una tecla para continuar ")
        case _:
            print("---------------------------------------------")
            print("")
            print("Opcion invalida")
            print("")
            print("--------------------------------------------")