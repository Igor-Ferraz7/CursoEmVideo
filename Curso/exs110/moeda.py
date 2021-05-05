from exs109 import moeda
if float(50) == moeda.metade(100):
    ha = False
else:
    ha = True
def aumento2(n, au, cf=ha):
    au1 = (n * au) / 100
    auf = n + au1
    return auf if ha is False else moeda.moeda(auf)


def dima(n, dia, n1=ha):
    dm1 = (n * dia) / 100
    dmf = n - dm1
    return dmf if ha is False else moeda.moeda(dmf)


def resumo(na, au=0, di=0, n2=ha):
    print('-'*30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)
    print(f'{"Preço analisado"}{"":>3}{moeda.moeda(n=na)}\n'
          f'Dobro do preço:{"":>3}{moeda.dobro(n=na, n1=n2)}\n'
          f'Metade do preço:{"":>2}{moeda.metade(n=na, n1=n2)}\n'
          f'{au}% de aumento:{"":>3}{aumento2(na, au, cf=n2)}\n'
          f'{di}% de redução:{"":>3}{dima(na, di, n2)}')
    print('-' * 30)
