n = float(input('Qual foi a velocidade? '))
if n < 80:
    print('Ok,sua velocidade não passsou do limite, pode processeguir.')
elif n > 80:
    tst = n - 80
    multa = tst * 7
    print(f'Você ultrapassou o limite de velocidade, e terá de pagar uma multa de R${multa:.2f}')