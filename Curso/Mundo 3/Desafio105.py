def notas(*n, sit=True):
    lis = []
    for c in n:
        lis.append(c)
    tot = len(lis)
    org = sorted(lis)
    mai = org[-1]
    men = org[0]
    med = sum(lis) / tot
    print(f'Total de números: {tot}\n'
          f'Maior: {mai}\n'
          f'Menor: {men}\n'
          f'Média: {med}')
    if sit == True:
        if med >= 6:
            print('Situação: Aprovado')
        else:
            print('Situação: Reprovado')


notas(2, 3, 1, 8, 4)

# ou

# def notas(*n, sit=True):
#     lis = {}
#     lista = []
#     for c in n:
#         lista.append(c)
#     tot = len(lista)
#     org = sorted(lista)
#     mai = org[-1]
#     men = org[0]
#     med = sum(lista) / tot
#     lis['total'] = tot
#     lis['maior'] = mai
#     lis['menor'] = men
#     lis['média'] = med
#     if sit == True:
#         if med >= 6:
#             lis['situação'] = 'Aprovado'
#         else:
#             lis['situação'] = 'Reprovado'
#     print(lis)
#
#
#
# notas(2, 3, 1, 8, 4)