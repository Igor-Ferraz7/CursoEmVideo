t = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Corinthians', 'Flamengo', 'Atlético Mineiro',
'Athletico Paranaense', 'Internacional', 'Chapecoense')
hh = '-='
print(hh * 30)
print('-Primeiros 5 colocados:')
for c in t[:6]:
    print(f'{c}', end=', ')
print('\b\b.')
print(hh * 30)
print('-Últimos 4 colocados: ')
for c1 in t[-4:]:
    print(f'{c1}')
print(hh * 30)
print(f'-Lista em ordem alfabética:')
for c2 in sorted(t):
    print(c2, end=', ')
print('\b\b.\n', end='')
print(hh * 30)
a = t.index('Chapecoense')
print(f'-A Chapecoense está na posição: {a}')
print(hh * 30)