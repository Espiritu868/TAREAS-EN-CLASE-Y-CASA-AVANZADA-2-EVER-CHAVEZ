class Formulas:
    def CelsiusAFahrenheit():
        c = float(input("Ingrese valor en ºC: "))
        f = c * 1.8 + 32
        print(f"ºC a ºF es: {f}")

    def CelsiusAKelvin():
        c = float(input("Ingrese valor en ºC: "))
        k = c + 273.15
        print(f"ºC a ºK es: {k}")

    def CelsiusARankine():
        c = float(input("Ingrese valor en ºC: "))
        r = (c + 273.15) * 1.8
        print(f"ºC a ºR es: {r}")

    def FahrenheitACelsius():
        f = float(input("Ingrese valor en ºF: "))
        c = (f - 32) / 1.8
        print(f"ºF a ºC es: {c}")

    def FahrenheitAKelvin():
        f = float(input("Ingrese valor en ºF: "))
        k = (f + 459.67) / 1.8
        print(f"ºF a K es: {k}")

    def FahrenheitARankine():
        f = float(input("Ingrese valor en ºF: "))
        r = f + 459.67
        print(f"ºF a ºR es: {r}")

    def KelvinACelsius():
        k = float(input("Ingrese valor en ºK: "))
        c = k - 273.15
        print(f"ºK a ºC es: {c}")

    def KelvinAFahrenheit():
        k = float(input("Ingrese valor en ºK: "))
        f = (9 * k) - 459.67
        print(f"ºK a F es: {f}")

