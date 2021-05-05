from operator import itemgetter
lista = []
lista2 = []
listaF = []
listama = []
dic = {}
dc = ''
n = n1 = 0
print('-='*30)
while dc != 'N':
    lista.append(dic.copy())
    lista[n]['Nome'] = str(input('Nome: '))
    lista[n]['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    if lista[n]['Sexo'] == 'F':
        listaF.append(lista[n]['Nome'])
    lista[n]['Idade'] = int(input('Idade: '))
    lista2.append(lista[n]['Idade'])
    n += 1
    dc = str(input('Quer continuar? ')).upper()
    print('-='*30)
mf = (sum(lista2)) / n
for d in lista:
    if lista[n1]['Idade'] > mf:
        listama.append(lista[n1]['Nome'])
    n1 += 1
print(f'Foram cadastradas {n} pessoas.\n'
      f'A média de idade é {mf:.0f}')
print(f'Mulheres presentes no cadastro são: ', end='')
print(*listaF, sep=', ', end='')
print('.')
print(f'As pessoas com a idade acima da média são: ', end='')
print(*listama, sep=', ', end='')
print('.')
print('-='*30)