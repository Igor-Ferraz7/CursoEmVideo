lista = ('Lápis', 1.75, 'Borracha', 3.05, 'Caderno', 4.75, 'Estojo', 5.00,
'Transferidor', 6.25,  'Compasso', 5.35, 'Mochila', 21.90, 'Canetas', 2.50, 'Livro', 67.39)
print('-'*37)
print('Listagem de preços:')
print('-'*37)
for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<30}', end='')
    else:
        print(f'R${lista[n]:>5.2f}')
print('-'*37)
