lista = []
dic = {}
dc = ''
n = n1 = 0
lista2 = []
print('-='*53)
while dc != 'N':
    lista.append(dic.copy())
    lista[n]['Nome'] = str(input('Nome do jogador: '))
    lista[n]['Número de partidas'] = int(input('Números de partidas jogadas: '))
    print('-=' * 53)
    for c in range(0, lista[n]['Número de partidas']):
        valor = int(input(f'Gols na {c+1}° partida: '))
        lista2.append(valor)
    print('-=' * 53)
    lista[n]['Gols'] = lista2[:]
    lista2.clear()
    dc = str(input('Continuar? [S/N] ')).upper() [0]
    n += 1
print('-='*53)
print(f'|N°{"":<3}Nome{"":<13}Gols{"":<20}Total|')
print('-'*53)
for nj in range(0, len(lista)):
    a = str(lista[nj]["Gols"])
    print(f'|{nj+1}{"":<3}{lista[nj]["Nome"]:<17}{a:<24}{str(sum(lista[nj]["Gols"])):>6}|')
while True:
    print('-=' * 53)
    lv = int(input('Mostrar dados de qual jogador? ')) - 1
    if lv == 998:
        break
    if lv not in range(0, len(lista)):
        print('Esse jogador não existe. Tente novamente.')
    if lv in range(0, len(lista)):
        print(f'- Levantamento de dados do jogador {lista[lv]["Nome"]}:')
        for j in range(0, lista[lv]['Número de partidas']):
            print(f'No jogo {j+1} ele fez {lista[lv]["Gols"][j]} gols.')
print('<<< Volte Sempre >>>')
