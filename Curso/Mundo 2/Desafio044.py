br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
cal = 'Calculadora'
print(f'{cal:=^77}')
print("""[1] Á vista com dinheiro/cheque.
[2] Á vista no cartão.
[3] Em até 2x no cartão.
[4] Em 3x ou mais no cartão.""")
es = int(input('Digite a opção que deseja: '))
if es == 1:
    n = float(input('Preço do produto:'))
    desc = (n * 10) / 100
    df = n - desc
    print(f'Você terá um desconto de 10% que ficará R${df:.2f}')
elif es == 2:
    n = float(input('Preço do produto:'))
    cp = (n * 5) /100
    cpf = n - cp
    print(f'Você terá um desconto de 5% que passará ser R${cpf:.2f}')
elif es == 3:
    n = float(input('Preço do produto:'))
    print(f'O preço será de R${n:2.f}')
elif es == 4:
    n = float(input('Preço do produto:'))
    jc = (n * 20) / 100
    jcf = n + jc
    print(f'Você terá juros de 20% e o preço passará a ser de R${jcf:.2f}')
else:
    print('Opção inválida.')