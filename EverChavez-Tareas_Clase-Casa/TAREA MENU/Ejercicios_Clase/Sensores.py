# sensor1 = True
# sensor2 = False
# sensor3 = True
# sensor4 = False
#
# for falla in range (4):
#     identificador = 0
#     if sensor1:
#         identificador += 1
#
#     if sensor2:
#         identificador += 1
#
#     if sensor3:
#         identificador += 1
#
#     if sensor4:
#         identificador += 1
#
#
# if sensor1:
#     print("sensor 1 en fallo")
#
# if sensor2:
#     print("sensor 2 en fallo")
#
# if sensor3:
#     print("sensor 3 en fallo")
#
# if sensor4:
#     print("sensor 4 en fallo")
#
# if(identificador == 0):
#     print("El sistema no ha detectado errores.")
# if(identificador == 1):
#     print("Falla Leve")
# if(identificador == 2):
#     print("Falla indeterminada")
# if(identificador == 3):
#     print("Falla indeterminada")
# if(identificador == 4):
#     print("Falla Critica")


print("------------------------------------")
print("PRUEBA 2, RECORTADO")
print("------------------------------------")

sensores = [True,False,True,True]
acumulador = 0
for i in sensores:
    if sensores[i] == True:
        print(f"sensor {i+1} en falla")
        acumulador += 1

if(acumulador == 0):
    print("El sistema no ha detectado errores.")
if(acumulador == 1):
    print("Falla Leve")
if(acumulador == 2):
    print("Falla indeterminada")
if(acumulador == 3):
    print("Falla indeterminada")
if(acumulador == 4):
    print("Falla Critica")





