n = cont = cont2 = 0
kk = '[Digite um número negativo p/ sair]'
while True:
    print('-=' * 20)
    n = int(input(f'{kk:-^40}\nDigite o valor da tabuada desejada: '))
    print('-=' * 20)
    if n < 0:
        asd = 'FIM'
        print(f'{asd:=^40}')
        print('-=' * 20)
        break
    while True:
        r = n * cont
        print(f'|{n} x {cont} = {r}')
        if cont == 10:
            cont -= cont
            break
        cont += 1