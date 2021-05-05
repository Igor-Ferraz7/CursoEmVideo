from exs107 import moeda
n1 = float(input('Digite o preço: R$'))
print(f'A metade de {n1} é {moeda.metade(n1):.2f}\n'
      f'O dobro de {n1} é {moeda.dobro(n1):.2f}\n'
      f'Com o aumento de 10% temos {moeda.aumento(n1):.2f}\n'
      f'Com uma diminuição de 13% temos {moeda.dim(n1):.2f}')
