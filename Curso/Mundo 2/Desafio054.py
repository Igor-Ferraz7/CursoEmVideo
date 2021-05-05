br = '\033[30m'
vm = '\033[31m'
vd ='\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
from datetime import date
s = 0
t1 = 0
t2 = 0
for c in range(1,8):
    s += 1
    ano = int(input(f'Em que ano a {s} pessoa nasceu? '))
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        t1 += 1
    else:
        t2 += 1
print(f'{t1} pessoas maiores de idade.')
print(f'{t2} Pesoas menores de idade')
