# Reference: https://www.youtube.com/watch?v=5wFyZJ8yH9Q

import os
import sys

from grafos import Graph, read_directed, vizinhos, rotulo
from pprint import pprint
from collections import namedtuple


def dfs(graph, f=None):
    visited= {}
    t_found = {}
    forest = []
    time = [0]
    vertices = []

    for v in graph.conj_vertices:
        label = rotulo(v)
        visited[label] = False
        t_found[label] = float("inf")

    if f is not None:
        for idVertice, tempoVertice in f.items():
            vertices.append((idVertice, tempoVertice))
        vertices.sort(key=lambda x: x[1], reverse=True)
        vertices = list(map(lambda x: x[0], vertices))
    else:
        vertices = graph.conj_vertices


    for u in vertices:
        if not visited[rotulo(u)]:
            found = []
            dfs_visit(graph, u, visited, t_found, found, time)
            if len(found) > 0:
                forest.append(found)

    return forest, t_found


def dfs_visit(graph, v, visited, t_found, found, time):
    visited[v] = True
    found.append(v)
    time[0] += 1

    for u in vizinhos(v):
        if not visited[rotulo(u)]:
            dfs_visit(graph, u, visited, t_found, found, time)
    time[0] += 1
    t_found[v] = time[0]


# kosaraju algorithm
def strongly_connected_components(graph):
    (_, t_found) = dfs(graph)

    # TODO: Transpose the graph

    forest_2 = dfs(graph, t_found)
    return forest_2


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./{sys.argv[0]} <filename>")
        os._exit(-1)

    read_directed(sys.argv[1])
    print("Graph:", "\n")
    print("Number of vertices")
    pprint(Graph.num_vertices)
    print("Vertices:")
    pprint(Graph.conj_vertices)
    print("Arcs:")
    pprint(Graph.conj_arestas)

    l = strongly_connected_components(Graph)
    pprint(l)
