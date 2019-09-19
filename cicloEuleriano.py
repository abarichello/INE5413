import grafos as Graph
import sys


def Hierholzer(graph):

    arestas = []

    for vertice in graph.getCon_Vertices():
        for adj in graph.vizinhos(vertice):
            if not (vertice[0], adj[0]) or not (adj[0], vertice[0]) in arestas:
                arestas.append((vertice[0], adj[0]))
    ord = set(map(tuple, map(sorted, arestas)))
    visitado = {aresta: False for aresta in ord}

    (r, ciclo) = buscarSubcicloEuleriano(graph, graph.getCon_Vertices()[0], visitado)

    if not r:
        return (False, None)
    else:
        if all(visitado):
            return (True, ciclo)
        else:
            return (False, None)


def buscarSubcicloEuleriano(graph, vertice, visitado):

    ciclo = [vertice[0]]
    t = vertice[0]

    while True:
        emb = True
        vu = None
        u = None

        for vizinho in graph.vizinhos(vertice):

            u = vizinho[0]
            vu = tuple(sorted((vertice[0], u)))
            if not visitado[vu]:
                emb = False
                break

        if emb:
            return False, None
        else:
            visitado[vu] = True
            vertice = u
            ciclo.append(vertice)
            break
        if vertice == t:
            break

    vp = set(ciclo)

    for elemento in vp:
        nao_visitado = False
        for vizinho2 in graph.vizinhos(elemento):
            vu = tuple(sorted((elemento[0], vizinho2[0])))
            if not visitado[vu]:
                nao_visitado = True
                break
        if not nao_visitado:
            continue
        (r, ciclo_l) = buscarSubcicloEuleriano(graph, elemento, visitado)
        if not r:
            return False, None
        ciclo_aux = ciclo
        ciclo = []
        inserido = False
        for i in ciclo_aux:
            if i == elemento and not inserido:
                inserido = True
                ciclo.extend(ciclo_l)
            else:
                ciclo.append(i)
    return True, ciclo

def main():
    file_name = sys.argv[1]
    Graph.ler(file_name)

    found, cicle = Hierholzer(Graph)
    if found:
        print(1)
        print(", ".join(map(str, cicle)))
    else:
        print(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
