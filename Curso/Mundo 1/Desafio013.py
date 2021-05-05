dsf = 'Desafio'
print(f'{dsf:=^87}')
dias = float(input('Quantos dias?:'))
Km = float(input('Quantos kilometros?:'))
pgd = 60 * dias
pgkm = Km * 0.15
pgf = pgd + pgkm
print(f'Seu preço a pagar pelo carro alugado após {dias:.0f} dias e de {Km}km rodados é de R${pgf:.2f}')
print('='*87)