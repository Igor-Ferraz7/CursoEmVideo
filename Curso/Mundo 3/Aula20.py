# a = []
# for c in range(0,5):
#     dec = int(input('Valor: '))
#     a.append(dec)
# def me(a):
#     m = sum(a) / len(a)
#     print(m)
def dob(lis):
    n = 0
    while n < len(lis):
        lis[n] *= 2
        n += 1


lista = [1, 2, 3, 4, 5, 6]
dob(lista)
print(lista)
