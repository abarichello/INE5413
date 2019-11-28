from maxFlowGraph import *
from pprint import pprint


def edmondsKarp(C):
    graph = MaxFlowGraph(sys.argv[1])
    initial = int(graph.s) - 1
    final = int(graph.t) - 1

    n = len(C)
    F = [[0] * n for _ in range(n)]

    while True:
        path = bfs(C, F, initial, final)

        if not path:
            break

        u,v = path[0], path[1]
        flow = C[u][v] - F[u][v]

        for i in range(len(path) - 2):
            u,v = path[i + 1], path[i + 2]
            flow = min(flow, C[u][v] - F[u][v])

        for i in range(len(path) - 1):
            u,v = path[i], path[i + 1]
            F[u][v] += flow
            F[v][u] -= flow

    return sum([F[initial][i] for i in range(n)])

def bfs(C, F, initial, final):
    P = [-1] * len(C)
    P[initial] = initial
    queue = [initial]

    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                queue.append(v)
                if v == final:
                    path = []
                    while True:
                        path.insert(0, v)
                        if v == initial:
                            break
                        v = P[v]
                    return path
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./dijkstra.py <filename>")
        os._exit(-1)

    graph = MaxFlowGraph(sys.argv[1])

    C = []
    for u in graph.vertices.keys():
    	l = []
    	for v in graph.vertices.keys():
    		l.append(graph.get_vertex(u).weigth(v, True))
    	C.append(l)
    print("Fluxo máximo:", edmondsKarp(C))

