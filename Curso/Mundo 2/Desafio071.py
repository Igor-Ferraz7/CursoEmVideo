asd = 'Banco'
print('-=' * 30)
print(f'{asd:-^60}')
print('-=' * 30)
vl = int(input('Quanto quer sacar? R$'))
ced = 50
tot = vl
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break