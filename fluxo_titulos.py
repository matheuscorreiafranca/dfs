# =============================================
# DFS - Busca em Profundidade
# Exemplo: Fluxo Financeiro
# =============================================

def dfs(grafo, atual, destino, caminho=None, visitados=None):

    # Inicializa estruturas
    if caminho is None:
        caminho = []
    if visitados is None:
        visitados = set()

    # Marca o nó atual
    caminho.append(atual)
    visitados.add(atual)

    # Verifica se chegou ao objetivo
    if atual == destino:
        return caminho

    # Explora os próximos nós
    for vizinho in grafo.get(atual, []):

        if vizinho not in visitados:

            resultado = dfs(grafo, vizinho, destino, caminho, visitados)

            if resultado:
                return resultado

    # Backtracking
    caminho.pop()
    return None


# ====================== GRAFO FINANCEIRO ======================

grafo_financeiro = {
    "Inicio": ["TituloA", "TituloB", "TituloC"],
    "TituloA": ["PagamentoA"],
    "TituloB": ["PagamentoB"],
    "TituloC": ["PagamentoC"],
    "PagamentoA": ["Caixa"],
    "PagamentoB": ["Caixa"],
    "PagamentoC": ["Caixa"],
    "Caixa": []
}

# ====================== EXECUÇÃO ======================

caminho = dfs(grafo_financeiro, "Inicio", "Caixa")

print("\nDFS - Fluxo Financeiro")
print("Caminho:", " → ".join(caminho))