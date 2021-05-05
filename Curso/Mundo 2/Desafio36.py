br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
cp = '\033[34mCalculador de empréstimo\033[33m'
print(f'{a}{cp:=^100}')
casa = float(input(f'{a}-{az}Valor da casa:{des}{vd} R$'))
sal = float(input(f'{a}-{az}Seu salário:{vd} R$'))
anos = float(input(f'{a}-{az}Vai pagar em quantos anos? '))
n1 = casa / (anos*12)
n2 = (sal * 30) / 100
if n1 > n2:
    print(f'{vm}Sua prestação mensal é maior que 30% do seu salário, não poderemos efetuar o empréstimo.')
else:
    print(f"""{az}Você terá que pagar {vd}R${n1:.2f}{des:} {az}por mês em{vd} {anos:.0f}{des}{az} anos até pagar o valor completo da casa.'
Sua prestação será de {vd}R${n1:.2f}""")
fim = '\033[34mFIM\033[33m'
print(f'{a}{fim:=^100}')