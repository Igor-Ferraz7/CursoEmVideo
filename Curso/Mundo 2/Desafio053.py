br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
am = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
a = str(input(f'{c}Digite uma palavra{br}: ')).strip().upper()
s = a.split()
junto = ''.join(s)
inv = ''
for c in range(len(junto) - 1, -1, -1):
    inv += junto[c]
    if a == inv:
        print(f'{vd}Sua palavra {az}{a}{vd} é um palíndromo{br}.', end='')
if a != inv:
    print(f'{vm}Sua palavra {az}{a}{vm} não é um palíndromo{br}.')