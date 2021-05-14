import problem_representation
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def fitness_function(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = problem_representation.pessoas[i][1]
        id_voo += 1
        ida = problem_representation.voos[(origem, problem_representation.destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = problem_representation.voos[(problem_representation.destino, origem)][agenda[id_voo]]
        total_preco += volta[2]

    return total_preco


agenda = [1,7, 3,1, 1,1, 6,3, 2,4, 5,3]
fitness_function(agenda)

fitness = mlrose.CustomFitness(fitness_function)
problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness,
                              maximize = False, max_val = 10)