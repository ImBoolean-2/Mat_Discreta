from menu import menu
from Calculador_Distancia import calcular_distancia

print("Ingrese el putno de partida".center(70))
partida =   menu()
print("Ingrese el punto de llegada".center(70))
llegada =   menu()

calcular_distancia(partida, llegada)  