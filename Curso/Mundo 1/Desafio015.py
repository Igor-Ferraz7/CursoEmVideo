from math import sqrt
dsf = 'Desafio'
print(f'{dsf:=^33}')
ca = int(input('Cateto Adjacente:'))
co = int(input('Cateto Oposto:'))
fh = ca**2 + co**2
h = sqrt(fh)
print(f'A hipotenusa é: {h:.2f}')
print('='*33)