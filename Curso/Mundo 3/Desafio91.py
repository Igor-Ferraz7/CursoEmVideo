import random
from operator import itemgetter
sorteio = dict()
n = n1 = 1
for c in range(0, 4):
    sorteio[f'Jogador{n}'] = random.randint(0, 6)
    n += 1
rank = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for k, v in rank:
    print(f'{n1}°{k}: {v}')
    n1 += 1

