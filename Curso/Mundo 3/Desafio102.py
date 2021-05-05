def fatorial(n=1, show=False):
    """
    --> Calcular Fatorial de um número:
    :param n: Número a ser fatorado.
    :param show: (opcional) Serve para mostrar ou não o processo do cálculo.
    :return: O valor fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show is True:
            print(f'{c} x ', end='')
        elif show is False:
            continue
    print('\b\b\b')
    print(f'O fatorial de {n} é {f}')


a = int(input('Digite um número a ser fatoriado: '))
fot = str(input('Deseja  mostrar o processo? [S/N] ')).upper()
if fot == 'S':
    fots = True
else:
    fots = False
fatorial(a, show=fots)
# help(fatorial)
