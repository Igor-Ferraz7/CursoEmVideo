import random, time
br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
rx = '\033[35m'
c = '\033[36m'
des = '\033[m'
ha = str(input(f'{c}Preparado{br}? ')).upper()
if ha == 'SIM' or 's':
    print(f'{az}Ok então{br}!!')
    print(f"""{rx}Esses são os comandos que você pode escolher para jogar{br}:
    [1] {vm}Pedra{br}
    [2] {az}Papel{br}
    [3] {a}Tesoura{des}""")
    lista = ['pedra', 'papel', 'tesoura']
    r = random.choice(lista)
    es = int(input(f'{c}Digite sua escolha{br}: '))
    print(f'{rx}Vamos lá então{br}!')
    time.sleep(2)
    print(f'{vd}Jo{br}..')
    time.sleep(2)
    print(f'{a}Ken{br}...')
    time.sleep(1)
    print(f'{vm}PÔ{br}! ')
    if r == 'pedra' and es == 1 or r == 'papel' and es == 2 or r == 'tesoura' and es == 3:
        print('\033[33;4mAh, droga. Deu empate!')
    if r == 'pedra' and es == 3:
        print('\033[31;4mHaha, eu ganhei! Escolhi pedra e você tesoura.')
    if r == 'papel' and es == 1:
        print('\033[31;4mHaha, eu ganhei! Escolhi papel e você pedra.')
    if r == 'tesoura' and es == 2:
        print('\033[31;4mHaha eu ganhei! Escolhi tesoura e você papel.')
    if r == 'pedra' and es == 2:
        print('\033[32;4mAh droga, você venceu.. Eu havia escolhido pedra.')
    if r == 'papel' and es == 3:
        print('\033[31;4mAh droga, você venceu.. Eu havia escolhido papel.')
    if r == 'tesoura' and es == 1:
        print('\033[31;4mAh droga, você venceu.. Eu havia escolhido tesoura.')
elif ha == 'NÃO':
    print("""Ah, ok.
    Bye bye""")
else:
    print('Não entendi, repita o processo.')