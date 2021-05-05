dic = {}
dic['Nome'] = str(input('Nome: '))
dic['Idade'] = int(input('Data de nascimento: '))
dic['Carteira de trabalho'] = int(input('Carteira de trabalho:(0 não tem) '))
if dic['Carteira de trabalho'] != 0:
    dic['Ano de contratação'] = int(input('Ano de contratação: '))
    dic['Salário'] = float(input('Salário: R$'))
    dic['Aposentadoria'] = dic['Ano de contratação'] - dic['Idade'] - 35 * -1
dic['Idade'] = 2020 - dic['Idade']
print('=-'*30)
for k, v in dic.items():
    print(f'- {k}: {v}')
print('=-'*30)
