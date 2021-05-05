nome = str(input('Digite seu nome:'))
nm = nome.upper()
nmn = nome.lower()
lt = nome.split()
pnh = lt[0]
llt = len(''.join(lt))
pn = len(pnh)
print(f"""Nome com todas as letras maiúsculas: {nm}
Nome com todas as letras minúsculas: {nmn}
Sua quantidade de letras são(sem contar os espaços contidos): {llt}
O primeiro nome tem: {pn} letras""")