s = 0
cs = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n
        cs += 1
print(f'A soma dos {cs} valores pares é {s}')