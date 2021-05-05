def leiaInt(txt):
    global n
    val = 0
    ok = False
    while True:
        n = str(input(txt))
        if n.isnumeric():
            val = int(n)
            ok = True
            print(f'Você digitou o número {n}')
            break
        else:
            print('Erro. Digite um número inteiro e válido.')


n = leiaInt('Digite um número: ')