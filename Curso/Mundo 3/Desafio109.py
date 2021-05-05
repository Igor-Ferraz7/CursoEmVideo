from exs109 import moeda
n1 = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(n1)} é {moeda.metade(n1)}\n'
      f'O dobro de {moeda.moeda(n1)} é {moeda.dobro(n1)}\n'
      f'Com o aumento de 10% temos {moeda.aumento(n1)}\n'
      f'Com uma diminuição de 13% temos {moeda.dim(n1)}')
