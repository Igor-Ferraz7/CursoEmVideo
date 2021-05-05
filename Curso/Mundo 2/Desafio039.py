br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
n = int(input('Digite sua idade:'))
f = 18 - n
p = n - 18
if n > 18:
    print(f'Você ja passou da idade de se alistar. Se passaram {p} anos do prazo do alistamento.')
elif n < 18:
    print(f'Você ainda irá se alistar ao exército. Falta apenas {f} anos!')
elif n == 18:
    print('Você já está na idade de se alistar!\n Prepare-se.')