def metade(n):
    a = n / 2
    return a


def dobro(n):
    d = n * 2
    return d


def aumento(n):
    au1 = (n * 10) / 100
    auf = n + au1
    return auf


def dim(n):
    dm1 = (n * 13) / 100
    dmf = n - dm1
    return dmf


def moeda(n=0, moeda=f'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


