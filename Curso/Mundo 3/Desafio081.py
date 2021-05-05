l = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    l.append(n)
    sn = str(input('Quer continuar? [S/N]: '))
    if sn in 'Nn':
        break
rev = sorted(l, reverse=True)
print(f'Você digitou {cont} números.')
print(f'Ordem decrescente: {rev}')
if 5 not in l:
    print('O número 5 não está na lista.')
else:
    print('O número 5 está na lista.')