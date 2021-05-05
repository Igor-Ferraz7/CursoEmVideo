l = []
count = 0
l.append(int(input('Digite um valor: ')))
print('Salvado com sucesso!')
print('-=' * 20)
d = str(input('Quer continuar?'))
print('-=' * 20)
while d != 'N':
    n = int(input('Digite um valor: '))
    ass = sorted(l)
    if n not in l:
        l.append(n)
        print('Salvado com sucesso!')
        print('-=' * 20)
        d = str(input('Quer continuar?')).upper()
        print('-=' * 20)
    else:
        print('Repetido. Não irei adicionar..')
        d = str(input('Quer continuar?'))
print(f'Finalizado com sucesso!\nAqui está sua lista: {ass}')