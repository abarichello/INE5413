import sys
import os

from itertools import groupby
from operator import itemgetter
from grafos import Graph, ler, vizinhos
from pprint import pprint


def graph_coloring(graph):
    # Reversed sort by number of neighbours
    vertices = sorted(graph.conj_vertices, key=lambda x: len(vizinhos(x)), reverse=True)

    colors = []
    color_map = {}

    for v in vertices:
        color_tmp = [True for i in vertices]
        for n in vizinhos(v):
            if n in color_map:
                color = color_map[n]
                color_tmp[color] = False

        for color, available in enumerate(color_tmp):
            if available:
                color_map[v] = color
                if color not in color_map:
                    colors.append(color)
                break
    return color_map


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./{sys.argv[0]} <filename>")
        os._exit(-1)

    ler(sys.argv[1])
    print("Graph:")
    print("Number of vertices")
    pprint(Graph.num_vertices)
    print("Vertices:")
    pprint(Graph.conj_vertices)
    print("Arcs:")
    pprint(Graph.conj_arestas)

    color_map = graph_coloring(Graph)
    print("Result:")

    seq = list(color_map.items())
    seq.sort(key = itemgetter(1))
    groups = groupby(seq, itemgetter(1))

    print("Nº of colors:\n", len(list(groups)))
    print("Color mapping:")
    pprint(color_map)
