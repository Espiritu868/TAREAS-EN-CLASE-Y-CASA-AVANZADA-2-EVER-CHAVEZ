import pandas as pd
from array import array

# Arreglo 
edades = array('i', [18, 19, 20, 18])

#lista
estudiantes = ["Carlos", "Ana", "Luis", "Maria"]
# Diccionario
notas = {"Carlos": 85, "Ana": 92, "Luis": 78, "Maria": 90}

print("Lista de estudiantes:", estudiantes)
print("\nDiccionario de notas:", notas)
print("\nArreglo de edades:", edades)

print("\nRECORRIDO DE DATOS:")
for i in range(len(estudiantes)):
    nombre = estudiantes[i]
    nota = notas[nombre]
    edad = edades[i]

    print(f"Estudiante: {nombre}, Nota: {nota}, Edad: {edad}")

print("\n Agregando un nuevo estudiante:")
estudiantes.append("Pedro")
notas["Pedro"] = 88
edades.append(21)

print("\nRECORRIDO DE DATOS:")
for i in range(len(estudiantes)):
    nombre = estudiantes[i]
    nota = notas[nombre]
    edad = edades[i]

    print(f"Estudiante: {nombre}, Nota: {nota}, Edad: {edad}")