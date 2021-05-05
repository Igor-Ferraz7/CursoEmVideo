dsf = 'Desafio'
print(f'{dsf:=^33}')
p = float(input('Preço do produto:R$'))
d = (p * 5) / 100
pf = p - d
print(f'Você pagará {pf} como desconto de 5%.')
print('='*33)