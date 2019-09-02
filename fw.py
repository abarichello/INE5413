# Floyd–Warshall Algorithm

import sys
import os
from math import inf
from pprint import pprint
from grafos import Graph, ler, peso
from typing import List


def floyd_warshall(graph: Graph) -> List[List[float]]:
    n_vertices = graph.num_vertices
    print(f"Total vertices: {str(n_vertices)}")
    dist: List[List[float]] = [
        [inf for i in range(n_vertices)] for j in range(n_vertices)
    ]

    pprint(graph.conj_arestas)
    for vertex in graph.conj_vertices:
        index = vertex[0] - 1
        dist[index][index] = 0

    for vertex0 in graph.conj_vertices:
        for vertex1 in graph.conj_vertices:
            if vertex0 == vertex1:
                continue
            else:
                ind_u = vertex0[0] - 1
                ind_v = vertex1[0] - 1
                weight = peso(vertex0, vertex1)
                dist[ind_u][ind_v] = weight if weight else inf

    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./{sys.argv[0]} <filename>")
        os._exit(-1)

    ler(sys.argv[1])
    dist = floyd_warshall(Graph)
    pprint(dist)
