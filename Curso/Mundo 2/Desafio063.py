print('-'*30)
print('Sequência Fibonacci')
print('-'*30)
t = int(input('Quantos termos? '))
cont = 3
n1 = 0
n2 = 1
print(f'{n1} ➞ {n2}', end='')
while cont <= t:
    n3 = n1 + n2
    print(f' ➞ {n3}', end='')
    cont += 1
    n1 = n2
    n2 = n3
print(' ➞ FIM')
print('-'*30)