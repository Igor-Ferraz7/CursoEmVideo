from exs110 import moeda
n1 = float(input('Digite o preço: R$'))
if float(100*2) == moeda.moeda.dobro(100):
    ha = False
else:
    ha = True
moeda.resumo(n1, 80, 35, ha)