# import time
# a = '.'
# cont = 0
# print(f'Loading', end='')
# while True:
#     time.sleep(0.3)
#     print(f'{a}', end='')
#     time.sleep(0.3)
#     print(f'{a}', end='')
#     time.sleep(0.3)
#     print(f'{a}', end='')
#     time.sleep(0.3)
#     print('\b\b\b', end='')
#     cont += 1
#     if cont == 3:
#         print('\b\b\b\b\b\b\bLoaded')
#         break
#---------------------------------------------------#
# cont1 = 0
# while cont1 < 5:
#     rd = random.randrange(1,11)
#     print(rd)
#     cont1 += 1
#---------------------------------------------------#
# a = 75
# n1 = 0
# while True:
#     n1 += a
#     print(n1)
#---------------------------------------------------#
# import random
# gatinhodaamanda = 'Malhado', 'Rajado', 'Marrom', 'Cinza', 'Pintado'
# a = random.choice(gatinhodaamanda)
# print(f'O Gatinho da Amanda vai ser: {a}')
#---------------------------------------------------#
# l = 1,5,2,9,4
# s = sorted(l, reverse=True)
# print(s)
#---------------------------------------------------#
# dados = []
# geral = [['Igor', 100],['Jose', 70],['Ana', 100]]
# dc = ''
# lista = []
# totpe = 0
# lista2 = []
# lista3 = [['Igor', 'Jose', 'Ana']]
# a = sorted(geral)
# ma = geral[-1][1]
# mn = geral[1][1]
# for p in geral:
#     if p[1] == ma:
#         lista2.append(p)
# print(lista2[0:1][1])

#---------------------------------------------------#
# lista = [['Igor', [9.0, 8.7]], ['Ana', [7.8, 9.7]]]
# print(lista[0][1][0])
# m = lista[0][1][0] + lista[0][1][1]
# mf = m / 2
# print(mf)
#---------------------------------------------------#
# def test(*n):
#     lis1 = []
#     lis2 = []
#     for a in n:
#         if a % 2 == 0:
#             lis1.append(a)
#         else:
#             lis2.append(a)
#     print(f'Soma dos pares: {sum(lis1)}\n'
#           f'Soma dos ímpares: {sum(lis2)}')
# test(12, 44, 56, 87,99, 9)

#---------------------------------------------------#
def moeda(n=0, moeda=f'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


dc = str(input('Deseja mostrar em valor monetário?[S/N] ')).upper()
if dc == 'S':
    ha = True
else:
    ha = False
def slc(n=0):
    if ha == True:
        return moeda(a)
    else:
        return a
def metade(n, n1=ha):
    a = n / 2
    slc()

def dobro(n, n1=ha):
    d = n * 2
    slc()


def aumento(n, n1=ha):
    au1 = (n * 10) / 100
    auf = n + au1
    slc()


def dim(n, n1=ha):
    dm1 = (n * 13) / 100
    dmf = n - dm1
    slc()



#---------------------------------------------------#