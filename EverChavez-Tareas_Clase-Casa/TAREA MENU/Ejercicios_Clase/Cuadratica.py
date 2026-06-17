from Ejercicios_Clase.EcuacionCuadraticaConImaginarios import cuadratica


class Cuadratica:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def raices(self):
        # Para a = 0 se convierte en ecuacion lineal
        if self.a == 0 and self.b != 0:
            print("ES UNA ECUACION LINEAL")
            print(f"x = {self / c / self.b}")
        if self.c == 0 and self.b != 0:
            print("ES UNA ECUACION LINEAL")
            print(f"x = {self / c / self.b}")

        if self.a != 0 and self.b != 0:
            if self.delta() > 0:
                x1 = (-self.b + self.delta() ** 0.5) / (2 * self.a)
                x2 = (-self.b - self.delta() ** 0.5) / (2 * self.a)
                print(x1)
                print(x2)

            else:
                parteReal = -self.b/(2*self.a)
                parteCompleja = abs(self.delta())**0.5/(2*self.a)
                print(f"x1 = {parteReal} + {parteCompleja}i")
                print(f"x2 = {parteReal} - {parteCompleja}i")