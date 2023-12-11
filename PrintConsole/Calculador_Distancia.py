from coordenadas import info
import heapq
import matplotlib.pyplot as plt

def calcular_distancia(partida, llegada):
    aristas, lugares = info()
    partida = str(partida)  # Convertir los números enteros a cadenas
    llegada = str(llegada)
    distancias = {nodo: float('inf') for nodo in lugares}
    distancias[partida] = 0
    rutas = {nodo: [] for nodo in lugares}
    cola_prioridad = [(0, partida)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == llegada:
            break

        if distancia_actual == distancias[nodo_actual]:
            if nodo_actual in aristas:  # Comprueba si el nodo_actual existe en aristas
                for vecino, distancia in aristas[nodo_actual].items():
                    nueva_distancia = distancia_actual + distancia
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        rutas[vecino] = rutas[nodo_actual] + [nodo_actual]
                        heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
    
    ruta = rutas[llegada] + [llegada]
    distancia = distancias[llegada]

    
# Imprimir la ruta y la distancia
    print("╔════════════════════════════════════════════════════╗")
    print("║                  Resultado del cálculo             ║")
    print("╠════════════════════════════════════════════════════╣")
    print(f"║  La ruta es: {' -> '.join(ruta)}")
    print(f"║  La distancia total en kilómetros es: {round(distancia, 2)}")
    print("╚════════════════════════════════════════════════════╝")
    
    # Dibujar todos los nodos
    x_todos = [lugares[nodo]['longitud'] for nodo in lugares]
    y_todos = [lugares[nodo]['latitud'] for nodo in lugares]
    plt.scatter(x_todos, y_todos, color='lightgray')
    
    for nodo in lugares:
        plt.text(lugares[nodo]['longitud'], lugares[nodo]['latitud'], nodo)
    
    # Dibujar todas las conexiones en color gris claro
    for nodo_actual in aristas:
        for nodo_siguiente in aristas[nodo_actual]:
            x_conexion = [lugares[nodo_actual]['longitud'], lugares[nodo_siguiente]['longitud']]
            y_conexion = [lugares[nodo_actual]['latitud'], lugares[nodo_siguiente]['latitud']]
            plt.plot(x_conexion, y_conexion, color='lightgray')
    
    # Dibujar la ruta en un gráfico
    x_ruta = [lugares[nodo]['longitud'] for nodo in ruta]
    y_ruta = [lugares[nodo]['latitud'] for nodo in ruta]
    plt.plot(x_ruta, y_ruta, color='black', marker='o')
    
    for i in range(len(ruta) - 1):
        nodo_actual = ruta[i]
        nodo_siguiente = ruta[i + 1]
        peso_arista = aristas[nodo_actual][nodo_siguiente]
        x_medio = (lugares[nodo_actual]['longitud'] + lugares[nodo_siguiente]['longitud']) / 2
        y_medio = (lugares[nodo_actual]['latitud'] + lugares[nodo_siguiente]['latitud']) / 2
        plt.text(x_medio, y_medio, str(peso_arista), color='green')
    
    plt.show()

    return ruta, distancia
