import numpy as np
import graph

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
vetor.insere(graph.grafo.palmeira)
vetor.insere(graph.grafo.lapa)
vetor.insere(graph.grafo.campoLargo)
vetor.insere(graph.grafo.curitiba)

vetor.imprime()

vetor.insere(graph.grafo.contenda)
vetor.imprime()

vetor.valores[0], vetor.valores[0].rotulo