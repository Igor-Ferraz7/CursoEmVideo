br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
ma = 0
mn = 0
sf = 0
s = 0
maf = 0
mnf = 0
nmh = ''
nmnf = ''
ttf = 0
for c in range(1, 5):
    s += 1
    id = int(input(f'Idade da {s}° pessoa: '))
    sf += id
    nm = str(input(f'Nome da {s}° pessoa: '))
    sx = str(input(f'Sexo da {s}° pessoa: ')).upper()
    if c == 1 and sx in 'Mm':
        ma = id
        nmh = nm
    if sx in 'Mm' and id > ma:
        ma = id
        nmh = nm
    elif id < 20 and sx in 'Ff':
        ttf += 1
print(f'O homem mais de idade é: {nmh} e tem {ma} anos\nNo total há {ttf} mulheres com menos de 20 anos.')
m = sf / 4
print(f'A média da idade do grupo é de {m:.0f} anos.')