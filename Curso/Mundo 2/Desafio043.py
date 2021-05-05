br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
al = float(input(f'{c}Altura{br}:'))
p = float(input(f'{c}Peso{br}:'))
imc = p / (al**2)
if imc < 18.5:
    print(f'{vd}Você está abaixo do peso{br}.')
elif imc >= 18.5 and imc < 25:
    print(f'{az}Você possui o peso ideal{br}.')
elif imc >= 25 and imc < 30:
    print(f'{a}Você está sobrepeso{br}.')
elif imc >= 30 and imc < 40:
    print(f'{vm}Você está obeso{br}.')
elif imc > 40:
    print(f'\033[31;4mVocê possui obesidade mórbida.')