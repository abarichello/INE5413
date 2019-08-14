from collections import namedtuple

#Cria o grafo propriamente dito
Graph = namedtuple("Graph", "num_vertices conj_vertices conj_arestas")

#Retorna o numero de vértices do grafo
def qtdVertices():
    return Graph.num_vertices

#Retorna a quantidade de arestas do grafo
def qtdArestas():

    qtd = 0

    for i in range(Graph.num_vertices):
        qtd = qtd + len(Graph.conj_arestas[i])

    return qtd

#Retorna o grau do vértice desejado
def grau(v):
    return len(Graph.conj_arestas[v[0]-1])

#Retorna o rótulo de um vértice
def rotulo(v):
    print(v[1])

#Retorna os vértices vizinhos de um vértice
def vizinhos(v):

    vizinhos_final = []
    vizinhos = Graph.conj_arestas[v[0]-1]

    for i in range(len(vizinhos)):
         vizinhos_final.append(vizinhos[i][0])

    return vizinhos_final

#Retorna se há uma aresta conectando dois vértices
def haAresta(u, v):

        x = u[0] if u[0] < v[0] else v[0]
        i = 0

        if x == u[0]:
            y = v
        else:
            y = u

        while (i < len(Graph.conj_arestas[x-1])):
            if Graph.conj_arestas[x-1][i][0] == y:
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

    while (tam_arr < len(Graph.conj_arestas[x-1])):
        if Graph.conj_arestas[x-1][i][0][0] == y:
            return Graph.conj_arestas[x-1][i][1]
        tam_arr = tam_arr+1
        i = i+1

    return result

#Lê o arquivo e define os atributos do grafo, funciona como um construtor
def ler(arquivo):

    file = open(arquivo, "r")
    texto = file.readlines()
    file.close()

    Graph.num_vertices = ler_num_vertices(texto[0])
    Graph.conj_vertices = cria_vertices(texto)
    Graph.conj_arestas = define_arestas(texto)
    print(Graph.conj_arestas)

#Função auxiliar que lê o número de vértices do arquivo
def ler_num_vertices(texto):

    resultado = []
    temp = []
    resultado_formatado = ''

    for i in texto:
        temp.append(i)

    i = 0

    while (temp[i] != '\n'):

        while (temp[i] != ' ' and len(resultado) == 0):
            i = i+1

        i = i+1
        resultado.append(temp[i])

    resultado.pop()

    for i in resultado:
        resultado_formatado = resultado_formatado + i

    return int(resultado_formatado)

#Função auxiliar que define o conjunto de vértices do Grafo
def cria_vertices(texto):

#Deixa na lista apenas o numero do vértice e seu respectivo rótulo
    texto.pop(0)
    index = texto.index("*edges\n")
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
        rotulo_vertice = rotulo_vertice[2:len(rotulo_vertice)-1]
        conj_vertices.append((num_vertices, rotulo_vertice))

    return conj_vertices

#Função auxiliar que define o conjunto de arestas lendo-as do arquivo
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

            if j == len(texto):
                break

    return conj_arestas

#Função auxiliar, que retorna o rótulo de um vértice dado seu número identificador
def getRotuloByNumber(n):

    for i in Graph.conj_vertices:
        if i[0] == n:
            return i[1]
