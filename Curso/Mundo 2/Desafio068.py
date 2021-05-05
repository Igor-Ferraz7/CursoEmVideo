import time, random
ase = ''
cont = 0
print('Vamos lá!')
while ase != 'GAME OVER':
    pi = str(input('Par ou ímpar? ')).upper()
    time.sleep(1)
    print('Um...')
    time.sleep(1)
    print('Dois..')
    time.sleep(1)
    print('Três..')
    rd = random.randint(1, 10)
    n = int(input('Digite o valor: '))
    sm = n + rd
    if (rd + n) % 2 == 1 and pi == 'PAR':
        print(f'Ah, que pena! Você perdeu..\n O computador escolheu {rd} e você {n}, no total: {sm} e deu ÍMPAR.')
        print('-=' * 30)
        ase = 'GAME OVER'
        print(f'{ase:-^60}')
        print('-=' * 30)
        break
    elif (rd + n) % 2 == 0 and pi == 'IMPAR' or (rd + n) % 2 == 0 and pi == 'ÍMPAR':
        print(f'Ah, que pena! Você perdeu..\n O computador escolheu {rd} e você {n}, no total: {sm} e deu PAR.\n Você venceu {cont} vezes.')
        print('-=' * 30)
        ase = 'GAME OVER'
        print(f'{ase:-^60}')
        print('-=' * 30)
        break
    else:
        print(f'O computador escolheu {rd} e você {n}, no total: {sm} e deu {pi}.\nParabéns! Você ganhou..')
        print('-=' * 30)
        time.sleep(1)
        print('Vamos jogar novamente..')
        cont += 1
