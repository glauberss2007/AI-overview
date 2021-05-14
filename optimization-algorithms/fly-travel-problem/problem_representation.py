pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'
voos = {('BRU', 'FCO'): ['15:44', '18:55', 382]}

voos = {}
for linha in open('./content/flights.txt'):
    # print(linha)
    # print(linha.split(','))
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

agenda = [1, 2, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]


def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0

    for i in range(len(agenda) // 2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2], volta[0],
                                                    volta[1], volta[2]))

    print('Preço total: ', total_preco)


agenda = [1, 0, 3, 2, 7, 1, 6, 3, 2, 4, 5, 3]
imprimir_voos(agenda)