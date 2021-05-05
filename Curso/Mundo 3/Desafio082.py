l = []
p = []
while True:
    n = int(input('Digite um valor: '))
    l.append(n)
    p.append(n)
    sn = str(input('Quer encerrar?[S/N] '))
    if sn in 'Ss':
        break
print(f'Lista: {l}')
for np in l:
    if np % 2 == 0:
        l.remove(np)
print(f'Impares: {l}')
for ni in p:
    if ni % 2 == 1:
        p.remove(ni)
print(f'Pares: {p}')
# ----------------------------------------------------------------------
# outra forma ----------------------------------------------------------
# ----------------------------------------------------------------------
# l = []
# while True:
#     n = int(input('Digite um valor: '))
#     l.append(n)
#     sn = str(input('Quer encerrar?[S/N] '))
#     if sn in 'Ss':
#         break
# p = l[:]
# im = l[:]
# print(f'Lista: {l}')
# for np in im:
#     if np % 2 == 0:
#         im.remove(np)
# print(f'Impares: {im}')
# for ni in p:
#     if ni % 2 == 1:
#         p.remove(ni)
# print(f'Pares: {p}')
# --------------------------------------------------------------------
# forma corrigida ----------------------------------------------------
# --------------------------------------------------------------------
# lis = list()
# par = list()
# imp = list()
# while True:
#     lis.append(int(input('Digite um valor: ')))
#     es = str(input('Es: '))
#     if es in 'Nn':
#         break
# for i, v in enumerate(lis):
#     if v % 2 == 0:
#         par.append(v)
#     elif v % 2 == 1:
#         imp.append(v)
# print(lis)
# print(par)
# print(imp)
# FIM--------------------------------------------------------