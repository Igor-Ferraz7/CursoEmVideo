a = '\033[33m'
vd = '\033[32m'
vm = '\033[31m'
az = '\033[4;34m'
r = '\033[4;35m'
c = '\033[36m'
des = '\033[m'
s = float(input('Quanto é seu salário? R$'))
if s > 1250:
    a = (s * 10) /100
    au = s + a
    print(f'Seu salarário de R${az}{s}{des} passará a ser de R${r}{au:.2f}{des}')
elif s <= 1250:
    na = (s * 15) /100
    nau = s + na
    print(f'Seu salário de R${az}{s}{des} passará a ser de R${r}{nau:.2f}')