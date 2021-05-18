import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Background (entries)
Service: How would you rate the service, on a scale of 0 to 10?
    bad, acceptable, great

Food quality: how good was the food, on a scale of 0 to 10?
    bad, good, tasty

Consequential (occur)
Tip: How much tip would you give, between 0% and 20%?
    low, medium, high

Rules
    If the quality of the food is poor or the service is poor then tipping will be low
    If service to medium then tip will be average
    If the service is good and the food quality is good then the tip will be high
'''

# Background and consequent
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

# Membership functions
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 8])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [2, 10, 18])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 20, 20])
gorjeta.view()

regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitável'], gorjeta['media'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['saborosa'], gorjeta['alta'])

# Control System
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])

sistema = ctrl.ControlSystemSimulation(sistema_controle)

sistema.input['qualidade'] = 10
sistema.input['servico'] = 10
sistema.compute()

print(sistema.output['gorjeta'])
gorjeta.view(sim=sistema)
