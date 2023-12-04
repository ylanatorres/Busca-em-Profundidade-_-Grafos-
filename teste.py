def DFS(graph):
    global cor, d, f, tipo_aresta, vm
    vertices = list(graph.keys())
    vertices.sort(key=lambda v: len(graph[v]), reverse=True)

    for u in vertices:
        cor[u] = 'branco'

    for u in vertices:
        if cor[u] == 'branco':
            DFS_VISIT(graph, u)

def DFS_VISIT(graph, u):
    global cor, d, f, tipo_aresta, vm
    cor[u] = 'cinza'
    vm = vm + 1
    d[u] = vm

    for v in graph[u]:
        if cor[v] == 'branco':
            tipo_aresta.append(f"Aresta ({u+1}, {v+1}): Árvore")
            DFS_VISIT(graph, v)

        elif d[u] < d[v]:
            tipo_aresta.append(f"Aresta ({u+1}, {v+1}): Avanço")

        elif cor[v] == 'cinza':
            tipo_aresta.append(f"Aresta ({u+1}, {v+1}): Retorno")

        else:
            tipo_aresta.append(f"Aresta ({u+1}, {v+1}): Cruzamento")

    cor[u] = 'preto'
    vm = vm + 1
    f[u] = vm

# Exemplo de uso
graph = {0: [1, 2], 1: [3], 2: [4], 3: [], 4: [3]}
cor = {}
d = {}
f = {}
tipo_aresta = []
vm = 0

DFS(graph)

print("Valores do vetor d:", d)
print("Valores do vetor f:", f)
print("Nomenclatura das arestas:")
for aresta in tipo_aresta:
    print(aresta)
