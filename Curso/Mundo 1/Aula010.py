n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print(f'Sua média final foi: {m:.1f}')
if m >= 6:
    print('Sua nota foi boa. Parabéns!')
else:
    print('Sua nota foi ruim. Estude mais!')
fim = 'FIM'
print(f'{fim:=^33}')