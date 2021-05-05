import random
dsf = 'Desafio'
print(f'{dsf:=^33}')
pa = str(input('Primeiro aluno:'))
sa = str(input('Segundo aluno:'))
ta = str(input('Terceiro aluno:'))
qa = str(input('Quarto aluno:'))
lista = [pa,sa,ta,qa]
r = random.choice(lista)
print(f'{r}')
print('='*33)