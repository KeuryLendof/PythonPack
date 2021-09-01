print("Introduzca la distancia recorrida en kilometros")
lunes = float(input("Introduzca la distancia recorrida el lunes: "))
martes = float(input("Introduzca la distancia recorrida el martes: "))
miercoles = float(input("Introduzca la distancia recorrida el miercoles: "))
jueves = float(input("Introduzca la distancia recorrida el jueves: "))
viernes = float(input("Introduzca la distancia recorrida el viernes: "))
sabado = float(input("Introduzca la distancia recorrida el sabado: "))
domingo = float(input("Introduzca la distancia recorrida el domingo: "))

promedio = (lunes + martes + miercoles + jueves + viernes + sabado + domingo) / 7
promedio = float(promedio)

print("El promedio de distancia recorrida durante la semana es de : {} Kilometros".format(round(promedio, 2)))

arreglo =[lunes , martes , miercoles , jueves , viernes , sabado , domingo]

dia_mayor = max(arreglo)
print ("El dia que mas recorrio fue: {} kilometros".format(dia_mayor))
if dia_mayor == arreglo[0]:
    print("Esto fue el dia lunes")
if dia_mayor == arreglo[1]:
    print("Esto fue el martes")
if dia_mayor == arreglo[2]:
    print("Esto fue el miercoles")
if dia_mayor == arreglo[3]:
    print("Esto fue el jueves")
if dia_mayor == arreglo[4]:
    print("Esto fue el viernes")
if dia_mayor == arreglo[5]:
    print("Esto fue el sabado")
if dia_mayor == arreglo[6]:
    print("Esto fue el domingo")


dia_menor = min(arreglo)
print ("El dia que menos recorrio fue: {} kilometros".format(dia_menor))
if dia_menor == arreglo[0]:
    print("Esto fue el dia lunes")
if dia_menor == arreglo[1]:
    print("Esto fue el martes")
if dia_menor == arreglo[2]:
    print("Esto fue el miercoles")
if dia_menor == arreglo[3]:
    print("Esto fue el jueves")
if dia_menor == arreglo[4]:
    print("Esto fue el viernes")
if dia_menor == arreglo[5]:
    print("Esto fue el sabado")
if dia_menor == arreglo[6]:
    print("Esto fue el domingo")

peso = float(input("Ingrese su peso en libras: "))
altura = float(input("Ingrese su altura en metros : "))

IMC = (peso/altura*altura)

print("El indice de masa corpolar del atleta es : {}".format(round(IMC, 2)))

print("Fin")
