import os
from coordenadas import info

_, lugares = info()

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    print("\n\n")
    print("+-------------------------------------+".center(70))
    print("|             MENÚ PRINCIPAL          |".center(70))
    print("+-------------------------------------+".center(70))
    
    for id_lugar, lugar in lugares.items():
        print(">", id_lugar + ".-", lugar["nombre"])
    
    while True:
        opcion = input("\nPor favor, elija una opción: ".center(70))
        if opcion.isdigit() and 1 <= int(opcion) <= 11:
            os.system('cls' if os.name == 'nt' else 'clear') 
            return int(opcion)
        else:
            print("+------------------------------------------+".center(70))
            print("| Por favor, elija una opción del 1 al 11 |".center(70))
            print("+------------------------------------------+".center(70))
