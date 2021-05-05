br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
am = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
t = '-' * 30
def inhelp(n):
    help(n)


a = 'Sistema de ajuda PyHelp'
print(f'{vd}{t}')
print(f"{c}{a:^30}")
print(f'{vd}{t}')
while True:
    ns = input(f'{az}Função ou biblioteca > ')
    if ns == 'fim':
        print(f'{vm}{t}')
        bd = 'Até logo!'
        print(f'{br}{bd:^30}')
        print(f'{vm}{t}')
        break
    else:
        print(c)
        inhelp(ns)
        print(f'{vd}{t}')

#
#or
#
# def ajuda(com):
#     help(com)
#
#
# while True:
#     coma = input('Função ou biblioteca > ')
#     if coma == 'fim':
#         print('See you later!')
#         break
#     else:
#         ajuda(coma)
