import random
dsf = 'Desafio'
print(f'{dsf:=^33}')
pa = str(input('Primeiro aluno:'))
sa = str(input('Segundo aluno:'))
ta = str(input('Terceiro aluno:'))
qa = str(input('Quarto aluno:'))
lista = [pa, sa, ta, qa]
random.shuffle(lista)
print(f"A ordem será:\n{lista}")
print('='*33)
#deck = a.split()
#random.shuffle(deck)