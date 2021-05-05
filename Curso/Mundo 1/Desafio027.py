n = str(input('Diga seu nome completo:')).strip()
cr = n.split()
pn = cr[0]
un = cr[len(cr)-1]
print(f'Seu primeiro nome é:{pn}\nE o último é:{un}')