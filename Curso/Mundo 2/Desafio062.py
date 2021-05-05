print('Gerador de PA')
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
cont2 = 0
sair = 0
es = 0
while cont <= 10 and es != 190:
    n1 += r
    cont += 1
    print(n1, end=' ➞ ')
print('Pausa')
while es != 190:
    ap = '-='
    print('-='*19)
    es = int(input(f'Para finalizar o programa digite [190]\n{ap*19}\n- Quantas vezes quer mostrar mais? '))
    print('-='*19)
    cont2 = es
    cont2 -= es - 1
    while cont2 <= es and es != 190:
        n1 += r
        cont2 += 1
        print(n1, end=' ➞ ')
    if es != 190:
        print('Pausa')
if es == 190:
    print('FIM')