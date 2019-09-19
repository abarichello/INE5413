import sys
import os
from typing import Tuple
from grafos import Graph, ler, vizinhos, peso, getVertexByNumber


inf = float('inf')


def dijkstra(initial: int):
    vertices = set(Graph.conj_vertices)

    # initiate distance, path -> inf, none for all vertices
    distances: dict = {vertex: inf for vertex in vertices}
    paths: dict = {vertice: [] for vertice in vertices}

    # prepare initial vertice attributes
    initial_vertex = getVertexByNumber(initial)
    distances[initial_vertex] = 0
    paths[initial_vertex] = [initial]

    # while all vertices aren't visited
    while vertices:
        # find minor distance
        current = min(vertices, key=lambda vertice: distances[vertice])

        # current is "marked as visited"
        vertices.remove(current)

        if distances[current] == inf:
            break

        for neighbour in vizinhos(current):
            weigth = peso(current, neighbour)
            route = distances[current] + weigth

            if route < distances[neighbour]:
                distances[neighbour] = route
                paths[neighbour].append(current[0])

    return paths, distances


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./dijkstra.py <filename>")
        os._exit(-1)

    ler(sys.argv[1])

    vertice_inicial = Graph.num_vertices
    print(f"Vértice inicial: {str(vertice_inicial)}")

    caminhos, distancias = dijkstra(vertice_inicial)

    for v in Graph.conj_vertices:
        caminho = caminhos[v]
        distancia = distancias[v]

        print(v[0],": ",caminho,"; d=",distancia)

