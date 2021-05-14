import numpy as np
import city_map_graph

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, vertice):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = vertice
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)


vetor = VetorOrdenado(5)
vetor.insere(city_map_graph.grafo.arad)
vetor.insere(city_map_graph.grafo.craiova)
vetor.insere(city_map_graph.grafo.bucharest)
vetor.insere(city_map_graph.grafo.dobreta)

vetor.imprime()

vetor.insere(city_map_graph.grafo.lugoj)
vetor.imprime()

vetor.valores[0], vetor.valores[0].rotulo