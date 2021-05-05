br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
pm = 0
pn = 0
s = 0
for c in range(1, 6):
    s += 1
    ps = float(input(f'Digite o peso da {s}° pessoa: '))
    if ps == 1:
        pm = ps
        pn = ps
    else:
        if ps > pm:
            pm = ps
        elif ps < pm:
            pn = ps
print(f'O peso {pm} é o maior.\nJá o peso {pn} é o menor.')