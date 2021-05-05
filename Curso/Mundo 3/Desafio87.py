lista = [[], [], []]
valor = 0
c2 = 0
c1 = 0
n = 0
for c in range(0, 9):
    valor = int(input(f'Digite um valor para a posição [{c2}, {c1}]: '))
    lista[n].append(valor)
    c1 += 1
    if c == 2:
        n += 1
        c2 += 1
        c1 -= 3
    if c == 5:
        n += 1
        c2 += 1
        c1 -= 3
sm = lista[0][2] + lista[1][2] + lista[2][2]
nw = 0
a = sorted(lista[1])
asd = '-='
for n in lista:
    for np in n:
        if np % 2 == 0:
            nw += np
print(f'{asd*30}\nAqui está sua matriz: '
      f'\n{lista[0]}\n{lista[1]}\n{lista[2]}\n'
      f'{asd*30}\nA soma de todos os valores pares é: {nw}.\n'
      f'A soma dos valores da terceira coluna é: {sm}.\n'
      f'O maior valor da segunda linha é: {a[-1]}.\n{asd*30}')
