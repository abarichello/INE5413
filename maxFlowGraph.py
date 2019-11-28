import shlex
import sys
import os


class MaxFlowVertex:
    def __init__(self, id_):
        self.id = int(id_)
        self.adjacent = {}

    def neighbour(self):
        return self.adjacent.keys()

    def weigth(self, neighbour, flow = False):
        if neighbour in self.adjacent.keys():
            return self.adjacent[neighbour]
        elif flow:
            return 0
        else:
            return float("inf")

    def add_arc(self, neighbour, weigth):
        self.adjacent[int(neighbour)] = float(weigth)


class MaxFlowGraph:
    def __init__(self, path=None):
        self.s = 0
        self.t = 0
        self.vertices = {}
        self.arcs = 0

        self.read_file(path)

    def read_file(self, path):
        file = open(path, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            if line[0] == "c" or line[0] == "p":
                continue
            elif line[0] == "n":
                i = line.split()
                if i[2] == "s":
                    self.s = i[1]
                else:
                    self.t = i[1]
            elif line[0] == "a":
                a, v1, v2, weigth = line.split()
                self.add_vertex(int(v1))
                self.add_vertex(int(v2))
                self.get_vertex(v1).add_arc(int(v2), weigth)

    def add_vertex(self, id_):
        if id_ in self.vertices:
            return
        vertex = MaxFlowVertex(id_)
        self.vertices[id_] = vertex

    def add_arcs(self, v1, v2, weigth):
        self.vertices[int(v1)].add_arc(v2, weigth)
        self.vertices[int(v2)].add_arc(v1, weigth)
        self.arcs += 1

    def get_vertex(self, id_):
        return self.vertices[int(id_)]

    def qty_vertices(self):
        return len(self.vertices)

    def qty_arcs(self):
        return self.arcs

