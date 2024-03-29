from collections import namedtuple
from typing import List, Tuple

#Cria o grafo propriamente dito
Graph = namedtuple("Graph", "num_vertices conj_vertices conj_arestas")

#Retorna o numero de vertices do grafo
def getNum_vertices():
    return Graph.num_vertices

#Retorna o conjunto de vertices do grafo
def getCon_Vertices():
    return Graph.conj_vertices

#Retorna o conjunto de arestas do grafo
def getConj_Arestas():
    return Graph.conj_arestas

#Retorna o numero de vertices do grafo
def qtdVertices():
    return Graph.num_vertices

#Retorna a quantidade de arestas do grafo
def qtdArestas():

    qtd = 0

    for i in range(Graph.num_vertices):
        qtd = qtd + len(Graph.conj_arestas[i])

    return qtd

#Retorna o grau do vertice desejado
def grau(v):
    return len(Graph.conj_arestas[v[0]-1])

#Retorna o rotulo de um vertice
def rotulo(v):
    return(v[1])

#Retorna os vertices vizinhos de um vertice
def vizinhos(v):

    vizinhos_final = []
    vizinhos = Graph.conj_arestas[v[0]-1]

    for i in range(len(vizinhos)):
         vizinhos_final.append(vizinhos[i][0])

    return vizinhos_final

#Retorna se ha uma aresta conectando dois vertices
def haAresta(u, v):

        x = u[0] if u[0] < v[0] else v[0]
        i = 0

        if x == u[0]:
            y = v
        else:
            y = u

        while (i < len(Graph.conj_arestas[x-1])):
            if Graph.conj_arestas[x-1][i][0][0] == y[0]:
                return True
            i = i+1

        return False

#Retorna o peso de uma aresta
def peso(u, v):

    x = u[0] if u[0] < v[0] else v[0]
    i = 0
    tam_arr = 0
    result = []

    if x == u[0]:
        y = v[0]
    else:
        y = u[0]

    while tam_arr < len(Graph.conj_arestas[x - 1]):
        if Graph.conj_arestas[x - 1][i][0][0] == y:
            return Graph.conj_arestas[x - 1][i][1]
        tam_arr = tam_arr + 1
        i = i + 1
    return result

#Le o arquivo e define os atributos do grafo, funciona como um construtor
def ler(arquivo):

    file = open(arquivo, "r")
    texto = file.readlines()
    file.close()

    Graph.num_vertices = read_total_vertices(texto[0])
    Graph.conj_vertices = cria_vertices(texto)
    Graph.conj_arestas = define_arestas(texto)

    return Graph

def read_directed(path: str):
    file = open(path, "r")
    contents = file.readlines()
    file.close()

    Graph.num_vertices = read_total_vertices(contents[0])
    Graph.conj_vertices = cria_vertices(contents, directed=True)
    Graph.conj_arestas = make_arcs_list(contents)
    return Graph

def read_total_vertices(text: str) -> int:
    return int(text.replace("*vertices ", ""))

#Funcao auxiliar que define o conjunto de vertices do Grafo
def cria_vertices(texto, directed=False):

#Deixa na lista apenas o numero do vertice e seu respectivo rotulo
    texto.pop(0)

    header_text = "*edges\n"
    if directed:
        header_text = "*arcs\n"
    index = texto.index(header_text)
    texto = texto[0:index]

    conj_vertices = []

    for elemento in texto:

        contador = 0
        num_vertices = ''
        rotulo_vertice = ''
        aux = False
        contador_interno = 0

        while (elemento[contador] != '\n'):

            if aux == False:
                num_vertices = num_vertices + elemento[contador]

            if elemento[contador] == " ":
                aux = True
                rotulo_vertice = rotulo_vertice + elemento[contador]
                contador_interno = contador + 1

                while (elemento[contador_interno] != '\n'):
                    rotulo_vertice = rotulo_vertice + elemento[contador_interno]
                    contador_interno = contador_interno + 1
                    contador = contador_interno - 1

            contador = contador+1

        num_vertices = num_vertices[0:len(num_vertices)-1]
        num_vertices = int(num_vertices)
        rotulo_vertice = rotulo_vertice[1:len(rotulo_vertice)]
        if rotulo_vertice[0] == '"' and rotulo_vertice[-1] == '"':
            rotulo_vertice = rotulo_vertice[1:-1]
        conj_vertices.append((num_vertices, rotulo_vertice))

    return conj_vertices

def make_arcs_list(texto: List[str]):
    contador = 0
    conj_arestas = []
    j = 0

    for i in range(Graph.num_vertices):
        conj_arestas.append([])

    while (texto[contador] != '*arcs\n'):
        contador = contador+1

    texto = texto[contador+1:]

    for i in range(Graph.num_vertices):
        aux = len(str(i+1))

        while (j < len(texto) and int(texto[j][0:aux]) == i+1):

            espacos = []

            for k in range(len(texto[j])):
                if texto[j][k] == ' ':
                    espacos.append(k)

            vertice_adj = int(texto[j][espacos[0]+1:espacos[1]])
            peso = float(texto[j][espacos[1]+1:])
            rotulo = getRotuloByNumber(vertice_adj)
            conj_arestas[i].append(((vertice_adj, rotulo), peso))
            j = j+1
       
    return conj_arestas

#Funcao auxiliar que define o conjunto de arestas lendo-as do arquivo
def define_arestas(texto):

    contador = 0
    conj_arestas = []
    j = 0

    for i in range(Graph.num_vertices):
        conj_arestas.append([])

    while (texto[contador] != '*edges\n'):
        contador = contador+1

    texto = texto[contador+1:]

    for i in range(Graph.num_vertices):
        aux = len(str(i+1))

        while (j < len(texto) and int(texto[j][0:aux]) == i+1):

            espacos = []

            for k in range(len(texto[j])):
                if texto[j][k] == ' ':
                    espacos.append(k)

            vertice_adj = int(texto[j][espacos[0]+1:espacos[1]])
            peso = float(texto[j][espacos[1]+1:])
            rotulo = getRotuloByNumber(vertice_adj)
            conj_arestas[i].append(((vertice_adj, rotulo), peso))
            j = j+1

        if i > 0:
            for n in range(i):
                for m in range(len(conj_arestas[n])):
                    if conj_arestas[n][m][0][0] == i+1:
                        conj_arestas[i].append(((n+1, getRotuloByNumber(n+1)), conj_arestas[n][m][1]))
                        if j == len(texto):
                            break

    return conj_arestas

# Retorna um vértice dado seu número
def getVertexByNumber(n):
    for i in Graph.conj_vertices:
        if i[0] == n:
            return i

# Função auxiliar, que retorna o rótulo de um vértice dado seu número identificador
def getRotuloByNumber(n):
    return getVertexByNumber(n)[1]
