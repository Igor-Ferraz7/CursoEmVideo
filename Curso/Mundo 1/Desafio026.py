n = str(input('Diga uma frase:')).lower().strip()
c = n.count('a')
fp = n.find('a') +1
fu = n.rfind('a') +1
print(f'A letra "a" apareceu {c} vezes.\nA letra "a" apareceu na posição:{fp}\nE pela última vez na posição:{fu}')