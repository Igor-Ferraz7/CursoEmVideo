val = []
count = 0
for v in range(1, 6):
    val.append(int(input(f'Digite um valor para a posição {count}: ')))
    count += 1
srt = sorted(val)
ma = srt[-1]
mn = srt[0]
print(f'Você digitou os valores: {val}')
print(f'O maior valor foi: {ma} na posição: ', end='')
count2 = 0
for pos, v in enumerate(val):
    if v == ma:
        print(pos, end=', ')
print('\b\b.')
print(f'O menor valor foi: {mn} na posição: ', end='')
for posn, vl in enumerate(val):
    if vl == mn:
        print(posn, end=', ')
print('\b\b.')
