import sys
import os
from typing import Tuple
from grafos import Graph, ler, vizinhos


def bfs(n_vertices: int) -> Tuple[dict, dict]:
    visited: dict = {}
    distance: dict = {}
    predecessor: dict = {}
    for v in Graph.conj_vertices:
        i = v[0]
        visited[i] = False
        distance[i] = float("inf")
        predecessor[i] = None

    start = Graph.conj_vertices[0]
    visited[start[0]] = True
    distance[start[0]] = 0

    queue: list = [start]
    while queue:
        u = queue.pop()
        for neighbour in vizinhos(u):
            key = neighbour[0]
            if not visited[key]:
                visited[key] = True
                distance[key] = distance[u[0]] + 1
                predecessor[key] = u[0]
                queue.append(neighbour)
    return distance, predecessor


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./bfs.py <filename>")
        os._exit(-1)

    ler(sys.argv[1])
    n_vertices = Graph.num_vertices
    print(f"Total vertices: {str(n_vertices)}")
    dist, pred = bfs(n_vertices)
    print(f"Distance: {dist}, Predecessor: {pred}")
    print("Printing levels:")

    levels = {}
    for v in Graph.conj_vertices:
        key = v[0]
        if not dist[key] in levels:
            levels[dist[key]] = []
        levels[dist[key]].append(key)

    for k in levels.keys():
        print(str(k) + ": " + ", ".join(map(str, levels[k])))
