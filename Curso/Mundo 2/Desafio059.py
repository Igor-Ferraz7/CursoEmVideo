n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
d = ' '
lista = [1, 2, 3, 4, 5]
print("""[1] Somar
[2] Mutiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
c = int(input('Digite sua opção: '))
print('-=-'*7)
if c != 5 and c < 5:
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
    elif c == 5:
        print('Fim')
        print('-=-' * 7)
    while c == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
        print("""[1] Somar\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
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
        elif c == 5:
            print('Fim')
            print('-=-' * 7)
    while c != 5 and c in lista:
        print("""[1] Somar\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
        c = int(input('Digite sua nova opção: '))
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
        elif c == 5:
            print('Fim')
            print('-=-' * 7)
        while c == 4:
            n1 = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            print("""[1] Somar\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
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
            elif c == 5:
                print('Fim')
                print('-=-' * 7)
elif c == 5:
    print('Fim')
    print('-=-' * 7)
elif c > 5:
    while c != 1 and c != 2 and c != 3 and c != 4 and c != 5:
        c = int(input('Opção inválida. Tente novamente: '))
        if c != 5 and c < 5:
            if c != 5 and c < 5:
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
                elif c == 5:
                    print('Fim')
                    print('-=-' * 7)
                while c == 4:
                    n1 = float(input('Primeiro valor: '))
                    n2 = float(input('Segundo valor: '))
                    print("""[1] Somar\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
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
                    elif c == 5:
                        print('Fim')
                        print('-=-' * 7)
                while c != 5 and c in lista:
                    print("""[1] Somar\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
                    c = int(input('Digite sua nova opção: '))
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
                    elif c == 5:
                        print('Fim')
                        print('-=-' * 7)
                    while c == 4:
                        n1 = float(input('Primeiro valor: '))
                        n2 = float(input('Segundo valor: '))
                        print("""[1] Somar\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
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
                        elif c == 5:
                            print('Fim')
                            print('-=-' * 7)
        elif c == 5:
            print('Fim')
            print('-=-' * 7)