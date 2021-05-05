import random, time
lista = []
lc = []
n = 0
nj = int(input('Quantos jogos? '))
for c in range(0, nj):
    lista.append(lc[:])
for c in range(0, nj):
    for co in range(0, 6):
        nr = random.randint(0, 60)
        if nr not in lista[n]:
            lista[n].append(nr)
        else:
            nre = nr
            while nr == nre:
                lista[n].remove(nr)
                nr = random.randint(0, 60)
                lista[n].append(nr)
            lista[n].append(nre)
    time.sleep(0.3)
    print(f'Jogo {c+1}: {lista[n]}')
    n += 1