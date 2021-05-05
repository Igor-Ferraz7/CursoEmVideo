from exs108 import moeda
n1 = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(n1)} é {moeda.moeda(moeda.metade(n1))}\n'
      f'O dobro de {moeda.moeda(n1)} é {moeda.moeda(moeda.dobro(n1))}\n'
      f'Com o aumento de 10% temos {moeda.moeda(moeda.aumento(n1))}\n'
      f'Com uma diminuição de 13% temos {moeda.moeda(moeda.dim(n1))}')

# dc = str(input('Deseja mostrar em valor monetário?[S/N] ')).upper()
# if dc == 'S':
#     ha = True
# else:
#     ha = False
# def metade(n, n1=True or False):
#     a = n / 2
#     if n1 == True:
#         return moeda(a)
#     else:
#         return a
#
# def dobro(n):
#     d = n * 2
#     return d
#
#
# def aumento(n):
#     au1 = (n * 10) / 100
#     auf = n + au1
#     return auf
#
#
# def dim(n):
#     dm1 = (n * 13) / 100
#     dmf = n - dm1
#     return dmf
#
#
# def moeda(n=0, moeda=f'R$'):
#     return f'{moeda}{n:.2f}'.replace('.', ',')
