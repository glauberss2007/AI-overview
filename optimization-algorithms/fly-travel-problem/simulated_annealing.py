import problem_representation
import fitness_function
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

melhor_solucao, melhor_custo = mlrose.simulated_annealing(fitness_function.problema,
                                                          schedule=mlrose.decay.GeomDecay(init_temp=10000),
                                                          random_state=1)
melhor_solucao, melhor_custo

problem_representation.imprimir_voos(melhor_solucao)