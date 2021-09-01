print("sistemas para calcular el promedio de un alimno")

nombre = input("para comenzar, ¿cual es tu nombre?: ")

matematicas = int(input(nombre +" ¿cual es tu calificacion en matematicas?: "))
lengua = int(input(nombre +" ¿cual es tu calificacion en lengua española?: "))
quimica = int(input(nombre +" ¿cual es tu calificacion en quimica?: "))
sociales = int(input(nombre +" ¿cual es tu calificacion en sociales?: "))

promedio = (matematicas + lengua + quimica + sociales) / 4

print (promedio)






