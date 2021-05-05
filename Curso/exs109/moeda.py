def moeda(n=0, moeda=f'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


dc = str(input('Deseja mostrar em valor monetário?[S/N] ')).upper()
if dc == 'S':
    ha = True
else:
    ha = False
def metade(n, n1=ha):
    a = n / 2
    return a if ha is False else moeda(a)
def dobro(n, n1=ha):
    d = n * 2
    return d if ha is False else moeda(d)


def aumento(n, n1=ha):
    au1 = (n * 10) / 100
    auf = n + au1
    return auf if ha is False else moeda(auf)


def dim(n, n1=ha):
    dm1 = (n * 13) / 100
    dmf = n - dm1
    return dmf if ha is False else moeda(dmf)
