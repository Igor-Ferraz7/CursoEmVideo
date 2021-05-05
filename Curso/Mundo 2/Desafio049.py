br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
ci = '\033[36m'
des = '\033[m'
v = '\033[36m|Calculadora|'
print(f'{vd}-='*15+'-')
print(f'{br}{v:^35}')
print(f'{vd}-='*15+'-')
n = int(input(f'{vd}-{ci}Digite o valor{br}: '))
for c in range(0, 11):
    print(f'{vd}|{des}{ci}', c, end = f'{vd} x {ci}{n}{vd} = {ci}{c*n}\n')
print(f'{vd}-='*15+'-')