dic = {}
dic['Nome'] = str(input('Nome do jogador: '))
dic['Número de partidas'] = int(input('Números de partidas: '))
n1 = 0
lista = []
print('=-'*30)
for n in range(0, dic['Número de partidas']):
    valor = int(input(f'- Quantos gols na {n+1}° partida? '))
    lista.append(valor)
print('=-'*30)
dic['gols'] = lista
for k, v in dic.items():
    print(f'{k}: {v}')
print('=-'*30)
print(f'O jogador {dic["Nome"]} jogou {dic["Número de partidas"]} partidas..')
for n in dic['gols']:
    print(f'  => Na {n1+1}° partida, fez {n} gols.')
    n1 += 1
print('=-'*30)
print(f'Foi um total de {sum(dic["gols"])} gols.')
print(dic)