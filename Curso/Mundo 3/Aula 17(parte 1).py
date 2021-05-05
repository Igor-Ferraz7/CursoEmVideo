# a = list(range(1,11))
# a.append(11)
# a.insert(11,12)
# a.remove(12) #Trabalha com o obj em expecífico
# del a[5] #Trabalha com posição
# a.pop() #Remove o ultimo item ou faz a mesma coisa que o remove
# a.sort(reverse=True)
# print(a)
val = []
for ad in range(1,6):
    val.append(int(input('Digite um valor: ')))
for c,v in enumerate(val):
    print(f'{v} na posição: {c}')
# a = [1,5,3,7]
# b = a #Ligação
# b = a[:] #Cópia