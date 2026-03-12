# =============================================
# DFS - Busca em Profundidade (Recursiva)
# Exemplo: Mapa da Romênia
# =============================================

def dfs(grafo, atual, destino, caminho=None, visitados=None):

    # Inicializa estruturas na primeira chamada
    if caminho is None:
        caminho = []
    if visitados is None:
        visitados = set()

    # Marca a cidade atual
    caminho.append(atual)
    visitados.add(atual)

    # Verifica se chegou ao destino
    if atual == destino:
        return caminho

    # Explora cada vizinho da cidade atual
    for vizinho in grafo.get(atual, []):

        # Evita visitar cidades já exploradas
        if vizinho not in visitados:

            resultado = dfs(grafo, vizinho, destino, caminho, visitados)

            # Se encontrou o destino, retorna o caminho
            if resultado:
                return resultado

    # Backtracking → volta para a cidade anterior
    caminho.pop()
    return None


# ====================== GRAFO ======================

grafo_romenia = {
    "Oradea": ["Zerind", "Sibiu"],
    "Zerind": ["Arad", "Oradea"],
    "Arad": ["Sibiu", "Timisoara"],
    "Sibiu": ["Fagaras", "Rimnicu Vilcea"],
    "Timisoara": ["Lugoj"],
    "Lugoj": ["Mehadia"],
    "Mehadia": ["Drobeta"],
    "Drobeta": ["Craiova"],
    "Craiova": ["Pitesti"],
    "Pitesti": ["Bucharest"],
    "Fagaras": ["Bucharest"],
    "Rimnicu Vilcea": ["Pitesti"],
    "Bucharest": []
}

# ====================== EXECUÇÃO ======================

caminho = dfs(grafo_romenia, "Oradea", "Bucharest")

print("\nDFS - Mapa da Romênia")
print("Caminho:", " → ".join(caminho))