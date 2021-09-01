print("sistemas para calcular el promedio de un alumno")

nombre = input("para comenzar, ¿cual es tu nombre?: ")

matematicas = int(input(nombre +" ¿cual es tu calificacion en matematicas?: "))
lenguaje = int(input(nombre +" ¿cual es tu calificacion en lenguaje?: "))
quimica = int(input(nombre +" ¿cual es tu calificacion en quimica?: "))
sociales = int(input(nombre +" ¿cual es tu calificacion en sociales?: "))

promedio = (matematicas + lenguaje + quimica + sociales) / 4

#para quitar decimales y convertirlo en entero
promedio = int(promedio)
#fin

if promedio >= 7:
    print('felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)

else:
    print("Que mal " + nombre + ' "Reprobaste" con un promedio de: ', promedio)


print("fin.")





