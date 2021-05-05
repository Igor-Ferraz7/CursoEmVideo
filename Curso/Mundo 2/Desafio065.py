ma = 0
mn = 0
sn = ''
n = 0
cont = 0
sm = 0
me = 0
while sn != 'N':
    n = float(input('Digite um número: '))
    sn = str(input('Quer continuar?[S/N] ')).upper()
    cont += 1
    sm += n
    me = sm / cont
    if cont == 1:
        ma = mn = n
    else:
        if n > ma:
            ma = n
        elif n < mn:
            mn = n
print(f'Maior: {ma:.0f}\nMenor: {mn:.0f}\nMédia: {me:.2f}\nVezes: {cont}')
