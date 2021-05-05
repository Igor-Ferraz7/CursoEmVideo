am = '\033[33m'
vd = '\033[32m'
vm = '\033[31m'
az = '\033[34m'
r = '\033[35m'
cin = '\033[36m'
des = '\033[m'
a = int(input('Primeiro número:'))
b = int(input('Segundo número:'))
c = int(input('Terceiro número:'))
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'O menor múmero é {menor}.')
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior número é {maior}.')