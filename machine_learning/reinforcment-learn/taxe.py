import gym
import random
import numpy as np

# Overview
env = gym.make('Taxi-v3').env
env.render()
env.reset()
env.render()
env.reset()

print(env.action_space)
print(env.observation_space)

len(env.P)

env.P[484]

# Training
random.uniform(0, 1)
env.action_space

q_table = np.zeros([env.observation_space.n, env.action_space.n])
q_table.shape

q_table

np.argmax(np.array([3, 5]))

# 1-10% 3-90%
# exploration / exploitation
# 0 = south 1 = north 2 = east 3 = west 4 = pickup 5 = dropoff
#%%time
from IPython.display import clear_output

alpha = 0.1
gamma = 0.6
epsilon = 0.1

for i in range(100000):
  estado = env.reset()

  penalidades, recompensa = 0, 0
  done = False
  while not done:
    # Exploração
    if random.uniform(0, 1) < epsilon:
      acao = env.action_space.sample()
    # Exploitation
    else:
      acao = np.argmax(q_table[estado])

    proximo_estado, recompensa, done, info = env.step(acao)

    q_antigo = q_table[estado, acao]
    proximo_maximo = np.max(q_table[proximo_estado])

    q_novo = (1 - alpha) * q_antigo + alpha * (recompensa + gamma * proximo_maximo)
    q_table[estado, acao] = q_novo

    if recompensa == -10:
      penalidades += 1

    estado = proximo_estado

  if i % 100 == 0:
    clear_output(wait=True)
    print('Episódio: ', i)

print('Treinamento concluído')

# 0 = south 1 = north 2 = east 3 = west 4 = pickup 5 = dropoff
q_table[346]

env.reset()
env.render()

env.step(1)
env.render()

env.step(1)
env.render()

env.encode(3, 2, 1, 2)

# Avaliation
total_penalidades = 0
episodios = 50
frames = []

for _ in range(episodios):
    estado = env.reset()
    penalidades, recompensa = 0, 0
    done = False
    while not done:
        acao = np.argmax(q_table[estado])
        estado, recompensa, done, info = env.step(acao)

        if recompensa == -10:
            penalidades += 1

        frames.append({
            'frame': env.render(mode='ansi'),
            'state': estado,
            'action': acao,
            'reward': recompensa
        })

    total_penalidades += penalidades

print('Episódios', episodios)
print('Penalidades', total_penalidades)

frames[0]

from time import sleep
for frame in frames:
  clear_output(wait=True)
  print(frame['frame'])
  print('Estado', frame['state'])
  print('Ação', frame['action'])
  print('Recompensa', frame['reward'])
  sleep(.5)