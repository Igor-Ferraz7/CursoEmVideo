dic = {}
dic['Nome'] = str(input('Nome: '))
dic['Média'] = float(input('Média: '))
if dic['Média'] >= 7.0:
    dic['Situação'] = 'Aprovado!'
elif 5 <= dic['media'] < 7.0:
    dic['Situação'] = 'Recuperação..'
elif dic['Média'] < 7.0:
    dic['Situação'] = 'Reprovado!'
for k, v in dic.items():
    print(f'{k} é igual a: {v}')