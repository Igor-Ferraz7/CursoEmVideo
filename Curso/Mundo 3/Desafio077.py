v = ('aprender', 'olhar', 'testar', 'programar')
vr = 'a' or 'e' or 'i' or 'o' or 'u'
for n in v:
    print(f'\nNa palavra {n.upper()} temos: ', end='')
    for l in n:
        if l.lower() in 'aeiou':
            print(l, end=' ')