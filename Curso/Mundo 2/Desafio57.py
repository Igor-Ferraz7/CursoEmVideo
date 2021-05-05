c = str(input('Digite seu sexo [M/F]: ')).upper()
if c == 'F' or c == 'M':
    print('Sexo definido com êxito.')
else:
    while c != 'M':
        c = str(input('Você digitou uma opção inválida. Digite novamante.\nDigite seu sexo[M/F]: ')).upper()
        if c == 'F' or c == 'M':
            print('Sexo definido com êxito.')
            break