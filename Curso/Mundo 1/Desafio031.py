a = '\033[33m'
vd = '\033[32m'
vm = '\033[31m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
v = float(input('Diga a distância da viagem: '))
if v <= 200:
    p = 0.50 * v
    print(f'O valor da passagem é R${az}{p}{des}')
else:
    pr = 0.45 * v
    print(f'O valor da passagem é R${vm}{pr}{des}')