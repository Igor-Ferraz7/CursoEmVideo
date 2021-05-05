dsf = 'Desafio'
print(f'{dsf:=^33}')
m = float(input('Digite um valor em metros: '))
k = m / 1000
h = m / 100
da = m / 10
dc = m * 10
c = m * 100
mm = m * 1000
print('Seu valor em: \nKm é: {}km \nHm é: {}hm \nDam é: {}dam \nDcm é: {:.0f}dcm \nCm é: {:.0f}cm \nMm é: {:.0f}mm'.format(k,h,da,dc,c,mm))
print('='*33)