am = '\033[33m'
vd = '\033[4;32m'
vm = '\033[4;31m'
az = '\033[34m'
r = '\033[35m'
ci = '\033[36m'
des = '\033[m'
a = int(input(f'{ci}Primeira reta{des}:'))
b = int(input(f'{ci}Segunda reta{des}:'))
c = int(input(f'{ci}Terceira reta{des}:'))
if a < b + c and b < a + c and c < a + b:
    print(f'{vd}As retas acima podem formar um triângulo{des}.')
else:
    print(f'{vm}As retas acima não podem formar um triângulo{des}.')
