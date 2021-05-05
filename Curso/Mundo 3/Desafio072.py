t = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
tp = int(input('Digite um número entre 0 e 10: '))
hh = '-='
for c in t:
    if tp > 10 or tp < 0:
        print(hh * 21)
        tp = int(input(f'Esse número não é aceito. Tente novamente.\n{hh*21}\nDigite um número entre 0 e 10: '))
print(f'O número digitado foi o {t[tp]}.')
print(hh * 21)
asd = 'FIM'
print(f'{asd:-^42}')
print(hh * 21)