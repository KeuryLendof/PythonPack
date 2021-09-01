#def timeConvert
num = int(input("Introduzca su cantidad de minutos: "))
minutos = num % 60
print ("minutos: ", minutos)
horas = (num - minutos)/60
print ("horas: ", horas)
result = str(horas) + " horas" + " Con " + str(minutos) + " min"

print (result)
