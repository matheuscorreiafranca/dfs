# =============================================
# DFS - Busca em Profundidade (Recursiva)
# Exemplo: Mapa clássico da Romênia (AI Search)
# =============================================

def dfs(grafo, atual, destino, caminho=None, visitados=None):

    # Inicializa estruturas
    if caminho is None:
        caminho = []
    if visitados is None:
        visitados = set()

    # Marca cidade atual
    caminho.append(atual)
    visitados.add(atual)

    # Se chegou ao destino
    if atual == destino:
        return caminho

    # Explora vizinhos
    for vizinho in grafo.get(atual, []):
        if vizinho not in visitados:

            resultado = dfs(grafo, vizinho, destino, caminho, visitados)

            if resultado:
                return resultado

    # Backtracking
    caminho.pop()
    return None


# ====================== GRAFO COMPLETO ======================

grafo_romenia = {

    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],

    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],

    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],

    "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],

    "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],

    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],

    "Giurgiu": ["Bucharest"],

    "Urziceni": ["Bucharest", "Vaslui", "Hirsova"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],

    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"]
}

# ====================== EXECUÇÃO ======================

caminho = dfs(grafo_romenia, "Oradea", "Neamt")

print("\nDFS - Mapa da Romênia")
print("Caminho encontrado:", " → ".join(caminho))
print("Número de cidades visitadas:", len(caminho))
