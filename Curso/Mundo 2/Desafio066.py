cont = sm = n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    sm += n
print(f'A soma dos {cont} valores digitados é: {sm}')
