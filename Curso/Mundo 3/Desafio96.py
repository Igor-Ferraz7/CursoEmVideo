def t(txt):
    print('-='*15)
    print(f'{txt:^30}')
    print('-=' * 15)


t('Controle de terrenos')
la = float(input('Largura(m): '))
com = float(input('Comprimento(m): '))
def cdt(a, b):
    vz = a * b
    print(f'A área de um terreno {la:.1f}x{com:.1f} é {vz:.1f}m²')


cdt(la, com)