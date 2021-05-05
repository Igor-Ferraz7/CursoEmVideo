s = 0
c = 0
for n in range(1, 501):
    if n % 2 == 1:
        if n % 3 == 0:
            c += 1
            s += n
print(f'A soma de todos os {c} valores é {s}.')