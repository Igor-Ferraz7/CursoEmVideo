from time import sleep
lista = []
def maior(*n):
    for nu in n:
        lista.append(nu)
    ma = sorted(lista[:])
    print('Analisando valores passados...')
    for nu in n:
        print(f'{nu}', end=' ')
        sleep(0.3)
    print(f'\b. Foram informado {sum(lista)} valores ao todo.')
    print(f'O maior é: {ma[-1]}.\n'
          f'E o menor é: {ma[0]}.')
    print('-=' * 30)
    lista.clear()

print('-='*30)
maior(2, 4, 1, 8, 4)
maior(7, 1, 0)
maior(1, 2)
maior(0)