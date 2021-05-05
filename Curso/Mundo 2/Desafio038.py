a = '\033[33m'
br = '\033[30m'
vm = '\033[4;31m'
az = '\033[34m'
r = '\033[35m'
ci = '\033[36m'
des = '\033[m'
n = int(input(f'{br}-{ci}Primeiro número{br}: '))
n2 = int(input(f'{br}-{ci}Segundo número{br}: '))
if n > n2:
    print(f'{az}O número {br}{n}{az} é maior que o {br}{n2}{az}.')
elif n2 > n:
    print(f'{r}O número {br}{n2}{r} é maior que o {br}{n}{r}.')
elif n == n2:
    print(f'{vm}Os números colocados são iguais{des}{br}.')