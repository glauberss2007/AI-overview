import numpy as np
import brazil_map_graph

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância A*
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)


brazil_map_graph.grafo.portoUniao.adjacentes

brazil_map_graph.grafo.portoUniao.adjacentes[0].vertice.rotulo, brazil_map_graph.grafo.portoUniao.adjacentes[0].vertice.distancia_objetivo

brazil_map_graph.grafo.portoUniao.adjacentes[0].distancia_aestrela, brazil_map_graph.grafo.portoUniao.adjacentes[0].custo

vetor = VetorOrdenado(3)
vetor.insere(brazil_map_graph.grafo.portoUniao.adjacentes[0])
vetor.insere(brazil_map_graph.grafo.portoUniao.adjacentes[1])
vetor.insere(brazil_map_graph.grafo.portoUniao.adjacentes[2])

vetor.imprime()