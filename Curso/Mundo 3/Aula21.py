# def fatorial(n=1):
#     f = 1
#     for c in range(n, 0, -1):
#         f *= c
#     return f
#
#
# n = int(input('Digite um número para seu fatorial: '))
# print(f'O fatorial de {n} é {fatorial(n)}')
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('D: '))
print(f'{n} é par? ', end='')
if par(n):
    print('Sim')
else:
    print('Não')