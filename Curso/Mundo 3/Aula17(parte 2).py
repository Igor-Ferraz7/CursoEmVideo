dados = []
pessoas = []
n = ma = men = 0
for c in range(0,2):
    dados.append(str(input('N: ')))
    dados.append(int(input('I: ')))
    pessoas.append(dados[:])
    dados.clear()
    c += 1
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        ma += 1
    else:
        print(f'{p[0]} é menor de idade.')
        men += 1
print(f'Há {ma} maiores de idade, e {men} menores de idade.')