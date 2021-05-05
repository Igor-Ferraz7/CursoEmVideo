print('Gerador de PA')
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
sair = 0
es = 0
while cont <= 10:
    n1 += r
    cont += 1
    print(n1, end=' ➞ ')
print('Fim')