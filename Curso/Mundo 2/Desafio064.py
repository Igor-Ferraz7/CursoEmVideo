#c = 0
#cont = 0
#sm = 0
#while c != 999:
#    c = int(input('Digite um número [999 para parar]: '))
#    cont += 1
#    sm += c
#print(f'Você digitou {cont-1} números, e a soma entre eles é {sm-999}.')
######or######
cont = 0
sm = 0
c = int(input('Digite um número [999 para parar]: '))
while c != 999:
    cont += 1
    sm += c
    c = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números, e a soma entre eles é {sm}.')