print ("Contador")

def Contador_par_impar(max_arr, arr_values):
    count_par = 0
    count_impar = 0

    par_impar = []

    for i in range (max_arr):
        if (arr_values[i] % 2 == 0):
            count_par += 1
        else:
            count_impar += 1
            
    par_impar.append(count_par)
    par_impar.append(count_impar)

    print ("Par: {} | Impar: {}".format(par_impar[0], par_impar[1]))

Contador_par_impar(5,[2, 4, 6, 2, 8])
