def menu_selection():
    print(4 * ".", "Convertir km a millas y millas a kilometros")
    print("Selecciona tu tipo de conversion")
    print("[ 1 ] km a millas")
    print("[ 2 ] millas a km")

main_loop = True
while not main_loop == False:
    menu_selection()
    user_selection = str(input("Escoja su seleccion [1 or 2]: "))

    if(user_selection == "1"):
        user_in_km = int(input("Por favor entre la cantidad de kilometros que desea convertir: "))
        to_miles = round (user_in_km / 1.6093, 2)
        
        print("{} km convertido a {} millas! ".format(user_in_km, to_miles))
        
        
    elif(user_selection == "2"):
        user_in_miles = int(input("Por favor entre la cantidad de millas que desea convertir: "))
        to_kilometers = round (user_in_miles * 1.6093, 2)

        print("{} millas convertidas a {} km! ".format(user_in_miles, to_kilometers))
        

         
        
   
