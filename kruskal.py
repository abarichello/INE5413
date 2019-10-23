from grafos import Graph, ler
import sys

def Kruskal(Graph):

    A = []
    S = []
    E = []
    crescente = []
    menor = 0
    vertices_conj = []
    somatorio = 0

    for vertice in Graph.conj_vertices:
        vertices_conj.append({vertice[0]})

 # Coloca em S todos os vertices do grafo
    for vertice in Graph.conj_vertices:
        S.append(vertice[0])

 # Ordena as arestas por peso crescente
    for i in range(len(Graph.conj_arestas)):
        for aresta in Graph.conj_arestas[i]:
            aux = [i, aresta[0][0], aresta[1]]
            E.append((aux))
    for i in range(len(E)):
        menor = [0, E[0][2]]
        for j in range(len(E)):
            if E[j][2] < menor[1]:
                menor = [j, E[j][2]]
        E[menor[0]][0] = E[menor[0]][0]+1
        crescente.append(E[menor[0]])
        E.remove(E[menor[0]])

 # Elimina arestas duplicadas
    novo = []
    for i in range(len(crescente)):
        if i % 2 == 0:
            novo.append(crescente[i])

 # Produz arvore geradora minima
    tam = len(novo)
    for i in range(tam):
            u = novo[i][0]
            v = novo[i][1]

            controle = False

            for k in range(len(vertices_conj)):
                if u in vertices_conj[k] and v in vertices_conj[k]:
                    controle = True
                    break
            if controle == False:
                for j in range(len(vertices_conj)):
                    if u in vertices_conj[j]:
                        x = vertices_conj[j]
                        vertices_conj[j] = {-1}
                    if v in vertices_conj[j]:
                        y = vertices_conj[j]
                        vertices_conj[j] = {-1}
                z = x.union(y)
                vertices_conj.append(z)
                A.append(novo[i])

 # Saida do programa
    for arestas_finais in A:
        somatorio = somatorio + arestas_finais[2]
    print(somatorio)

    string = ''
    for arestas_finais in A:
        string = string + str(arestas_finais[0]) + "-" + str(arestas_finais[1]) + ", "
    print(string[0:-2])

def main():
    file_name = sys.argv[1]
    ler(file_name)
    Kruskal(Graph)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
