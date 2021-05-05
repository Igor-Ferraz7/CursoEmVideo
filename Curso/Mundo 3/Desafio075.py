n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
n3 = int(input('Digite o 3° valor: '))
n4 = int(input('Digite o 4° valor: '))
nt = n1,n2,n3,n4
n9 = nt.count(9)
print(f'Apareceu {n9} vezes o valor 9.')
if 3 in nt:
    nts = nt.index(3)
    print(f'O 3 apareceu na posição {nts+1}.')
if 3 not in nt:
    print('O número 3 não apareceu nenhuma vez.')
print('Os números pares são: ', end='')
for c in nt:
    if c % 2 == 0:
        print(c, end=', ')
print('\b\b.')