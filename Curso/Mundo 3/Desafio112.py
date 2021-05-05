from exs111.UtilidadeCemV import dados

p = dados.leiadinheiro('Digite o preço: ')
if float(100*2) == dados.moeda.moeda.dobro(100):
    ha = False
else:
    ha = True
dados.moeda.resumo(p, 80, 35, ha)
