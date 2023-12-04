def grafo(arquivo):
    grafo = {}

    with open(arquivo, 'r') as file:
        for linha in file:
            origem, destino = linha.strip().split(',')