def voto(n):
    id = 2021 - n
    if id < 16:
        print(f'Com {id} anos: Voto negado.')
    if 16 <= id < 18 or id > 70:
        print(f'Com {id} anos: Voto Opcional/Facultativo.')
    if 18 <= id <= 70:
        print(f'Com {id} anos: Voto Obrigatório')


a = int(input('Ano de nascimento: '))
voto(a)
