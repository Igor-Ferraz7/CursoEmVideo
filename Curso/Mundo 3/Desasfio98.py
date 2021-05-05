from time import sleep
def contagem(n1, n2, n3):
    a = str(n3)
    asd = 0
    if n3 == 0:
        n3 += 1
    if n1 > n2 and '-' not in a:
        for c in range(n1, n2, -n3):
            print(c, end=' ')
            sleep(0.3)
            asd = c
        if '-' in str(n2) and asd != n2 and n3 > 1 and n1 % 2 == 1 and n2 % 2 == 0:
            print('FIM!')
        elif '-' not in str(n2) and asd != n2 and asd - n3 == n2:
            print(asd - n3, 'FIM!')
        elif '-' in str(n2) and asd != n2 and asd - n3 == n2:
            print(asd - n3, 'FIM!')
        else:
            print('FIM!')
    else:
        for c in range(n1, n2, n3):
            print(c, end=' ')
            sleep(0.3)
            asd = c
        if asd != n2 and asd + n3 == n2:
            print(asd + n3, "FIM!")
        else:
            print('FIM!')


n1 = int(input('Início: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
contagem(n1, n2, n3)
