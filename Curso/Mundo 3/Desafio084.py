dados = []
geral = list()
dc = ''
lista = []
totpe = 0
mai = men = 0
while dc != 'N':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(geral) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    geral.append(dados[:])
    dados.clear()
    totpe += 1
    dc = str(input('Quer continuar? [S/N] ')).upper()
    if dc == 'S':
        print('='*30)
        print('Ok')
        print('='*30)
print(f'Há {totpe} pessoas cadastradas.')
print(f'O maior peso foi {mai}Kg de:', end=' ')
for p in geral:
    if p[1] == mai:
        print(p[0], end=', ')
print('\b\b.')
print(f'E o menor foi {men}Kg de:', end=' ')
for p in geral:
    if p[1] == men:
        print(p[0], end=', ')
print('\b\b.')