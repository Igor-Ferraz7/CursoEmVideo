br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
c = '\033[36m'
des = '\033[m'
i = int(input('Idade do garoto:'))
if i in [0,1,2,3,4,5,6,7,8,9]:
    print('Sua categoria é Mirim.')
elif i in [10,11,12,13,14]:
    print('Sua categoria é Infantil.')
elif i in [15,16,17,18,19]:
    print('Sua categoria é Júnior.')
elif i == 20:
    print('Sua categoria é Sênior.')
else:
    print('Sua categoria é Master.')