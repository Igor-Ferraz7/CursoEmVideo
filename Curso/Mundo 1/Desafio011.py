dsf = 'Desafio'
print(f'{dsf:=^33}')
s = float(input('Salário:R$'))
pr = (s * 15) / 100
au = pr + s
print(f'O seu novo salário com o aumento de 15% é {au:.2f} .')
print('='*33)