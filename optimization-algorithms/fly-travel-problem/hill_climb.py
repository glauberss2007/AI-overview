import problem_representation
import fitness_function
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

melhor_solucao, melhor_custo = mlrose.hill_climb(fitness_function.problema, 1)

melhor_solucao, melhor_custo

problem_representation.imprimir_voos(melhor_solucao)

problem_representation.voos[('BRU', 'FCO')]