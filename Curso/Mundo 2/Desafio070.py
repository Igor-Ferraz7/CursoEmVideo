prm = sm = ma = mn = pr = 0
asd = 'Mercado'
print('-=' * 30)
print(f'{asd:-^60}')
while True:
    pr += 1
    print('-=' * 30)
    nome = str(input(f'Nome do {pr}º produto: '))
    preco = float(input(f'Preço do {pr}º produto: R$'))
    if preco > 1000:
        prm += 1
    sm += preco
    if pr == 1:
        ma = preco
        mn = preco
    if preco > ma:
        ma = preco
    if preco < mn:
        mn = preco
        bra = nome
    print('-=' * 30)
    esc = str(input('Quer continuar?[S/N]: ')).upper()
    if esc == 'N':
        break
print('-=' * 30)
print(f'Total gasto: {sm:.2f}\nHá {prm} produtos com o custo de mais de mil reais.\nO produto mais barato é a(o) {bra} custando R${mn:.2f}')
print('-=' * 30)
