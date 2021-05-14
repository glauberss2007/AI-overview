import problem_representation
import six
import sys

sys.modules['sklearn.externals.six'] = six
import mlrose

melhor_solucao, melhor_custo = mlrose.hill_climb(problem_representation.problema)

problem_representation.imprimir_solucao(melhor_solucao)
