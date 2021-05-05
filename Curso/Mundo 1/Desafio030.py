n = int(input('Digite um número qualquer número:'))
num = n % 2
list = [0, 2, 4, 6, 8]
if num in list:
    print('Seu número é \033[33mpar\033[m.')
else:
    print('Seu número é \033[34mímpar\033[m.')