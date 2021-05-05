#from random import randint
#i = ['Pedra', 'Papel', 'Tesoura']
#c = randint(0, 2)
#print(f'{i[c]}')
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
print("""[1] Somar
[2] Mutiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
c = int(input('Digite sua opção: '))
if c != 5:
    if c == 1:
        sm = n1 + n2
        print(f'Soma é: {sm:.1f}')
    elif c == 2:
        vz = n1 * n2
        print(f'A multiplicação é {vz:.1f}')
    elif c == 3:
        if n1 > n2:
            print(f'O maior é {n1:.1f}')
        elif n2 > n1:
            print(f'Maior é {n2:.1f}')
        elif n1 == n2:
            print(f'Os valores digitados são iguais.')
    elif c == 5:
        print('Tchau.')
    while c == 4:
        if c == 5:
            print('Tchau.')
        n1 = float(input('Novo primeiro valor: '))
        n2 = float(input('Novo segundo valor: '))
        c = int(input('Digite sua opção: '))
        if c == 1:
            sm = n1 + n2
            print(f'Soma é: {sm:.1f}')
        elif c == 2:
            vz = n1 * n2
            print(f'A multiplicação é {vz:.1f}')
        elif c == 3:
            if n1 > n2:
                print(f'O maior é {n1:.1f}')
            elif n2 > n1:
                print(f'Maior é {n2:.1f}')
            elif n1 == n2:
                print(f'Os valores digitados são iguais.')
        elif c == 5:
            print('Tchau.')
            while c == 4:
                n1 = float(input('Novo primeiro valor: '))
                n2 = float(input('Novo segundo valor: '))
                if c == 1:
                    sm = n1 + n2
                    print(f'Soma é: {sm:.1f}')
                elif c == 2:
                    vz = n1 * n2
                    print(f'A multiplicação é {vz:.1f}')
                elif c == 3:
                    if n1 > n2:
                        print(f'O maior é {n1:.1f}')
                    elif n2 > n1:
                        print(f'Maior é {n2:.1f}')
                    elif n1 == n2:
                        print(f'Os valores digitados são iguais.')
                elif c == 5:
                    print('Tchau.')
    while c != 5:
        c = int(input('Digite sua nova opção: '))
        if c == 1:
            sm = n1 + n2
            print(f'Soma é: {sm:.1f}')
        elif c == 2:
            vz = n1 * n2
            print(f'A multiplicação é {vz:.1f}')
        elif c == 3:
            if n1 > n2:
                print(f'O maior é {n1:.1f}')
            elif n2 > n1:
                print(f'Maior é {n2:.1f}')
            elif n1 == n2:
                print(f'Os valores digitados são iguais.')
        elif c == 5:
            print('Tchau.')
        while c == 4:
            n1 = float(input('Novo primeiro valor: '))
            n2 = float(input('Novo segundo valor: '))
            c = int(input('Digite sua opção: '))
            if c == 1:
                sm = n1 + n2
                print(f'Soma é: {sm:.1f}')
            elif c == 2:
                vz = n1 * n2
                print(f'A multiplicação é {vz:.1f}')
            elif c == 3:
                if n1 > n2:
                    print(f'O maior é {n1:.1f}')
                elif n2 > n1:
                    print(f'Maior é {n2:.1f}')
                elif n1 == n2:
                    print(f'Os valores digitados são iguais.')
            elif c == 5:
                print('Tchau.')
                while c == 4:
                    n1 = float(input('Novo primeiro valor: '))
                    n2 = float(input('Novo segundo valor: '))
                    if c == 1:
                        sm = n1 + n2
                        print(f'Soma é: {sm:.1f}')
                    elif c == 2:
                        vz = n1 * n2
                        print(f'A multiplicação é {vz:.1f}')
                    elif c == 3:
                        if n1 > n2:
                            print(f'O maior é {n1:.1f}')
                        elif n2 > n1:
                            print(f'Maior é {n2:.1f}')
                        elif n1 == n2:
                            print(f'Os valores digitados são iguais.')
                    elif c == 5:
                        print('Tchau.')
elif c == 5:
    print('Tchau.')