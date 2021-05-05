# lista = [[], [], []]
# valor = 0
# c2 = 0
# n = 0
# for c in range(0, 9):
#     valor = int(input(f'Digite um valor para a posição [{c2}, {c}]: '))
#     lista[n].append(valor)
#     if c == 2:
#         n += 1
#         c2 += 1
#     if c == 5:
#         n += 1
#         c2 += 1
# print(f'Aqui está sua matriz: '
#       f'\n{lista[0]}\n{lista[1]}\n{lista[2]}')
# ----------------------------------------------
# -------------Forma do professor---------------
# ----------------------------------------------
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lc in range(0, 3):
    for n in range(0, 3):
        lista[lc][n] = int(input(f'Digite um valor para a posição [{lc}, {n}]: '))
for lc in range(0, 3):
    for n in range(0, 3):
        print(f'{lista[lc][n]:^5}', end='|')
    print()
