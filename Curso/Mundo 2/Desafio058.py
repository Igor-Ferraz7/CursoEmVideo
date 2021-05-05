import random, time
print('Irei pensar em um número entre 0 a 10.')
time.sleep(1)
print('PENSANDO...')
time.sleep(1)
ad = int(input('Agora tente adivinhar o número em que pensei: '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rd = random.choice(lista)
palpite = 1
if ad != rd:
    while ad != rd:
        ad = int(input('Você errou!\nTente novamente: '))
        palpite += 1
        if ad == rd:
            print(f'Parabéns!! Você acertou!\nFoi nessessário {palpite} vezes para acertar.')
elif ad == rd:
    print('Parabéns!! Você acertou de primeira!')