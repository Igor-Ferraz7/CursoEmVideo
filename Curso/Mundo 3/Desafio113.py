import cores
def leiaint(x):
    while True:
        try:
            n1 = int(input(x))
        except (ValueError, TypeError):
            print(f'{cores.vermelho}ERRO: Por favor, digite um número inteiro válido.{cores.des}')
            continue
        except (KeyboardInterrupt):
            print(f'{cores.roxo}Ação interrompida pelo usuário.{cores.des}')
            break
        else:
            return n1
def leiareal(x):
    while True:
        try:
            n2 = float(input(x))
        except (ValueError, TypeError):
            print(f'{cores.vermelho}ERRO: Por favor, digite um número real válido.{cores.des}')
            continue
        except (KeyboardInterrupt):
            print(f'{cores.roxo}Ação interrompida pelo usuário.{cores.des}')
            break
        else:
            return n2


a = leiaint('Digite um número inteiro: ')
b = leiareal('Digite um número real: ')
print(f'Número inteiro: {a}\nNúmero real: {b}')
