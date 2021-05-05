br = '\033[30m'
vm = '\033[31m'
vd = '\033[32m'
a = '\033[33m'
az = '\033[34m'
r = '\033[35m'
ci = '\033[36m'
des = '\033[m'
t = int(input('Digite o primeiro termo: '))
rz = int(input('Digite sua razão: '))
for c in range(t, t+rz*10, rz):
    print(c, end=' ')