br = '\033[30m'
vm = '\033[4;31m'
vd = '\033[32m'
a = '\033[4;33m'
az = '\033[4;34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
n1 = float(input(f'{c}Primeira nota do aluno{br}: '))
n2 = float(input(f'{c}Segunda nota do aluno{br}: '))
m = (n1 + n2) / 2
if m < 5.0:
    print(f'{vm}Você foi reprovado{des}{br}!')
if m >= 5.0 and m <= 6.9:
    print(f'{a}Você está de recuperação{des}{br}.')
elif m > 7.0:
    print(f'{az}Parabéns{des}{br}! {az}Você foi aprovado{des}{br}!')