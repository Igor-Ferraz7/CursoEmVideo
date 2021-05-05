import random, time
lpa = []
n = 0
def sorteia(lis):
    # for c in lis:
    #     numeros.append(c)
    print(f'Sorteando 5 valores:', end=' ')
    for c in range(0, 5):
        valor = random.randint(1, 10)
        if valor % 2 == 0:
            lpa.append(valor)
        print(valor, end=' ')
        time.sleep(0.3)
        lis.append(valor)
    print('PRONTO!')
def somaPar(lis):
    sm = 0
    for c in lis:
        if c % 2 == 0:
            sm += c
    print(f'Somando os valores pares de {lis}, temos {sm}.')


numeros = []
sorteia(numeros)
somaPar(numeros)