#!/usr/bin/python

# Importar librerías necesarias
import time  # Para medir el tiempo de ejecución del algoritmo
import sys
import codecs  # Para manejar la codificación de archivos
from operator import itemgetter  # Utilidad para ordenar elementos

# Clase Edge representa una arista en el grafo
class Edge:
    def __init__(self, origin=None, weight=0):
        self.origin = origin  # Origen de la arista
        self.weight = weight  # Peso de la arista

    # Representación en cadena de la arista
    def __repr__(self):
        return f"edge: {self.origin} {self.weight}"

# Clase Airport representa un aeropuerto en el grafo
class Airport:
    def __init__(self, iden=None, name=None, index=None):
        self.code = iden  # Código del aeropuerto
        self.name = name  # Nombre del aeropuerto
        self.index = index  # Índice del aeropuerto en la lista
        self.routes = []  # Lista de rutas salientes del aeropuerto
        self.routeHash = dict()  # Diccionario para mapear destino a índice de ruta
        self.outweight = 0  # Peso total de las rutas salientes

    # Método para añadir una ruta a este aeropuerto
    def add_route(self, destination, weight):
        # Si la ruta ya existe, incrementar su peso
        if destination in self.routeHash:
            self.routes[self.routeHash[destination]].weight += weight
        else:
            # Si la ruta es nueva, añadirla a la lista y al diccionario
            self.routeHash[destination] = len(self.routes)
            self.routes.append(Edge(destination, weight))
        self.outweight += weight  # Incrementar el peso total de salida

    # Representación en cadena del aeropuerto
    def __repr__(self):
        return f"{self.code}\t{self.name}"

# Listas globales para almacenar aeropuertos y un hash para búsqueda rápida
airportList = []
airportHash = dict()

# Función para leer información de aeropuertos desde un archivo
def readAirports(fd):
    print(f"Reading Airport file from {fd}")
    with codecs.open(fd, "r") as airportsTxt:
        cont = 0  # Contador para el número de aeropuertos con código IATA
        for line in airportsTxt:
            a = Airport()
            try:
                # Dividir línea por comas y procesar campos
                temp = line.split(',')
                if len(temp[4]) != 5:
                    raise Exception('not an IATA code')
                # Establecer nombre y código del aeropuerto
                a.name = temp[1][1:-1] + ", " + temp[3][1:-1]
                a.code = temp[4][1:-1]
                a.index = cont  # Asignar índice al aeropuerto
            except Exception as inst:
                pass  # Ignorar aeropuertos sin código IATA
            else:
                # Agregar aeropuerto a la lista y al hash
                cont += 1
                airportList.append(a)
                airportHash[a.code] = a
    print(f'There are {cont} airports with IATA code.')

# Función para leer información de rutas desde un archivo
def readRoutes(fd):
    print(f"Reading Routes file from {fd}")
    total_routes = 0  # Contador para el número total de rutas válidas
    with codecs.open(fd, "r") as routesTxt:
        for line in routesTxt:
            # Dividir línea por comas y procesar campos
            temp = line.split(',')
            origin, destination = temp[2], temp[4]
            # Verificar si tanto el origen como el destino están en el hash
            if origin in airportHash and destination in airportHash:
                # Añadir ruta al aeropuerto de origen
                destination_index = airportHash[destination].index
                airportHash[origin].add_route(destination_index, 1)
                total_routes += 1  # Incrementar contador de rutas
    print(f'There are {total_routes} routes connecting 2 airports with IATA code.')

# Función para calcular PageRank de los aeropuertos
def computePageRanks(damping=0.85, max_iterations=250, convergence_threshold=1e-12):
    num_airports = len(airportList)  # Número total de aeropuertos
    P = [1 / num_airports] * num_airports  # Inicializar vector P con 1/n para cada aeropuerto
    L = damping  # Factor de amortiguamiento

    for iteration in range(max_iterations):
        Q = [0] * num_airports  # Inicializar vector Q con 0 para cada aeropuerto
        for i in range(num_airports):
            # Calcular la suma ponderada de PageRanks de las aristas entrantes
            for edge in airportList[i].routes:
                j = edge.origin
                # Verificar si el aeropuerto de origen tiene rutas de salida
                if airportList[j].outweight > 0:
                    Q[i] += (P[j] * edge.weight) / airportList[j].outweight
            # Aplicar factor de amortiguamiento y teleportación
            Q[i] = L * Q[i] + (1 - L) / num_airports
        
        # Normalizar los valores de PageRank para que su suma sea 1
        norm = sum(Q)
        if norm == 0:
            raise ValueError("Sum of PageRanks is zero. Check for disconnected graph components.")
        Q = [x / norm for x in Q]

        # Verificar si los valores de PageRank han convergido
        change = sum(abs(Q[i] - P[i]) for i in range(num_airports))
        if change < convergence_threshold:
            break

        P = Q  # Actualizar P con los nuevos valores de Q

    return P, iteration + 1, sum(Q)  # Devolver el vector final de PageRank y el número de iteraciones

# Función para imprimir los PageRanks de los aeropuertos

def outputPageRanks(pageRanks):
    # Ordenar aeropuertos por PageRank y mostrar los primeros 25
    sorted_airports = sorted([(pr, airport.name) for pr, airport in zip(pageRanks, airportList)], reverse=True)
    for pr, name in sorted_airports[:25]:
        print(f"{pr:.16f} {name}")

# Función principal del script
def main():
    # Leer archivos de aeropuertos y rutas
    readAirports("airports.txt")
    readRoutes("routes.txt")
    
    # Contar número de nodos sumideros (aeropuertos sin rutas de salida)
    num_sink_nodes = sum(1 for airport in airportList if airport.outweight == 0)
    print("Number of sink nodes:", num_sink_nodes)

    # Calcular PageRank, medir tiempo de ejecución y mostrar resultados
    time1 = time.time()
    pageRanks, iterations, sum_of_PageRank = computePageRanks()
    time2 = time.time()

    outputPageRanks(pageRanks)

    print("\nSum of PageRank:", sum_of_PageRank)
    print("Number of iterations: ", iterations)
    print("Time of computePageRanks(): ", time2 - time1)

if __name__ == "__main__":
    main()
