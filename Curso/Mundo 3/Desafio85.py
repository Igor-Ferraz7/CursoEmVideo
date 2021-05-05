lista = [[], []]
for c in range(0, 7):
    lista[0].append(int(input(f'Digite o {c+1}° número: ')))
    for n in lista[0]:
        if n % 2 == 1:
            lista[1].append(n)
            lista[0].remove(n)
ordpa = sorted(lista[0])
ordim = sorted(lista[1])
print('-='*30)
print(f'Pares: {lista[0]}\nÍmpares: {lista[1]}')
print('-='*30)
