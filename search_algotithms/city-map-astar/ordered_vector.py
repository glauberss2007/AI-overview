import numpy as np
import city_map_graph

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
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

city_map_graph.grafo.arad.adjacentes

city_map_graph.grafo.arad.adjacentes[0].vertice.rotulo, city_map_graph.grafo.arad.adjacentes[0].vertice.distancia_objetivo

city_map_graph.grafo.arad.adjacentes[0].distancia_aestrela, city_map_graph.grafo.arad.adjacentes[0].custo

vetor = VetorOrdenado(20)
vetor.insere(city_map_graph.grafo.arad.adjacentes[0])
vetor.insere(city_map_graph.grafo.arad.adjacentes[1])
vetor.insere(city_map_graph.grafo.arad.adjacentes[2])

vetor.imprime()