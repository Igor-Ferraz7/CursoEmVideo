a = '\033[33m'
vd = '\033[32m'
vm = '\033[31m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
n = int(input(f'{c}Diga um ano qualquer{des}:'))
b = n % 4
if b == 0:
    print(f'{az}O ano{des} {r}{n}{des} {az}é bissexto.{des}')
else:
    print(f'{vm}O ano{des} {a}{n}{a} {vm}não é bissexto.{des}')