br = '\033[30m'
vm = '\033[4;31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
ci = '\033[36m'
des = '\033[m'
cvs = '\033[36mConversor\033[30m'
print(f'{br}{cvs:=^78}')
n = int(input(f'\033[4;36mDigite o número inteiro{des}: '))
bi = bin(n)
oc = oct(n)
he = hex(n)
print(f'{br}[1] {a}Binário \n{br}[2] {r}Octal\n{br}[3] {az}Hexadecimal')
c = int(input(f'\033[4;36mEscolha um deles para fazer a conversão{des}: '))
if c == 1:
    print(f'{a}O valor {vd}{n}{a} em binário é{des}: {vd}{bi[2:]}')
elif c == 2:
    print(f'{r}O valor {vd}{n}{r} em octal é{des}: {vd}{oc[2:]}')
elif c == 3:
    print(f'{az}O valor {vd}{n}{az} em hexadecimal é{des}: {vd}{he[2:]}')
else:
    print(f'{vm}- Opção inválida. Tente novamente{des}{br}.')
fim = '\033[36mFIM\033[30m'
print(f'{des}{br}{fim:=^78}')