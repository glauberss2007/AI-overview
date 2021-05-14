import problem_representation
import six
import sys

sys.modules['sklearn.externals.six'] = six
import mlrose

melhor_solucao, melhor_custo = mlrose.genetic_alg(problem_representation.problema, pop_size=500, mutation_prob=0.2)

problem_representation.imprimir_solucao(melhor_solucao)
