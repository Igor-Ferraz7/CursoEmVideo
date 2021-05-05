c = 0
while c != 5 and c < 5:
    n1 = float(input('Primeiro valor: '))
    n2 = float(input('Segundo valor: '))
    d = ' '
    print("""[1] Somar
[2] Mutiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
    c = int(input('Digite sua opção: '))
    print('-=-' * 7)
    if c == 1:
        sm = n1 + n2
        print(f'A soma é: {sm:.0f}')
        print('-=-' * 7)
    elif c == 2:
        vz = n1 * n2
        print(f'{n1} x {n2} = {vz}')
        print('-=-' * 7)
    elif c == 3:
        if n1 > n2:
            print(f'{d:^7}{n1:.0f} > {n2:.0f}')
            print('-=-' * 7)
        elif n2 > n1:
            print(f'{d:^7}{n2:.0f} > {n1:.0f}')
            print('-=-' * 7)
        elif n1 == n2:
            print('Os valores são iguais.')
            print('-=-' * 7)
    elif c == 4:
        n1 = float(input('Primeiro novo valor: '))
        n2 = float(input('Segundo novo valor: '))
        print("""   [1] Somar
    [2] Mutiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""")
        c = int(input('Digite sua opção: '))
        print('-=-' * 7)
    elif c == 5:
        print(f'{d:^8}Fim')
        print('-=-' * 7)
orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
n1 = int(input('digite um numero:'))
n2 = int(input('digite outro:'))
opção = 0
while opção != 5:
    print ('---'*8)
    print ('''[01] somar
[02] multiplicar 
[03] maior
[04] novos numeros
[05] sair do programa''')
    opção = int(input('>>>'))
    if opção == 1:
        soma =  n1 + n2
        print ('a soma entre {} é {} e igual a {}'.format(n1,n2,soma))
    elif opção == 2:
        mult = n1 + n2
        print ('a multiplicação de {} é {} e igual a {}'.format(n1,n2,mult))
    elif opção == 3:
        if n1 > n2:
            print ('o maior dos números {} e {} e o {}'.format(n1,n2,n1))
        if n1 < n2:
            print ('o maior dos números {} e {} e o {}'.format(n1,n2,n2))
    elif opção == 4:
        n1 = int(input('digite um numero:'))
        n2 = int(input('digite outro:'))
print ('fim do programa')