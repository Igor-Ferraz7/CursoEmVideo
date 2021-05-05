n = 1
pa = 0
im = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pa += 1
        else:
            im += 1
if pa > 1:
    print(f'{pa} pares.')
elif pa == 1:
    print(f'{pa} par.')
if im > 1:
    print(f'{im} impares.')
elif im == 1:
    print(f'{im} impar.')