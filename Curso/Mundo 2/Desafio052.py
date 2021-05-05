br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
ci = '\033[36m'
des = '\033[m'
np = int(input('Digite um número: '))
s = 0
for c in range(1, np +1):
    if np % c == 0:
        print(f'{az}{c}', end=' ')
        s += 1
    else:
        print(f'{vm}{c}', end=' ')
if s == 2:
    print(f'\n{des}{np} é primo pois foi divisível apenas por {s} números.')
elif s > 2:
    print(f'\n{des}{np} não é primo pois foi divisível por {s} números.')