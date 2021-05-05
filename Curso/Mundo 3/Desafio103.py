def ficha(n=0, g=0):
    if nm == '':
        n = '<desconhecido>'
    if gol == '':
        g = '0'
    print(f'O jogador {n} fez {g} gol(s) no campeonnato.')


nm = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
ficha(nm, gol)
