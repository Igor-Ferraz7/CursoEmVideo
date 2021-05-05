from random import randint
from time import sleep
print('-=-'*22)
print('Irei pensar em um número de 0 a 5, tente adivinhar.')
print('-=-'*22)
r = randint(0,5)
n = int(input('Chute um número de 0 a 5 e veja se acertou:'))
print('Processando...')
sleep(2)
if n == r:
    print(f'Que sortudo! Você acertou! Era {n}, dá pra acreditar?')
else:
    print(f'Que azar..O número sorteado era {r}.')
f = '-=-'
print(f'{f:=^33}')