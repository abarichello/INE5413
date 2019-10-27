import sys
import os
from typing import Tuple
from grafos import Graph, read_directed, vizinhos, rotulo


inf = float('inf')


def visit_ot(current: int, visited: dict, sorted_vertices):
    visited[current] = True

    for neighbour in vizinhos(current):
        if visited[neighbour] == False:
            visit_ot(neighbour, visited, sorted_vertices)

    # add vertice to the top of the list
    sorted_vertices.insert(0, current)

def topological_sort():
    vertices = Graph.conj_vertices

    # configuring all vertices
    visited: dict = {vertex: False for vertex in vertices}

    # creating list of topolotical sorted vertices
    sorted_vertices = []

    for current in vertices:
        if (visited[current] == False):
            # DFS-Visit-OT
            visit_ot(current, visited, sorted_vertices)

    return sorted_vertices


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./ordenacaoTopologica.py <filename>")
        os._exit(-1)

    read_directed(sys.argv[1])

    sorted_vertices = topological_sort()

    for index, v in enumerate(sorted_vertices):
            print(rotulo(v), end='')
            if index < len(sorted_vertices) - 1:
                print(' -> ', end='')
    print()
