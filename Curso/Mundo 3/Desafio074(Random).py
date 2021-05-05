import random
rdt = (random.randrange(1,11), random.randrange(1,11), random.randrange(1,11), random.randrange(1,11),
random.randrange(1,11))
print(f'Listagem dos números aleatórios:')
for n in rdt:
    print(n,end=' ')
rdtl = sorted(rdt)
rdm = rdtl[-1]
rdmn = rdtl[0]
print(f'\nMaior: {rdm}\nMenor: {rdmn}')
