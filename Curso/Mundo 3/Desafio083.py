br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
am = '\033[33m'
az = '\033[34m'
r = '\033[35m'
ci = '\033[36m'
des = '\033[m'
a = str(input('Digite sua expressão: '))
pilha = []
for simb in a:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[32mSua expressão está certa\033[30m.')
elif len(pilha) != 0:
    print('\033[31mSua expressão está errada\033[30m.')