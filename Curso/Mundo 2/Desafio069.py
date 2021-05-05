id = 0
asd = 'Cadrastos'
ps = 0
id18 = 0
mtt = 0
ftt = 0
print('-=' * 30)
print(f'{asd:-^60}')
print('-=' * 30)
while True:
    ps += 1
    id = int(input(f'Digite a idade da {ps}º pessoa: '))
    if id >= 18:
        id18 += 1
    sx = ' '
    while sx not in 'MF':
        sx = str(input(f'Digite o sexo da {ps}º pessoa [M/F]: ')).upper()
        if id < 20 and sx == 'F':
            ftt += 1
        if sx == 'M':
            mtt += 1
    print('-=' * 30)
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar?[S/N]: ')).upper()
    print('-=' * 30)
    if esc == 'N':
        break
print('-=' * 30)
print(f'Há {id18} pessoas com mais de 18 anos.')
print(f'Há {mtt} pessoas masculinas cadastradas.')
print(f'Há {ftt} mulheres com menos de 20 anos.')
print('-=' * 30)