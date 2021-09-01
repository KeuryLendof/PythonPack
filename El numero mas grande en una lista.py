my_list = []

numeros =int(input("introduzca la cantidad de numeros que tendra la lista: "))

for i in range (numeros):
    list_cant = int(input("Introduzca los elementos de su lista: "))
    my_list.append (list_cant)

print ("Lista original: ", my_list)
my_list.sort()

print ("lista organizada: ", my_list)
print("El numero mas grande es: ", my_list[-1])
