lista = []
lc = []
n = n1 = 0
ct = 1
aqw = 'Nome'
a = '-'
while True:
    lista.append(lc[:])
    nome = str(input('Nome: '))
    lista[n].append(nome)
    lista[n].append(lc[:])
    nota1 = float(input('Nota1: '))
    lista[n][1].append(nota1)
    nota2 = float(input('Nota2: '))
    lista[n][1].append(nota2)
    dc = str(input('Quer continuar? [S/N] ')).upper()
    if dc == 'S':
        print('OK')
        ct += 1
    elif dc == 'N':
        break
    n += 1
print('-='*40)
print(f'N°| {aqw:<15}Média|\n{a*24}|')
for c1 in range(0, ct):
    m = lista[n1][1][0] + lista[n1][1][1]
    mf = m / 2
    print(f'{n1} | {lista[n1][0]:<15}',end='')
    print(f'{mf:>5.1f}|')
    n1 += 1
print('-=' * 40)
while True:
    dc2 = int(input('Mostrar nota de qual aluno?(999 Interrompe): '))
    if dc2 != 999:
        print(f'Notas de {lista[dc2][0]} foram: {lista[dc2][1]}')
        print('-=' * 40)
    else:
        print('-=' * 40)
        break
